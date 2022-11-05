from dataclasses import dataclass, field
from enum import StrEnum


class GamePlatform(StrEnum):
    XBOX_CLOUD = "XBOX Cloud"
    XBOX_CONSOLE = "XBOX Console"
    XBOX_PC = "XBOX PC"

    LUNA_PLUS = "Luna+"
    LUNA_FAMILY = "Luna Family"
    LUNA_RETRO = "Luna Retro"
    LUNA_UBISOFT_PLUS = "Luna Ubisoft+"
    LUNA_PRIME_GAMING = "Luna Prime Gaming"
    LUNA_JACKBOX = "Luna Jackbox"

    PSNOW_PREMIUM = "PSNow Premium"
    PSNOW_EXTRA = "PSNow Extra"

    NVIDIA = "Nvidia"

    BOOSTEROID = "Boosteroid"


@dataclass
class Game:
    title: str
    platform: GamePlatform
    source_url: str
    sub_title: str = field(default=None)
    developer: str = field(default=None)
    thumbnail_image_url: str = field(default=None)
