# Fáze 3 – Integrace multicallu a mempoolu

from core.multicall_utils import fetch_pool_reserves
from core.mempool_listener import listen_to_pending_transactions

print("Spouštím realtime monitoring")
fetch_pool_reserves()
listen_to_pending_transactions()
