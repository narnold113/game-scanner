from game_sources.amazon_luna.amazon_luna_family import AmazonLunaFamily
from game_sources.amazon_luna.amazon_luna_jackbox import AmazonLunaJackbox
from game_sources.amazon_luna.amazon_luna_plus import AmazonLunaPlus
from game_sources.amazon_luna.amazon_luna_prime_gaming import AmazonLunaPrimeGaming
from game_sources.amazon_luna.amazon_luna_retro import AmazonLunaRetro
from game_sources.amazon_luna.amazon_luna_ubisoft_plus import AmazonLunaUbisoftPlus
from game_sources.nvidia_gfn import NvidiaGfn
from game_sources.ps_plus import PsPlus
from game_sources.xbox_cloud import XboxCloud


def main():
    xbox_cloud = XboxCloud()
    xbox_cloud.load_games()
    print(xbox_cloud.games)

    nvidia = NvidiaGfn()
    nvidia.load_games()
    print(nvidia.games)

    amazon_luna_plus = AmazonLunaPlus()
    amazon_luna_plus.load_games()
    print(amazon_luna_plus.games)

    amazon_luna_family = AmazonLunaFamily()
    amazon_luna_family.load_games()
    print(amazon_luna_family.games)

    amazon_luna_retro = AmazonLunaRetro()
    amazon_luna_retro.load_games()
    print(amazon_luna_retro.games)

    amazon_luna_ubisoft_plus = AmazonLunaUbisoftPlus()
    amazon_luna_ubisoft_plus.load_games()
    print(amazon_luna_ubisoft_plus.games)

    amazon_luna_prime_gaming = AmazonLunaPrimeGaming()
    amazon_luna_prime_gaming.load_games()
    print(amazon_luna_prime_gaming.games)

    amazon_luna_jackbox = AmazonLunaJackbox()
    amazon_luna_jackbox.load_games()
    print(amazon_luna_jackbox.games)

    ps_plus = PsPlus()
    ps_plus.load_games()
    print(ps_plus.games)

    pass


if __name__ == "__main__":
    main()
