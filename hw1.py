import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for ball in range(1, 6):
        await asyncio.sleep(1/power)
        print(f'Силач {name} поднял {ball}')
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    strongman1 = start_strongman('Pasha', 3)
    strongman2 = start_strongman('Denis', 4)
    strongman3 = start_strongman('Apollon', 5)
    await asyncio.gather(strongman1, strongman2, strongman3)

asyncio.run(start_tournament())
