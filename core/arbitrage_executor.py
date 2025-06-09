from web3 import Web3
import os
from dotenv import load_dotenv

load_dotenv()
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
ALCHEMY_RPC_URL = os.getenv("ALCHEMY_RPC_URL")

w3 = Web3(Web3.HTTPProvider(ALCHEMY_RPC_URL))
account = w3.eth.account.from_key(PRIVATE_KEY)

def execute_arbitrage(contract_address, dex1, dex2, path_forward, path_backward, amount_in, min_profit):
    abi = [...]  # Zkráceno, doporučeno načíst externě
    contract = w3.eth.contract(address=contract_address, abi=abi)

    txn = contract.functions.executeArbitrage(
        dex1, dex2, path_forward, path_backward, amount_in, min_profit
    ).build_transaction({
        "from": account.address,
        "nonce": w3.eth.get_transaction_count(account.address),
        "gas": 3000000,
        "gasPrice": w3.eth.gas_price,
    })

    signed_txn = account.sign_transaction(txn)
    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    print("Arbitrážní tx odeslána:", tx_hash.hex())
