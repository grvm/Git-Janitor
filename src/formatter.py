"""Module to format(Bold/Underline) and colorize output."""


class Formatter:
    """Class to format(Bold/Underline) and colorize output."""

    WARNING_COLOR = '\033[93m'
    FAIL_COLOR = '\033[91m'
    OK_COLOR = '\033[92m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @staticmethod
    def print_pretty_message(color, message):
        """Bolden and colorize text specified."""
        print Formatter.BOLD + color + message + Formatter.ENDC

    @staticmethod
    def print_pretty_ok_message(message):
        """Bolden and colorize text with OK_COLOR."""
        return Formatter.print_pretty_message(Formatter.OK_COLOR, message)

    @staticmethod
    def print_pretty_fail_message(message):
        """Bolden and colorize text with FAIL_COLOR."""
        return Formatter.print_pretty_message(Formatter.FAIL_COLOR, message)

    @staticmethod
    def print_pretty_warn_message(message):
        """Bolden and colorize text with WARN_COLOR."""
        return Formatter.print_pretty_message(Formatter.WARNING_COLOR, message)
