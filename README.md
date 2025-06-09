
## Fáze 3 – Realtime ceny přes multicall a sledování mempoolu

- `multicall_utils.py`: logika pro čtení rezerv z více DEXů
- `mempool_listener.py`: připojení k Alchemy WebSocket a sledování pending transakcí
- `main.py`: volá oba moduly
