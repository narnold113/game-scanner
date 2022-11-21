from dataclasses import dataclass

import requests
from bs4 import BeautifulSoup

from game_sources.game_source import GameSource
from games.game import Game, GamePlatform


@dataclass
class PsPlus(GameSource):
    def __init__(self) -> None:
        super().__init__()
        self.url = "https://www.playstation.com/en-bg/ps-plus/games/"

    def __get_html(self, url):
        response = requests.get(url=url)
        return response.content

    def load_games(self) -> None:
        html = self.__get_html(url=self.url)
        soup = BeautifulSoup(html, "html.parser")
        section = soup.find_all("div", class_="section")[1]
        p_games = section.find_all("p", class_="txt-style-base")

        if len(p_games) < 300:
            print("Failed to load PS Plus games")
            raise ValueError

        for p_game in p_games[2:]:
            game_title = p_game.text
            if game_title:
                self.games.append(
                    Game(
                        title=game_title,
                        sub_title=None,
                        platform=GamePlatform.PS_PLUS,
                        source_url=self.url,
                        developer=None,
                        thumbnail_image_url=None,
                    )
                )
