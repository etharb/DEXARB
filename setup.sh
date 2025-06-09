#!/bin/bash

unzip -o project.zip -d .
git add .
git commit -m "Fáze 1: Subgraph páry (Uniswap, Quickswap, Sushiswap, Kyber, 0x)"
git push origin main
echo "✅ Hotovo."
