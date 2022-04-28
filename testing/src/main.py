def repeated_greetings(name: str, repetitions: int, capitalize: bool = False) -> int:
    from src.greetings import greet

    if capitalize:
        raise NotImplementedError("Capitalization is not implemented yet !")
    for _ in range(repetitions):
        greet(name)
    return 0
