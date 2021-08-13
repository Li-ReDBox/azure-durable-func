from unittest import main
from unittest import TestCase
from unittest.mock import patch

import azure.durable_functions as df

from orchestrator import orchestrator_chain, orchestrator_fan

# side_effect function for returning various values depending on args.
def spy(activity:str, location:str):
    print("Spying in activity function '%s'" % activity, "with value %s" % location)
    return f'Hello {location}!'

class DurableFunctionsOrchestratorTestCase(TestCase):

    def test_chain(self):
        """orchestrator_chain returns a list of tasks - yields"""
        with patch('azure.durable_functions.DurableOrchestrationContext',spec=df.DurableOrchestrationContext) as mock:
            mock.call_activity.side_effect = spy
            result = list(orchestrator_chain(mock))

            self.assertEqual(4,len(result))
            self.assertEqual('Hello Tokyo!',result[0])

    def test_fan(self):
        """orchestrator_fan returns a single collection of tasks"""
        with patch('azure.durable_functions.DurableOrchestrationContext',spec=df.DurableOrchestrationContext) as mock:
            mock.call_activity.side_effect = spy
            mock.task_all.side_effect = lambda *args: args
            tasks = orchestrator_fan(mock)
            # why the generator is a single element of tuple?
            result = next(tasks)[0]

            self.assertEqual(4, len(result))
            self.assertEqual('Hello Tokyo!',result[0])
