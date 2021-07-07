# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.
import azure.durable_functions as df


def orchestrator_chain(context: df.DurableOrchestrationContext):
    print("Comes into orchestrator")
    result1 = yield context.call_activity('worker', "Tokyo")
    result2 = yield context.call_activity('worker', "Seattle")
    result3 = yield context.call_activity('worker', "London")
    result4 = yield context.call_activity('worker', "Adelaide")
    return [result1, result2, result3, result4]


def orchestrator_fan(context: df.DurableOrchestrationContext):
    print("Comes into orchestrator")
    tasks = []
    for city in ("Tokyo", "Seattle", "London", "Adelaide"):
        tasks.append(context.call_activity("worker", city))
    results = yield context.task_all(tasks)
    return results


main = df.Orchestrator.create(orchestrator_fan)
