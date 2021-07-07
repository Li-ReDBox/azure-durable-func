**Run locally**
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

## replay history
**Three activities: 3 + 1 histories**
```log
[2021-07-06T07:27:32.167Z] Worker process started and initialized.
[2021-07-06T07:27:38.471Z] Host lock lease acquired by instance ID '00000000000000000000000072AD543F'.
[2021-07-06T07:28:03.983Z] Executing 'Functions.starter' (Reason='This function was programmatically called via the host APIs.', Id=3d22cb1a-5212-4463-b8b4-d003de10d963)
[2021-07-06T07:28:04.307Z] Started orchestration with ID = '649ee9314e134e97932cf5294c421133'.
[2021-07-06T07:28:04.368Z] Executed 'Functions.starter' (Succeeded, Id=3d22cb1a-5212-4463-b8b4-d003de10d963, Duration=410ms)
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
[2021-07-06T07:33:52.405Z] Host lock lease acquired by instance ID '00000000000000000000000072AD543F'.
[2021-07-06T07:33:55.797Z] Executing 'Functions.starter' (Reason='This function was programmatically called via the host APIs.', Id=a8ff55a3-e650-4e30-9d35-a3556607bf1e)
[2021-07-06T07:33:56.284Z] Started orchestration with ID = '2a1157aecc58431b8191f75606833219'.
[2021-07-06T07:33:56.285Z] Executed 'Functions.starter' (Succeeded, Id=a8ff55a3-e650-4e30-9d35-a3556607bf1e, Duration=488ms)
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
[2021-07-07T01:29:03.448Z] Worker process started and initialized.
[2021-07-07T01:29:09.480Z] Host lock lease acquired by instance ID '00000000000000000000000072AD543F'.
[2021-07-07T01:29:16.818Z] Executing 'Functions.starter' (Reason='This function was programmatically called via the host APIs.', Id=141b74a7-5860-4d85-b285-516706bafa7c)
[2021-07-07T01:29:17.074Z] Started orchestration with ID = 'd7a366b5c4ad4f31a8a41704c2028395'.
[2021-07-07T01:29:17.135Z] Executed 'Functions.starter' (Succeeded, Id=141b74a7-5860-4d85-b285-516706bafa7c, Duration=339ms)
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
