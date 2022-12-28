# https://docs.alchemy.com/reference/getnftsales

import requests
import json

from conf.conf import logging


API_key = "vYHU2nVXBMrIHlByeFOQWubnRQcl_v_3"
address_bayc = "0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D"


def get_floor_price(API: str, address: str) -> dict:
    logging.info("Sending request to API")
    url = f"https://eth-mainnet.g.alchemy.com/nft/v2/{API}/getFloorPrice?contractAddress={address}"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    
    logging.info("Creating a dictionary")
    prices = {"opensea": data['openSea']['floorPrice'],
              "looksrare": data['looksRare']['floorPrice']}

    return prices


def get_activity_collection(API: str, address: str, limit: int) -> json:
    logging.info("Sending request to API")
    url = f"https://eth-mainnet.g.alchemy.com/nft/v2/{API}/getNFTSales?fromBlock=0&toBlock=latest&order=desc&contractAddress={address}&limit={limit}"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    
    logging.info("Creating a dictionary")
    activity = {"marketplace": data['nftSales'][0]['marketplace'],
                "tokenId": data['nftSales'][0]['tokenId'],
                "price": int(data['nftSales'][0]['sellerFee']['amount']) / 10 ** 18}
    
    return activity


def get_activity_token(API: str, address: str, limit: int, tokenId: int) -> json:
    logging.info("Sending request to API")
    url = f"https://eth-mainnet.g.alchemy.com/nft/v2/{API}/getNFTSales?fromBlock=0&toBlock=latest&order=desc&contractAddress={address}&limit={limit}&tokenId={tokenId}"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    
    logging.info("Creating a dictionary")
    activity = {"marketplace": data['nftSales'][0]['marketplace'],
                 "tokenId": data['nftSales'][0]['tokenId'],
                 "sellerFee": int(data['nftSales'][0]['sellerFee']['amount']) / 10 ** 18,
                 "protocolFee": int(data['nftSales'][0]['protocolFee']['amount']) / 10 ** 18,
                 "royaltyFee": int(data['nftSales'][0]['royaltyFee']['amount']) / 10 ** 18,
                 "payed": (int(data['nftSales'][0]['sellerFee']['amount']) + int(data['nftSales'][0]['protocolFee']['amount']) + int(data['nftSales'][0]['royaltyFee']['amount'])) / 10 ** 18}
    
    return activity


def get_rarity(API: str, address: str, tokenId: int) -> json:
    logging.info("Sending request to API")
    url = f"https://eth-mainnet.g.alchemy.com/nft/v2/{API}/computeRarity?contractAddress={address}&tokenId={tokenId}"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    
    logging.info("Calculating rarity")
    result = 1
    for rarity in data:
        result *= rarity['prevalence']

    return result

#print(get_rarity(API_key, address_bayc, 5117))

# if __name__ == "__main__":
#     print("tests:")
#     print(get_floor_price(API_key, address_bayc))
#     print(get_activity_collection(API_key, address_bayc, 1))

dictionaries = [{'value': 'Leather Jacket', 'trait_type': 'Clothes', 'prevalence': 0.0206}, {'value': 'Sad', 'trait_type': 'Eyes', 'prevalence': 0.0551}]

result = 1
for d in dictionaries:
    result *= d['prevalence']

print(result)
