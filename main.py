import json
import argparse
from core.logger import log_result

parser = argparse.ArgumentParser()
parser.add_argument('--simulate', action='store_true', help='Spustí režim simulace')
parser.add_argument('--no-execute', action='store_true', help='Zakáže skutečné obchodování')
args = parser.parse_args()

with open('config/settings.json') as f:
    settings = json.load(f)

simulate = args.simulate or settings.get("simulate", True)
no_execute = args.no_execute

print("✅ Nastavení:")
print(f"Simulace: {simulate}")
print(f"Reálné obchodování povoleno: {not no_execute}")

# Mock výsledek arbitráže
result = {
    "timestamp": datetime.utcnow().isoformat(),
    "dex1": "Uniswap",
    "dex2": "Quickswap",
    "profit_usd": 14.2,
    "gas_used": 280000,
    "tx_hash": "0x1234...abcd" if not simulate else "SIMULATED"
}

log_result(result)
print("📊 Výsledek zaznamenán.")
