from dataclasses import dataclass


@dataclass
class InvalidSICCodeError(Exception):
    """
    Exception to raise when provided an invalid SIC code.

    Attributes:
        message (str): Message displayed when error is raised.
    """

    message: str

    def __str__(self) -> str:
        return self.message
