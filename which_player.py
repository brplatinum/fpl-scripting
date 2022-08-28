import asyncio
import aiohttp
from fpl import FPL

# Need to set system environment variables FPL_EMAIL and FPL
async def main():
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        await fpl.login()
        user = await fpl.get_user()
        my_team = await user.get_team()

    print(my_team)

print(os.environ["FPL_EMAIL"])
print(os.environ["FPL_PASSWORD"])
asyncio.run(main())
