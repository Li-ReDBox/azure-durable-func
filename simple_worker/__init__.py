# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# This worker only process determinable info

def main(name: str) -> str:
    return f"Hello {name}!"
