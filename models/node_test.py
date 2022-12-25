from solana.rpc.api import Client
import asyncio
from solana.rpc.async_api import AsyncClient


async def main():
    async with AsyncClient("https://api.devnet.solana.com") as client:
        res = await client.is_connected()
    print(f"Connected: {res}")  # True
    
    # async with AsyncClient("https://api.devnet.solana.com") as client:
    #     # Subscribe to new transactions
    #     async for transaction in client.transactions():
    #         print(f'New transaction: {transaction.transaction.message.instructions[0].program_id}')


asyncio.run(main())

