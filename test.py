class Printer:
    """A Printer.

    === Attributes ===
    message: the message to print
    """
    message: str

    def __init__(self, message: str) -> None:
        self.message = message

    def print_message(self):
        """Prints a message.
        """
        print(self.message)


class MysteryPrinter(Printer):
    def __init__(self, message: str) -> None:
        Printer.__init__(self, message + message)


class DoublePrinter(MysteryPrinter):
    def print_message(self):
        print(self.message + self.message)
