# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# This worker only process determinable info

def main(name: str) -> str:
    print("In ", __name__, name, " has type of", type(name))

    if name is None:
        return ""

    city = name.split(" ")
    if len(city) == 1:
        return f"Hello {name}!"

    result = f"{(' ').join(city[1:])} Hello {city[0]}!"
    print(f"Will return {result}")
    return result
