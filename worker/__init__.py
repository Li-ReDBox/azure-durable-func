# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# This worker will return time related information, when
# this information will be processed in another activity function, the result
# is interesting.
import datetime
import random
import time


def main(name: str) -> str:
    start = datetime.datetime.now().isoformat()
    time.sleep(random.randint(1, 10000)/1000)
    return f"Hello {name}! Process duration: {start} - {datetime.datetime.now().isoformat()}"
