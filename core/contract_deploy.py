from web3 import Web3
from solcx import compile_source
import os
from dotenv import load_dotenv

load_dotenv()
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
ALCHEMY_RPC_URL = os.getenv("ALCHEMY_RPC_URL")

w3 = Web3(Web3.HTTPProvider(ALCHEMY_RPC_URL))
account = w3.eth.account.from_key(PRIVATE_KEY)

with open("contracts/ArbitrageRouter.sol", "r") as file:
    source = file.read()

compiled_sol = compile_source(source)
contract_id, contract_interface = compiled_sol.popitem()

Arbitrage = w3.eth.contract(abi=contract_interface["abi"], bytecode=contract_interface["bin"])
construct_txn = Arbitrage.constructor().build_transaction({
    "from": account.address,
    "nonce": w3.eth.get_transaction_count(account.address),
    "gas": 3000000,
    "gasPrice": w3.eth.gas_price,
})

signed = account.sign_transaction(construct_txn)
tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
print("Deployment tx sent:", tx_hash.hex())
receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print("Contract deployed at:", receipt.contractAddress)
