# https://docs.alchemy.com/reference/

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


def get_sales_collection(API: str, address: str, limit: int) -> json:
    logging.info("Sending request to API")    
    url = f"https://eth-mainnet.g.alchemy.com/nft/v3/{API}/getNFTSales?fromBlock=0&toBlock=latest&order=desc&marketplace=seaport&contractAddress={address}&limit={limit}"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    
    logging.info("Creating a dictionary")
    # Use this to define price as all the money buyer paid to get NFT
    # "price": (int(sale["sellerFee"]["amount"]) + int(sale["protocolFee"]["amount"]) + (0 if sale["royaltyFee"]["amount"] is None else int(sale["royaltyFee"]["amount"]))) / 10 ** 18} for sale in data["nftSales"]]
    
    activity = [{"tokenId": sale["tokenId"],
                 "marketplace": sale["marketplace"],
                 "price": 0 if sale["sellerFee"]["amount"] is None else int(sale["sellerFee"]["amount"]) / 10 ** 18} for sale in data["nftSales"]]

    return activity


def get_sales_token(API: str, address: str, limit: int, tokenId: int) -> json:
    logging.info("Sending request to API")
    url = f"https://eth-mainnet.g.alchemy.com/nft/v2/{API}/getNFTSales?fromBlock=0&toBlock=latest&order=desc&contractAddress={address}&limit={limit}&tokenId={tokenId}"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    
    logging.info("Creating a dictionary")
    # Use this to calculate all the money buyer payed
    # activity = [{"tokenId": sale["tokenId"],
    #              "marketplace": sale["marketplace"],
    #              "sellerFee": int(sale["sellerFee"]["amount"]) / 10 ** 18,
    #              "protocolFee": int(sale["protocolFee"]["amount"]) / 10 ** 18,
    #              "royaltyFee": int(sale["royaltyFee"]["amount"]) / 10 ** 18,
    #              "payed": (int(sale["sellerFee"]["amount"]) + int(sale["protocolFee"]["amount"]) + int(sale["royaltyFee"]["amount"])) / 10 ** 18} for sale in data["nftSales"]]
    
    activity = [{"tokenId": sale["tokenId"],
                 "marketplace": sale["marketplace"],
                 "sellerFee": int(sale["sellerFee"]["amount"]) / 10 ** 18} for sale in data["nftSales"]]
    
    return activity


def get_attributes(API: str, address: str, tokenId: int) -> json:
    logging.info("Sending request to API")
    url = f"https://eth-mainnet.g.alchemy.com/nft/v2/{API}/computeRarity?contractAddress={address}&tokenId={tokenId}"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)

    return data


def get_attributes_collection(API: str, address: str) -> json:
    logging.info("Sending request to API")
    url = f"https://eth-mainnet.g.alchemy.com/nft/v2/{API}/summarizeNFTAttributes?contractAddress={address}"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    
    return data['summary']


def get_rarity(API: str, address: str, tokenId: int) -> json:
    data = get_attributes(API=API, address=address, tokenId=tokenId)
    
    logging.info("Calculating rarity")
    result = 1
    for rarity in data:
        result *= rarity["prevalence"]
        
    return result


#print(get_activity_collection(API=API_key, address=address_bayc, limit=10))
#print(get_collection_attributes(API=API_key, address=address_bayc))
#print(get_sales_collection(API=API_key, address=address_bayc, limit=1))
print(get_attributes(API=API_key, address=address_bayc, tokenId=8230))
#print(get_attributes_collection(API=API_key, address=address_bayc))
#print(get_rarity(API=API_key, address=address_bayc, tokenId=8230))