import json
from dataclasses import dataclass

import requests
from bs4 import BeautifulSoup

from game_sources.game_source import GameSource
from games.game import Game, GamePlatform


@dataclass
class XboxCloud(GameSource):
    def __init__(self) -> None:
        super().__init__()
        self.url = "https://www.xbox.com/en-us/play/gallery/all-games"

    def __get_html(self, url):
        response = requests.get(url=url)
        return response.content

    def load_games(self) -> None:
        html = self.__get_html(url=self.url)
        soup = BeautifulSoup(html, "html.parser")
        scripts = soup.find_all("script")

        game_dict = None
        for i, script in enumerate(scripts):
            if script_text := str(script.text).strip():
                if len(script_text) > 1000:
                    script_text = script_text.split("STATE__ = ")[1].strip()
                    script_text = script_text.split("window.env = ")[0].strip().replace(";", "")
                    game_dict = json.loads(script_text)

        if not game_dict:
            print("error getting games")
            raise ValueError

        for game in game_dict["xcloud"]["products"]["data"]:
            self.games.append(
                Game(
                    title=game_dict["xcloud"]["products"]["data"][game]["data"]["title"],
                    sub_title=None,
                    platform=GamePlatform.XBOX_CLOUD,
                    source_url=self.url,
                    developer=None,
                    thumbnail_image_url=None,
                )
            )
