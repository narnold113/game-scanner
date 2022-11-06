from game_sources.xbox_cloud import XboxCloud
from games.game import Game, GamePlatform


def main():
    game1 = Game("Genshin Impact", GamePlatform.XBOX_CLOUD, "hello.com")
    print(game1)

    xbox_cloud = XboxCloud()
    xbox_cloud.load_games()
    print(xbox_cloud.games)


if __name__ == "__main__":
    main()
