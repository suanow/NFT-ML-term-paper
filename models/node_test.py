# from solana.rpc.api import Client
# import asyncio
# from solana.rpc.async_api import AsyncClient


# node = "https://light-palpable-pond.solana-devnet.discover.quiknode.pro/ac06aca4979e78424f1c00799d9c83283bf05894/"

# async def main():
#     async with AsyncClient(node) as client:
#         res = await client.is_connected()
#     print(f"Connected: {res}")  # True
    
#     async with AsyncClient(node) as client:
#         # Subscribe to new transactions
#         async for transaction in client.transactions():
#             print(f'New transaction: {transaction.transaction.message.instructions[0].program_id}')


# asyncio.run(main())

# from solana.rpc.api import Client
# solana_client = Client("https://light-palpable-pond.solana-devnet.discover.quiknode.pro/ac06aca4979e78424f1c00799d9c83283bf05894/")
# print(solana_client.get_inflation_rate())

from solana.rpc.api import Client
solana_client = Client("https://light-palpable-pond.solana-devnet.discover.quiknode.pro/ac06aca4979e78424f1c00799d9c83283bf05894/")
print(solana_client.get_cluster_nodes())