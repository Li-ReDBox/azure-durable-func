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

    city = name.split(" ")
    if len(city) == 1:
        return f"Hello {name}! Process duration: {start} - {datetime.datetime.now().isoformat()}"

    result = f"{(' ').join(city[1:])}, Hello {city[0]}! Process duration: {start} - {datetime.datetime.now().isoformat()}"
    return result
