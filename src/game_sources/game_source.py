from abc import ABC, abstractmethod

from game import Game


class GameSource(ABC):
    def __init__(self, url) -> None:
        self.url = url
        self.games = []

    @abstractmethod
    def get_html(self):
        pass

    @abstractmethod
    def extract_games(self) -> list[Game]:
        pass
