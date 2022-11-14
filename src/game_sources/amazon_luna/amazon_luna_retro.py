import json
from dataclasses import dataclass
from uuid import uuid4

import requests

from game_sources.amazon_luna.amazon_luna import AmazonLunaGameSource
from games.game import Game, GamePlatform


@dataclass
class AmazonLunaRetro(AmazonLunaGameSource):
    def __init__(self) -> None:
        super().__init__()
        self.page_id = "B09PZF5XQF"
        self.request_payload["pageContext"]["pageId"] = self.page_id

    def __get_data(self):
        response = requests.post(
            url=self.url,
            headers=self.request_headers,
            json=self.request_payload,
        )
        return json.loads(response.content)

    def load_games(self) -> None:
        json_response = self.__get_data()

        if not json_response:
            print("Error getting Amazon Luna Retro games...")
            raise ValueError

        for widget in json_response["pageMemberGroups"]["mainContent"]["widgets"]:
            if widget["id"] == "collection_channel_games":
                for game_widget in widget["widgets"]:
                    if game_widget["type"] == "GAME_TILE":
                        game_info = json.loads(game_widget["presentationData"])
                        self.games.append(
                            Game(
                                title=str(game_info["title"]).strip(),
                                sub_title=None,
                                platform=GamePlatform.AMAZON_LUNA_RETRO,
                                source_url=self.url,
                                id=str(uuid4()),
                                developer=None,
                                thumbnail_image_url=str(game_info["imageLandscape"]),
                            )
                        )
