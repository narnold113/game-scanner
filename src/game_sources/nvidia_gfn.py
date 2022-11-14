# import json
import json
from dataclasses import dataclass
from uuid import uuid4

import requests

from game_sources.game_source import GameSource
from games.game import Game, GamePlatform

# from games.game import Game, GamePlatform


@dataclass
class NvidiaGfn(GameSource):
    def __init__(self) -> None:
        super().__init__()
        self.url = "https://gfnsdk.developer.nvidiagrid.net/api/1/products/gfn/games"

    def __get_data(self, url):
        response = requests.get(url=url)
        return json.loads(response.content)

    def load_games(self) -> None:
        response = self.__get_data(url=self.url)
        for item in response:
            self.games.append(
                Game(
                    title=item["name"],
                    sub_title=None,
                    platform=GamePlatform.NVIDIA_GFN,
                    source_url=self.url,
                    developer=item["launcher"],
                    id=str(uuid4()),
                    thumbnail_image_url=item["imageUrl"],
                )
            )
