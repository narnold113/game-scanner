from abc import ABC, abstractmethod
from dataclasses import dataclass, field

from games.game import Game


@dataclass
class GameSource(ABC):
    games: list[Game] = field(default_factory=list)

    # @abstractmethod
    # def get_html(self):
    #     pass

    @abstractmethod
    def load_games(self) -> None:
        pass
