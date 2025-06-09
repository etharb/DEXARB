import csv
import os
from datetime import datetime

def log_result(result, filename='logs/arbitrage_results.csv'):
    os.makedirs('logs', exist_ok=True)
    file_exists = os.path.isfile(filename)
    with open(filename, 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=result.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(result)
