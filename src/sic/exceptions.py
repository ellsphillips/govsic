from dataclasses import dataclass


@dataclass
class InvalidSICCodeError(Exception):

    message: str

    def __str__(self) -> str:
        return self.message
