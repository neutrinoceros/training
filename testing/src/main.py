def repeated_greetings(name: str, repetitions: int, captitalize: bool = False) -> int:
    from src.greetings import greet

    if captitalize:
        raise NotImplementedError("Capitalization is not implemented yet !")
    for _ in range(repetitions):
        greet(name)
    return 0
