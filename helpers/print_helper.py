"""Module for prints and inputs"""


class PrintHelper:
    """Helper class for printing"""

    @staticmethod
    def pr_menu(txt):
        """Prints the Menu items in teal color."""
        print("\033[38;5;37m" + txt + "\033[0m")

    @staticmethod
    def pr_error(txt, error=""):
        """Print error messages in red"""
        print("\033[91m" + txt +" "+ error + "\033[0m")

    @staticmethod
    def pr_bold(txt):
        """Prints text in bold"""
        print("\033[1m" + txt + "\033[0m")

    @staticmethod
    def pr_input(txt):
        """Print input prompt in a brownish color (yellow)"""
        return input("\033[33m" + txt + "\033[0m").strip()
