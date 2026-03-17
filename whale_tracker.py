import requests
import time

WALLET = "2RH6rUTPBJ9rUDPpuV9b8z1YL56k1tYU6Uk5ZoaEFFSK"

def get_transactions():
    url = f"https://public-api.solscan.io/account/transactions?account={WALLET}&limit=10"
    headers = {"accept": "application/json"}
    
    try:
        response = requests.get(url, headers=headers)
        return response.json()
    except:
        return []

last_tx = None

print("🐋 بدأ تتبع المحفظة...")

while True:
    txs = get_transactions()

    if txs:
        latest = txs[0]["txHash"]

        if latest != last_tx:
            print("\n🚨 حركة جديدة!")
            print("TX:", latest)

            for tx in txs[:3]:
                print("➡️ Hash:", tx["txHash"])
                print("⏱ وقت:", tx["blockTime"])
                print("-" * 30)

            last_tx = latest

    time.sleep(30)  # كل 30 ثانية
