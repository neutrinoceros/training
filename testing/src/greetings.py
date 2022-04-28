def greet(name: str, file=None) -> None:
    msg = f"Hello {name} !"
    if file is not None:
        with open(file, "w") as fh:
            fh.write(msg)
    else:
        print(msg)


# testing enable refactors !
def greet_v2(name: str, file=None) -> None:
    print(f"Hello {name} !", file=file)
