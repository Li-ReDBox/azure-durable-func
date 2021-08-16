## General reference from Azure
https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python

## Create a durable function app
```shell
# remember to run the command from a clean directory
func function new -l python -t "Durable Functions HTTP starter" -n starter -a function
func function new -l python -t "Durable Functions orchestrator" -n orchestrator
func function new -l python -t "Durable Functions activity" -n worker

# download configuration from azure to create a local.settings.json (not tracked by git)
func azure functionapp fetch-app-settings YOUR_AZURE_APP
```

## Run locally
```shell
func start --python
Found Python version 3.8.2 (python3).

Azure Functions Core Tools
Core Tools Version:       3.0.3442 Commit hash: 6bfab24b2743f8421475d996402c398d2fe4a9e0  (64-bit)
Function Runtime Version: 3.0.15417.0


Functions:

	starter: [POST,GET] http://localhost:7071/api/orchestrators/{functionName}

	orchestrator: orchestrationTrigger

	worker: activityTrigger

For detailed output, run func with --verbose flag.
```

## Run unit tests
```shell
python -m unittest tests/test_orchestrator.py
```

## Trigger locally
```shell
curl -v http://localhost:7071/api/orchestrators/orchestrator

{
    "id": "03ba0f9f26644ecaa79ab28ea9607d70",
    "statusQueryGetUri": "http://localhost:7071/runtime/webhooks/durabletask/instances/03ba0f9f26644ecaa79ab28ea9607d70?taskHub=TestHubName&connection=Storage&code=gYt5a9WGS2ATVbEAqtg5WGzY0QTVP3rjzJoC2K3k/jjLHojFESKTgw==",
    "sendEventPostUri": "http://localhost:7071/runtime/webhooks/durabletask/instances/03ba0f9f26644ecaa79ab28ea9607d70/raiseEvent/{eventName}?taskHub=TestHubName&connection=Storage&code=gYt5a9WGS2ATVbEAqtg5WGzY0QTVP3rjzJoC2K3k/jjLHojFESKTgw==",
    "terminatePostUri": "http://localhost:7071/runtime/webhooks/durabletask/instances/03ba0f9f26644ecaa79ab28ea9607d70/terminate?reason={text}&taskHub=TestHubName&connection=Storage&code=gYt5a9WGS2ATVbEAqtg5WGzY0QTVP3rjzJoC2K3k/jjLHojFESKTgw==",
    "rewindPostUri": "http://localhost:7071/runtime/webhooks/durabletask/instances/03ba0f9f26644ecaa79ab28ea9607d70/rewind?reason={text}&taskHub=TestHubName&connection=Storage&code=gYt5a9WGS2ATVbEAqtg5WGzY0QTVP3rjzJoC2K3k/jjLHojFESKTgw==",
    "purgeHistoryDeleteUri": "http://localhost:7071/runtime/webhooks/durabletask/instances/03ba0f9f26644ecaa79ab28ea9607d70?taskHub=TestHubName&connection=Storage&code=gYt5a9WGS2ATVbEAqtg5WGzY0QTVP3rjzJoC2K3k/jjLHojFESKTgw==",
    "restartPostUri": "http://localhost:7071/runtime/webhooks/durabletask/instances/03ba0f9f26644ecaa79ab28ea9607d70/restart?taskHub=TestHubName&connection=Storage&code=gYt5a9WGS2ATVbEAqtg5WGzY0QTVP3rjzJoC2K3k/jjLHojFESKTgw=="
}

# use statusQueryGetUri link to check the result
```


## replay history: need to pay attention what code to put in the orchestrator function
**Three activities: 3 + 1 histories**
```log
[2021-07-06T07:28:04.447Z] Executing 'Functions.orchestrator' (Reason='(null)', Id=ad2da907-a59f-40e6-9f28-da2971bd4d1a)
[2021-07-06T07:28:04.459Z] Comes into orchestrator
[2021-07-06T07:28:04.478Z] Executed 'Functions.orchestrator' (Succeeded, Id=ad2da907-a59f-40e6-9f28-da2971bd4d1a, Duration=38ms)
[2021-07-06T07:28:04.639Z] Executing 'Functions.worker' (Reason='(null)', Id=03c52b30-704f-416e-92c1-dfb573b4e5ce)
[2021-07-06T07:28:04.641Z] Executed 'Functions.worker' (Succeeded, Id=03c52b30-704f-416e-92c1-dfb573b4e5ce, Duration=3ms)
[2021-07-06T07:28:04.964Z] Executing 'Functions.orchestrator' (Reason='(null)', Id=2aef0d17-1ee7-4b48-81f9-2e553aab3680)
[2021-07-06T07:28:04.967Z] Comes into orchestrator
[2021-07-06T07:28:04.971Z] Executed 'Functions.orchestrator' (Succeeded, Id=2aef0d17-1ee7-4b48-81f9-2e553aab3680, Duration=8ms)
[2021-07-06T07:28:05.108Z] Executing 'Functions.worker' (Reason='(null)', Id=cd88c0a3-41c6-4a4d-ac3b-1ff60fdbcd15)
[2021-07-06T07:28:05.110Z] Executed 'Functions.worker' (Succeeded, Id=cd88c0a3-41c6-4a4d-ac3b-1ff60fdbcd15, Duration=2ms)
[2021-07-06T07:28:05.373Z] Executing 'Functions.orchestrator' (Reason='(null)', Id=bb0aef03-beed-4c7f-b4e1-3db00febad38)
[2021-07-06T07:28:05.378Z] Comes into orchestrator
[2021-07-06T07:28:05.379Z] Executed 'Functions.orchestrator' (Succeeded, Id=bb0aef03-beed-4c7f-b4e1-3db00febad38, Duration=7ms)
[2021-07-06T07:28:05.506Z] Executing 'Functions.worker' (Reason='(null)', Id=66e3d1f4-c4f4-4bf3-8b9c-9896f9839a84)
[2021-07-06T07:28:05.509Z] Executed 'Functions.worker' (Succeeded, Id=66e3d1f4-c4f4-4bf3-8b9c-9896f9839a84, Duration=2ms)
[2021-07-06T07:28:05.772Z] Executing 'Functions.orchestrator' (Reason='(null)', Id=e0b4bf75-10dc-41cd-8c84-11ce5f3ae7e4)
[2021-07-06T07:28:05.776Z] Comes into orchestrator
[2021-07-06T07:28:05.780Z] Executed 'Functions.orchestrator' (Succeeded, Id=e0b4bf75-10dc-41cd-8c84-11ce5f3ae7e4, Duration=7ms)
```

**Four activities: 4 + 1 histories**
```log
[2021-07-06T07:33:56.423Z] Executing 'Functions.orchestrator' (Reason='(null)', Id=b6d3f402-43fd-4f46-a5c8-bc7672b69e83)
[2021-07-06T07:33:56.430Z] Comes into orchestrator
[2021-07-06T07:33:56.449Z] Executed 'Functions.orchestrator' (Succeeded, Id=b6d3f402-43fd-4f46-a5c8-bc7672b69e83, Duration=29ms)
[2021-07-06T07:33:56.626Z] Executing 'Functions.worker' (Reason='(null)', Id=3d3a41af-a8ae-417e-a911-8f29904b0d17)
[2021-07-06T07:33:56.629Z] Executed 'Functions.worker' (Succeeded, Id=3d3a41af-a8ae-417e-a911-8f29904b0d17, Duration=3ms)
[2021-07-06T07:33:56.923Z] Executing 'Functions.orchestrator' (Reason='(null)', Id=b39cd851-4bbb-44c7-900a-1270f2c52b36)
[2021-07-06T07:33:56.925Z] Comes into orchestrator
[2021-07-06T07:33:56.929Z] Executed 'Functions.orchestrator' (Succeeded, Id=b39cd851-4bbb-44c7-900a-1270f2c52b36, Duration=8ms)
[2021-07-06T07:33:57.052Z] Executing 'Functions.worker' (Reason='(null)', Id=d8e63b31-01f3-4c8b-9525-03a569a5b4b5)
[2021-07-06T07:33:57.055Z] Executed 'Functions.worker' (Succeeded, Id=d8e63b31-01f3-4c8b-9525-03a569a5b4b5, Duration=2ms)
[2021-07-06T07:33:57.320Z] Executing 'Functions.orchestrator' (Reason='(null)', Id=2de3c0b8-0afa-4510-a7f9-f9507b70f835)
[2021-07-06T07:33:57.323Z] Comes into orchestrator
[2021-07-06T07:33:57.325Z] Executed 'Functions.orchestrator' (Succeeded, Id=2de3c0b8-0afa-4510-a7f9-f9507b70f835, Duration=6ms)
[2021-07-06T07:33:57.470Z] Executing 'Functions.worker' (Reason='(null)', Id=163189b4-86d6-47f2-b045-536f06b9fc06)
[2021-07-06T07:33:57.473Z] Executed 'Functions.worker' (Succeeded, Id=163189b4-86d6-47f2-b045-536f06b9fc06, Duration=3ms)
[2021-07-06T07:33:57.716Z] Executing 'Functions.orchestrator' (Reason='(null)', Id=8607f7f6-7126-415a-b70b-d683356fff0e)
[2021-07-06T07:33:57.720Z] Comes into orchestrator
[2021-07-06T07:33:57.721Z] Executed 'Functions.orchestrator' (Succeeded, Id=8607f7f6-7126-415a-b70b-d683356fff0e, Duration=5ms)
[2021-07-06T07:33:57.866Z] Executing 'Functions.worker' (Reason='(null)', Id=563c71ad-98a6-4522-8253-4995e781324e)
[2021-07-06T07:33:57.869Z] Executed 'Functions.worker' (Succeeded, Id=563c71ad-98a6-4522-8253-4995e781324e, Duration=2ms)
[2021-07-06T07:33:58.126Z] Executing 'Functions.orchestrator' (Reason='(null)', Id=3283ada2-afa6-4307-8931-ffc9549d0246)
[2021-07-06T07:33:58.131Z] Comes into orchestrator
[2021-07-06T07:33:58.136Z] Executed 'Functions.orchestrator' (Succeeded, Id=3283ada2-afa6-4307-8931-ffc9549d0246, Duration=11ms)
```
```json
{
    "name": "orchestrator",
    "instanceId": "f96a605b57a04a628df44e442f2d979a",
    "runtimeStatus": "Completed",
    "input": null,
    "customStatus": null,
    "output": [
        "Hello Tokyo! Process duration: 2021-07-07T09:19:07.664256 - 2021-07-07T09:19:11.612766",
        "Hello Seattle! Process duration: 2021-07-07T09:19:11.830690 - 2021-07-07T09:19:14.500532",
        "Hello London! Process duration: 2021-07-07T09:19:14.705451 - 2021-07-07T09:19:17.624469",
        "Hello Adelaide! Process duration: 2021-07-07T09:19:17.825359 - 2021-07-07T09:19:25.869143"
    ],
    "createdTime": "2021-07-06T23:49:07Z",
    "lastUpdatedTime": "2021-07-06T23:49:26Z"
}
```

**Fan Out: one yield, 3 histories**
```log
[2021-07-07T01:29:17.187Z] Executing 'Functions.orchestrator' (Reason='(null)', Id=2dfbdc1f-9698-44f8-9d28-39179fecc02f)
[2021-07-07T01:29:17.198Z] Comes into orchestrator
[2021-07-07T01:29:17.220Z] Executed 'Functions.orchestrator' (Succeeded, Id=2dfbdc1f-9698-44f8-9d28-39179fecc02f, Duration=41ms)
[2021-07-07T01:29:17.309Z] Executing 'Functions.worker' (Reason='(null)', Id=e932c49c-64c6-4a37-a955-8b986054cf76)
[2021-07-07T01:29:17.331Z] Executing 'Functions.worker' (Reason='(null)', Id=d16fdc50-e9cf-44ec-83f1-00315f28494c)
[2021-07-07T01:29:17.360Z] Executing 'Functions.worker' (Reason='(null)', Id=edc400d1-65bb-43e3-a920-f8fb0eff3283)
[2021-07-07T01:29:17.390Z] Executing 'Functions.worker' (Reason='(null)', Id=7afea3fc-c8f5-414d-a15d-1dab636d56ef)
[2021-07-07T01:29:19.517Z] Executed 'Functions.worker' (Succeeded, Id=e932c49c-64c6-4a37-a955-8b986054cf76, Duration=2209ms)
[2021-07-07T01:29:19.675Z] Executing 'Functions.orchestrator' (Reason='(null)', Id=8c0b3150-48b5-4981-840f-2daafe147304)
[2021-07-07T01:29:24.363Z] Executed 'Functions.worker' (Succeeded, Id=d16fdc50-e9cf-44ec-83f1-00315f28494c, Duration=7032ms)
[2021-07-07T01:29:27.683Z] Executed 'Functions.worker' (Succeeded, Id=edc400d1-65bb-43e3-a920-f8fb0eff3283, Duration=10323ms)
[2021-07-07T01:29:33.158Z] Comes into orchestrator
[2021-07-07T01:29:33.159Z] Executed 'Functions.worker' (Succeeded, Id=7afea3fc-c8f5-414d-a15d-1dab636d56ef, Duration=15769ms)
[2021-07-07T01:29:33.168Z] Executed 'Functions.orchestrator' (Succeeded, Id=8c0b3150-48b5-4981-840f-2daafe147304, Duration=13495ms)
[2021-07-07T01:29:33.343Z] Executing 'Functions.orchestrator' (Reason='(null)', Id=6fe09d8d-9186-4fff-95c4-022d0b2109f6)
[2021-07-07T01:29:33.348Z] Comes into orchestrator
[2021-07-07T01:29:33.352Z] Executed 'Functions.orchestrator' (Succeeded, Id=6fe09d8d-9186-4fff-95c4-022d0b2109f6, Duration=19ms)
```

**Chaining 4 activities: 4 yields, 4 + 1 histories, activities take time to process**
```log
[2021-08-14T01:38:18.138Z] Executing 'Functions.orchestrator' (Reason='(null)', Id=d7ccbe5b-8edf-42d5-abd1-d22cf2cf6b8b)
[2021-08-14T01:38:18.149Z] Comes into orchestrator
[2021-08-14T01:38:18.166Z] Executed 'Functions.orchestrator' (Succeeded, Id=d7ccbe5b-8edf-42d5-abd1-d22cf2cf6b8b, Duration=34ms)
[2021-08-14T01:38:18.337Z] Executing 'Functions.worker' (Reason='(null)', Id=9f1b5db1-8e8f-490f-9a42-9b4ac4b00b49)
[2021-08-14T01:38:23.462Z] Executed 'Functions.worker' (Succeeded, Id=9f1b5db1-8e8f-490f-9a42-9b4ac4b00b49, Duration=5127ms)
[2021-08-14T01:38:23.775Z] Executing 'Functions.orchestrator' (Reason='(null)', Id=ad21e972-0229-4f15-a438-e066ece5d241)
[2021-08-14T01:38:23.779Z] Comes into orchestrator
[2021-08-14T01:38:23.779Z] Hello Tokyo! Process duration: 2021-08-14T11:08:18.338901 - 2021-08-14T11:08:23.460011
[2021-08-14T01:38:23.782Z] Executed 'Functions.orchestrator' (Succeeded, Id=ad21e972-0229-4f15-a438-e066ece5d241, Duration=8ms)
[2021-08-14T01:38:24.132Z] Executing 'Functions.worker' (Reason='(null)', Id=284b1f44-32d5-4a8f-9580-9e86549a5c99)
[2021-08-14T01:38:25.593Z] Executed 'Functions.worker' (Succeeded, Id=284b1f44-32d5-4a8f-9580-9e86549a5c99, Duration=1461ms)
[2021-08-14T01:38:25.885Z] Executing 'Functions.orchestrator' (Reason='(null)', Id=6e183685-595e-45c7-9304-5a29e10509c1)
[2021-08-14T01:38:25.889Z] Comes into orchestrator
[2021-08-14T01:38:25.889Z] Hello Tokyo! Process duration: 2021-08-14T11:08:18.338901 - 2021-08-14T11:08:23.460011
[2021-08-14T01:38:25.890Z] Executed 'Functions.orchestrator' (Succeeded, Id=6e183685-595e-45c7-9304-5a29e10509c1, Duration=5ms)
[2021-08-14T01:38:25.988Z] Executing 'Functions.worker' (Reason='(null)', Id=cc84dfaf-b1de-443c-af85-b58fc5c92133)
[2021-08-14T01:38:27.757Z] Executed 'Functions.worker' (Succeeded, Id=cc84dfaf-b1de-443c-af85-b58fc5c92133, Duration=1769ms)
[2021-08-14T01:38:28.032Z] Executing 'Functions.orchestrator' (Reason='(null)', Id=8bb97097-9c65-40b6-9ba7-e1a1bb98cdcf)
[2021-08-14T01:38:28.038Z] Comes into orchestrator
[2021-08-14T01:38:28.039Z] Hello Tokyo! Process duration: 2021-08-14T11:08:18.338901 - 2021-08-14T11:08:23.460011
[2021-08-14T01:38:28.041Z] Executed 'Functions.orchestrator' (Succeeded, Id=8bb97097-9c65-40b6-9ba7-e1a1bb98cdcf, Duration=9ms)
[2021-08-14T01:38:28.133Z] Executing 'Functions.worker' (Reason='(null)', Id=9db0bc65-ab85-4d8e-a17c-81e88891a57f)
[2021-08-14T01:38:35.725Z] Executed 'Functions.worker' (Succeeded, Id=9db0bc65-ab85-4d8e-a17c-81e88891a57f, Duration=7592ms)
[2021-08-14T01:38:36.048Z] Executing 'Functions.orchestrator' (Reason='(null)', Id=c5ae7e21-69cf-4e4a-8f54-379f9ef69e63)
[2021-08-14T01:38:36.054Z] Comes into orchestrator
[2021-08-14T01:38:36.054Z] Hello Tokyo! Process duration: 2021-08-14T11:08:18.338901 - 2021-08-14T11:08:23.460011
[2021-08-14T01:38:36.054Z] Hello Tokyo! Process duration: 2021-08-14T11:08:18.338901 - 2021-08-14T11:08:23.460011, Hello Seattle! Process duration: 2021-08-14T11:08:24.133836 - 2021-08-14T11:08:25.589980, Hello London! Process duration: 2021-08-14T11:08:25.990070 - 2021-08-14T11:08:27.756051, Hello Adelaide! Process duration: 2021-08-14T11:08:28.135911 - 2021-08-14T11:08:35.723287
[2021-08-14T01:38:36.058Z] Executed 'Functions.orchestrator' (Succeeded, Id=c5ae7e21-69cf-4e4a-8f54-379f9ef69e63, Duration=10ms)
```
```json
{
    "name": "orchestrator",
    "instanceId": "e733e0b071c74fe59ceb74b62a8aba12",
    "runtimeStatus": "Completed",
    "input": null,
    "customStatus": null,
    "output": "Hello Tokyo! Process duration: 2021-08-14T11:08:18.338901 - 2021-08-14T11:08:23.460011, Hello Seattle! Process duration: 2021-08-14T11:08:24.133836 - 2021-08-14T11:08:25.589980, Hello London! Process duration: 2021-08-14T11:08:25.990070 - 2021-08-14T11:08:27.756051, Hello Adelaide! Process duration: 2021-08-14T11:08:28.135911 - 2021-08-14T11:08:35.723287",
    "createdTime": "2021-08-14T01:38:17Z",
    "lastUpdatedTime": "2021-08-14T01:38:36Z"
}
```


**Run with default settings, no forced concurrency**
```json
{
    "name": "orchestrator",
    "instanceId": "d7a366b5c4ad4f31a8a41704c2028395",
    "runtimeStatus": "Completed",
    "input": null,
    "customStatus": null,
    "output": [
        "Hello Tokyo! Process duration: 2021-07-07T10:59:17.311218 - 2021-07-07T10:59:19.515044",
        "Hello Seattle! Process duration: 2021-07-07T10:59:19.515179 - 2021-07-07T10:59:24.361709",
        "Hello London! Process duration: 2021-07-07T10:59:24.361802 - 2021-07-07T10:59:27.681557",
        "Hello Adelaide! Process duration: 2021-07-07T10:59:27.681698 - 2021-07-07T10:59:33.154568"
    ],
    "createdTime": "2021-07-07T01:29:16Z",
    "lastUpdatedTime": "2021-07-07T01:29:33Z"
}
```

**Run with settings of one activity function on one host**
The background of this setting is on [github](https://github.com/Azure/azure-functions-durable-python/issues/179). More on performance and scale is [here](https://docs.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-perf-and-scale).

An extraction:
```By default, a single function app instance can process multiple executions at the same time. It looks like what happened here is that when_all queued up a few tasks and a single function app instance grabbed them all. But since this is a CPU bound workload, it is only able to work on them one at a time.

Try to lower your maxConcurrentActivity functions to 1. This might seem counterintuitive, but it’s a per instance setting. In this case, a single instance should only grab a single message from the activity work item queue, and this should leave the other activity requests on the queue and the platform should scale out to more instances which will only process one activity at a time. Please give it a try and see if it makes a difference.

If you have access to more CPU cores or if your function doesn’t actually use up all the CPU, you can try increasing the worker process count (this is also per instance): https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python#use-multiple-language-worker-processes

Adding more processes comes with overhead, so experiment with it.
```

```json
  "extensions": {
    "durableTask": {
      "maxConcurrentActivityFunctions": 1
    }
  }
```
```json
{
    "name": "orchestrator",
    "instanceId": "696530d10b6e4d55a500316985041330",
    "runtimeStatus": "Completed",
    "input": null,
    "customStatus": null,
    "output": [
        "Hello Tokyo! Process duration: 2021-07-07T11:25:04.063215 - 2021-07-07T11:25:05.267014",
        "Hello Seattle! Process duration: 2021-07-07T11:25:11.882634 - 2021-07-07T11:25:18.384130",
        "Hello London! Process duration: 2021-07-07T11:25:05.496658 - 2021-07-07T11:25:11.681800",
        "Hello Adelaide! Process duration: 2021-07-07T11:25:18.583105 - 2021-07-07T11:25:22.232036"
    ],
    "createdTime": "2021-07-07T01:55:03Z",
    "lastUpdatedTime": "2021-07-07T01:55:22Z"
}
```

The considerations of orchestrator and activity functions from the [official document](https://docs.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-perf-and-scale):

**Thread usage**

Orchestrator functions are executed on a single thread to ensure that execution can be deterministic across many replays. Because of this single-threaded execution, it's important that orchestrator function threads do not perform CPU-intensive tasks, do I/O, or block for any reason. Any work that may require I/O, blocking, or multiple threads should be moved into activity functions.

Activity functions have all the same behaviors as regular queue-triggered functions. They can safely do I/O, execute CPU intensive operations, and use multiple threads. Because activity triggers are stateless, they can freely scale out to an unbounded number of VMs.

Basically orchestrator is just for controlling flow, so make it is simple.

**Concurrency throttles**

Azure Functions supports executing multiple functions concurrently within a single app instance. This concurrent execution helps increase parallelism and minimizes the number of "cold starts" that a typical app will experience over time. However, high concurrency can exhaust per-VM system resources such network connections or available memory. Depending on the needs of the function app, it may be necessary to throttle the per-instance concurrency to avoid the possibility of running out of memory in high-load situations.

Activity and orchestrator function concurrency limits can be configured in the `host.json` file. The relevant settings are `durableTask/maxConcurrentActivityFunctions` for activity functions and `durableTask/maxConcurrentOrchestratorFunctions` for orchestrator function. These settings control the maximum number of orchestrator or activity functions that can be loaded into memory concurrently.

**Language runtime considerations**
The language runtime you select may impose strict concurrency restrictions on your functions. For example, Durable Function apps written in Python or PowerShell may only support running a single function at a time on a single VM. This can result in significant performance problems if not carefully accounted for. For example, if an orchestrator fans-out to 10 activities but the language runtime restricts concurrency to just one function, then 9 of the 10 activity functions will be stuck waiting for a chance to run. Furthermore, these 9 stuck activities will not be able to be load balanced to any other workers because the Durable Functions runtime will have already loaded them into memory. This becomes especially problematic if the activity functions are long-running.

Python places a restriction on concurrency, you should update the Durable Functions concurrency settings to match the concurrency settings of Python. This ensures that the Durable Functions runtime will not attempt to run more functions concurrently than is allowed by Python runtime, allowing any pending activities to be load balanced to other VMs. For example, if you have a Python app that restricts concurrency to 4 functions (perhaps it's only configured with 4 threads on a single language worker process or 1 thread on 4 language worker processes) then you should configure both `maxConcurrentOrchestratorFunctions` and `maxConcurrentActivityFunctions` to `4`.

For more information and performance recommendations for Python, see [Improve throughput performance of Python apps](https://docs.microsoft.com/en-us/azure/azure-functions/python-scale-performance-reference) in Azure Functions. The techniques mentioned in this Python developer reference documentation can have a substantial impact on Durable Functions performance and scalability.