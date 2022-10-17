class HelpMenu:
    def __init__(self) -> None:
        pass

    def display(self) -> None:
        # Probably a better way to do this but it works
        menu = "CLI Password Manager\n\n"
        menu += "Keywords: \n"
        menu += "   generate       Generate a new password (default string of 12 random characters)\n"
        menu += "       options:    -p, --phrase        Generate a password of random words (default 4)\n"
        menu += "                   -l, --length        Generate a password of this length (chars or words)\n"
        menu += "                   -i, --id            The identifier for the credentials\n"
        menu += "                   -u, --username      Credentials username\n"
        menu += "                   -o, --once          Generates a password but is not saved\n"
        menu += "                   -d, --divide        Character to divide phrase password\n"
        menu += "   view           View saved credentials (all by default)\n"
        menu += "       options:    -i, --id            Shows the credentials for this identifier\n"
        menu += "   help           Display information about the tool\n"
        print(menu)
