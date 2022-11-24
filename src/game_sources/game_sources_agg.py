from dataclasses import dataclass, field

import pandas as pd

from game_sources.game_source import GameSource
from games.game import Game


@dataclass
class GameSourcesAgg:
    game_sources: list[GameSource] = field(default_factory=list)
    games: list[Game] = field(default_factory=list)

    def load(self) -> None:
        for game_source in self.game_sources:
            try:
                game_source.load_games()
            except Exception as error:
                print(f"Error loading games for {game_source}. Error: {error}")
                raise error

            for game in game_source.games:
                self.games.append(game)

    def build_games_data_frame(self):
        if not self.games:
            print("No games...")

        games_df = pd.DataFrame(
            columns=[
                "title",
                "sub_title",
                "source_url",
                "game_platform",
                "developer",
                "thumbnail_image_url",
            ],
            index=[0],
        )

        for game in self.games:
            game_dict = game.__dict__
            game_dict["platform"] = game.platform.value
            new_row = pd.Series(game_dict)
            games_df = pd.concat(
                [games_df, new_row.to_frame().T],
                ignore_index=True,
            )

        return games_df
