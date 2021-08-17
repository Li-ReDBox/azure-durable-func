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


def orchestrator_partial_return(context: df.DurableOrchestrationContext):
    """Only the results of the second and fourth activity functions are returned to HTTP status"""
    print("Comes into orchestrator")
    yield context.call_activity('worker', "Tokyo")
    result2 = yield context.call_activity('worker', "Seattle")
    yield context.call_activity('worker', "London")
    result4 = yield context.call_activity('worker', "Adelaide")
    return [result2, result4]


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


def orchestrator_no_return(context: df.DurableOrchestrationContext):
    # This returns a value once everything is done, but the retrun value cannot be tested
    print("Comes into orchestrator")
    yield context.call_activity("simple_worker", None)

    for b in ("1", "2", "3"):
        yield context.call_activity("simple_worker", b)

    yield context.call_activity("simple_worker", "dummy")
    return "This is done"

main = df.Orchestrator.create(orchestrator_partial_return)
