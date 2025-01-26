# pyevm < https://t.me/airdrophuntersid >
# Copyright (C) 2025-present @airdrophuntersid
#
# This file is a part of < https://github.com/airdrophuntersid/pyevm/ >
# Please read the GNU General Public License v3.0
# < https://github.com/airdophuntersid/pyevm/blob/main/LICENSE >

from os import getenv as gets
from dotenv import find_dotenv, load_dotenv
from typing import Union, Optional
from sys import exit

load_dotenv(
    find_dotenv(
        "config.env"
    )
)

MAX_SEND: Union[int, float] = gets("MAX_SEND", "")
MIN_SEND: Union[int, float] = gets("MIN_SEND", "")
PRIVATE_KEY: Union[str] = gets("PRIVATE_KEY", "").split(",")
RPC_URL: Optional[str] = gets("RPC_URL", "")
