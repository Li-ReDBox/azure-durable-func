from unittest import main
from unittest import TestCase
from unittest.mock import patch

import azure.durable_functions as df

from orchestrator import orchestrator_chain, orchestrator_fan, orchestrator_activity_chain, orchestrator_no_return

# side_effect function for returning various values depending on args.
def spy(activity:str, location:str):
    print("Spying in activity function '%s'" % activity, "with value %s" % location)
    return f'Hello {location}!'


def disappear(activity:str, location:str):
    print("Spying in activity function '%s'" % activity, "with value %s" % location)


class DurableFunctionsOrchestratorTestCase(TestCase):

    def test_chain(self):
        """orchestrator_chain returns a list of tasks - yields"""
        with patch('azure.durable_functions.DurableOrchestrationContext',spec=df.DurableOrchestrationContext) as mock:
            mock.call_activity.side_effect = spy
            result = list(orchestrator_chain(mock))

        print(result)
        self.assertEqual(4, len(result))
        self.assertEqual('Hello Tokyo!',result[0])
        self.assertEqual('Hello Adelaide!',result[3])

    def test_fan(self):
        """orchestrator_fan returns a single yield collection of tasks"""
        with patch('azure.durable_functions.DurableOrchestrationContext',spec=df.DurableOrchestrationContext) as mock:
            mock.call_activity.side_effect = spy
            mock.task_all.side_effect = lambda *args: args
            tasks = orchestrator_fan(mock)
            # Here is a difference of result of task_all
            # why the generator is a tuple if a single element?
            result = next(tasks)[0]
        print(result)
        self.assertEqual(4, len(result))
        self.assertEqual('Hello Tokyo!',result[0])
        self.assertEqual('Hello Adelaide!',result[3])

    def test_orchestrator_activity_chain(self):
        """orchestrator_activity_chain throw exception TypeError, cannot be tested"""
        # It needs some effort to set up a relay in test, so the orchestrator chaing results cannot be tested.
        with patch('azure.durable_functions.DurableOrchestrationContext',spec=df.DurableOrchestrationContext) as mock:
            mock.call_activity.side_effect = spy
            with self.assertRaises(TypeError) as cm:
                list(orchestrator_activity_chain(mock))
        self.assertIsInstance(cm.exception, TypeError)

    def test_orchestrator_no_return(self):
        """orchestrator_no_return has 5 yields, but the values are not captured"""
        with patch('azure.durable_functions.DurableOrchestrationContext',spec=df.DurableOrchestrationContext) as mock:
            mock.call_activity.side_effect = disappear
            result = list(orchestrator_no_return(mock))

        self.assertEqual(5, len(result))
        for n in result:
            self.assertIsNone(n)
