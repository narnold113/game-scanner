from game import Game, GamePlatform


def main():
    game1 = Game("Genshin Impact", GamePlatform.XBOX_CLOUD, "hello.com")
    print(game1)


if __name__ == "__main__":
    main()
