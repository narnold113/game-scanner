from dataclasses import dataclass, field
from enum import StrEnum
from uuid import uuid4


class GamePlatform(StrEnum):
    XBOX_CLOUD = "XBOX Cloud"
    XBOX_CONSOLE = "XBOX Console"
    XBOX_PC = "XBOX PC"

    AMAZON_LUNA_PLUS = "Amazon Luna+"
    AMAZON_LUNA_FAMILY = "Amazon Luna Family"
    AMAZON_LUNA_RETRO = "Amazon Luna Retro"
    AMAZON_LUNA_UBISOFT_PLUS = "Amazon Luna Ubisoft+"
    AMAZON_LUNA_PRIME_GAMING = "Amazon Luna Prime Gaming"
    AMAZON_LUNA_JACKBOX = "Amazon Luna Jackbox"

    PSNOW_PREMIUM = "PSNow Premium"
    PSNOW_EXTRA = "PSNow Extra"
    PS_PLUS = "PS Plus"

    NVIDIA_GFN = "Nvidia GeForce Now"

    BOOSTEROID = "Boosteroid"


@dataclass
class Game:
    title: str
    platform: GamePlatform
    source_url: str
    sub_title: str = field(default=None)
    developer: str = field(default=None)
    thumbnail_image_url: str = field(default=None)
