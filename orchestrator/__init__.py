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


def orchestrator_activity_chain(context: df.DurableOrchestrationContext):
    print("Comes into orchestrator")
    result1 = yield context.call_activity('worker', "Tokyo")
    print(result1)
    result2 = yield context.call_activity('worker', "Seattle " + result1)
    result3 = yield context.call_activity('worker', "London " + result2)
    result4 = yield context.call_activity('worker', "Adelaide " + result3)
    print(result4)
    return result4


def orchestrator_simple_chain(context: df.DurableOrchestrationContext):
    print("Comes into orchestrator")
    result1 = yield context.call_activity('simple_worker', "Tokyo")
    print(result1)
    result2 = yield context.call_activity('simple_worker', "Seattle " + result1)
    print(result2)
    result3 = yield context.call_activity('simple_worker', "London " + result2)
    print(result3)
    result4 = yield context.call_activity('simple_worker', "Adelaide " + result3)
    print(result4)
    return result4


main = df.Orchestrator.create(orchestrator_activity_chain)
