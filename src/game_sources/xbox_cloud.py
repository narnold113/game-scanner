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
                    # with open("game.txt", "w") as f:
                    #     f.write(script_text)
                    # print(script_text)
                    game_dict = json.loads(script_text)

        if not game_dict:
            print("error getting games")
            raise ValueError

        for game in game_dict["xcloud"]["products"]["data"]:
            self.games.append(
                Game(
                    game_dict["xcloud"]["products"]["data"][game]["data"]["title"],
                    GamePlatform.XBOX_CLOUD.value,
                    self.url,
                )
            )
