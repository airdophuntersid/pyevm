# pyevm < https://t.me/airdrophuntersid >
# Copyright (C) 2025-present @airdrophuntersid
#
# This file is a part of < https://github.com/airdrophuntersid/pyevm/ >
# Please read the GNU General Public License v3.0
# < https://github.com/airdophuntersid/pyevm/blob/main/LICENSE >

import os
import sys
os.system("clear")
import json
import random
import secrets
import time
from web3 import Web3, HTTPProvider
from config import MAX_SEND, MIN_SEND, PRIVATE_KEY, RPC_URL


ASCII = """

  /$$$$$$  /$$                 /$$
 /$$__  $$|__/                | $$
| $$  \ $$ /$$  /$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$   /$$$$$$
| $$$$$$$$| $$ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$
| $$__  $$| $$| $$  \__/| $$  | $$| $$  \__/| $$  \ $$| $$  \ $$
| $$  | $$| $$| $$      | $$  | $$| $$      | $$  | $$| $$  | $$
| $$  | $$| $$| $$      |  $$$$$$$| $$      |  $$$$$$/| $$$$$$$/
|__/  |__/|__/|__/       \_______/|__/       \______/ | $$____/
                                                      | $$
                                                      | $$
                                                      |__/

                /$$   /$$                       /$$
               | $$  | $$                      | $$
               | $$  | $$ /$$   /$$ /$$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$   /$$$$$$$
               | $$$$$$$$| $$  | $$| $$__  $$|_  $$_/   /$$__  $$ /$$__  $$ /$$_____/
               | $$__  $$| $$  | $$| $$  \ $$  | $$    | $$$$$$$$| $$  \__/|  $$$$$$
               | $$  | $$| $$  | $$| $$  | $$  | $$ /$$| $$_____/| $$       \____  $$
               | $$  | $$|  $$$$$$/| $$  | $$  |  $$$$/|  $$$$$$$| $$       /$$$$$$$/
               |__/  |__/ \______/ |__/  |__/   \___/   \_______/|__/      |_______/

                           Copyright (C) 2025-present @airdrophuntersid
"""

print(ASCII)
print(f"")
print(f"Automatic Transactions by @airdrophuntersid")
print(f"")
print(f"")

WALLET = Web3(Web3.HTTPProvider(str(RPC_URL)))
CHAIN_ID = WALLET.eth.chain_id

if WALLET.is_connected() == True:
    print("Wallet has been Connected ✅\n")
else:
    print("Error connecting to your wallet.#\nPlease try again...\nExiting...")
    sys.exit(0)
