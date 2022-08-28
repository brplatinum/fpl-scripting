import asyncio
import aiohttp
import sys
import argparse
from fpl import FPL


# Need to set system environment variables FPL_EMAIL and FPL
async def main():
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        await fpl.login()
        players = await fpl.get_players()
        players = list(filter(filter_price_and_position, players))

    for player in players:
        print(f"{player.first_name} {player.second_name} - {player.now_cost / 10}\n")


def filter_price_and_position(player):
    if player.element_type == position and player.now_cost <= max_price:
        return True

    return False


def position_number(pos):
    match pos:
        case "gkp":
            return 1
        case "def":
            return 2
        case "mid":
            return 3
        case "fwd":
            return 4


parser = argparse.ArgumentParser()

parser.add_argument('--price', help='Max price of the player')
parser.add_argument('--pos', help='Which position the player should be')

args = parser.parse_args()
max_price = int(float(args.price) * 10)
position = position_number(args.pos.lower())

print(max_price)
print(position)

asyncio.run(main())
