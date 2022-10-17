class CommandOptions:
    @property
    def options(self) -> dict[str, str]:
        return self.__options

    def __init__(self) -> None:
        self.__options = {}

    def sort_options(self, args: list[str]) -> None:
        for i, a in enumerate(args):
            if a == "generate" or a == "view" or a == "help":
                self.__options["keyword"] = a
            elif a.startswith("-"):
                nextIdx = i + 1
                nextOpt = "" if nextIdx >= len(args) else args[nextIdx]
                self.__options[a] = nextOpt

