import abc


class APIBase(abc.ABC):
    def __init__(self, settings: dict) -> None:
        self.settings = settings


class APIBaseAsync(abc.ABC):
    def __init__(self, settings: dict) -> None:
        self.settings = settings
