import os
from configparser import ConfigParser

from clients.s3_client import S3Client
from game_sources.amazon_luna.amazon_luna_family import AmazonLunaFamily
from game_sources.amazon_luna.amazon_luna_jackbox import AmazonLunaJackbox
from game_sources.amazon_luna.amazon_luna_plus import AmazonLunaPlus
from game_sources.amazon_luna.amazon_luna_prime_gaming import AmazonLunaPrimeGaming
from game_sources.amazon_luna.amazon_luna_retro import AmazonLunaRetro
from game_sources.amazon_luna.amazon_luna_ubisoft_plus import AmazonLunaUbisoftPlus
from game_sources.game_sources_agg import GameSourcesAgg
from game_sources.nvidia_gfn import NvidiaGfn
from game_sources.ps_plus import PsPlus
from game_sources.xbox_cloud import XboxCloud

config = ConfigParser(os.environ)
config.read("config.ini")


def main():
    game_sources_agg = GameSourcesAgg()

    game_sources_agg.game_sources.append(XboxCloud())
    # game_sources_agg.game_sources.append(NvidiaGfn())
    # game_sources_agg.game_sources.append(AmazonLunaPlus())
    # game_sources_agg.game_sources.append(AmazonLunaFamily())
    # game_sources_agg.game_sources.append(AmazonLunaRetro())
    # game_sources_agg.game_sources.append(AmazonLunaUbisoftPlus())
    # game_sources_agg.game_sources.append(AmazonLunaPrimeGaming())
    # game_sources_agg.game_sources.append(AmazonLunaJackbox())
    # game_sources_agg.game_sources.append(PsPlus())

    game_sources_agg.load()

    df = game_sources_agg.build_games_data_frame()

    s3_client = S3Client(config.get("AMAZON", "aaki"), config.get("AMAZON", "asak"))
    s3_client.upload_df(df)


if __name__ == "__main__":
    main()
