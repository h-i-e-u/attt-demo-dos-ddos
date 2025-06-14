# 🛡️ DoS & DDoS Simulation

> **⚠️ For educational and research purposes only.**  
> Use responsibly. Do not deploy on or target any unauthorized networks or systems.

---

## 📖 About

This project demonstrates basic implementations of **Denial of Service (DoS)** and **Distributed Denial of Service (DDoS)** attacks using Dockerized environments.

It's designed for **learning, testing, and research** on private/local networks or lab setups.

---

## 🚀 Quick Start

### 📥 Step 1: Clone the Repository

```bash
git clone https://github.com/h-i-e-u/attt-demo-dos-ddos.git
cd attt-demo-dos-ddos
```

### 🛠️ Step 2: Build Docker Images
**remember to start docker engine**
run build-all.ps1 in attt-demo-dos-ddos
```bash
.\build-all.ps1
```
### 🧪 Step 3: Run & Test
🔥 **Create network for safe testing**
```bash
docker network create ddos-demo-net
```
🟢 **Run the Victim Server with limit cpu and memory (--cpu, --memory flag)**
I run with 10% of 1 core and 256m memory
```bash
docker run --rm -d --name server --network ddos-demo-net --cpus="0.1" --memory="256m" -p 5000:5000 ddos-server
```

🔥 **Run the Attacker**
```bash
docker run -it --rm --network ddos-demo-net --name attacker ddos-attacker
```
🤖 **Run the Botnet (Multiple Instances for DDoS)**
change the (--name) flag to spin more botnet bot, bot2, bot3, etc... 
```bash
docker run -it --rm --network ddos-demo-net --name bot ddos-botnet
```
```bash
docker run -it --rm --network ddos-demo-net --name bot2 ddos-botnet
```
---
🌐 **Test DoS**
run the python code to attack http flood 50 thread and see the result
in attacker container 
```bash
python3 dos_sim.py
```

🌐 **Test DDoS**
run trojan in each botnet
```bash
python3 botnet2.py
```
then run in attacker
if spin 1 bot 
```bash
python3 attacker.py -b bot 
```
if multi bot [bot, bot2, bot3, ect]
```bash
python3 attacker.py -b bot bot2 bot3 etc 
```
**Note:** flag -b is the bot name in previous docker container spin up (--name)
*use name instead of ip for convenient*

### 🧹 Step 4: Clean Up
We have flag *--rm* when spin up container so just need to `exit` the attacker and bot
We also need to stop server
```bash
docker stop server
``` 
---
## 🎬 Guide Video
*coming soon...*
---
## 📂 Project Structure
```code
.
├── attacker/        # DoS attack logic
├── botnet/          # Botnet logic for DDoS
├── server/          # Simple HTTP server as victim
├── build-all.sh     # Shell script to build all Docker images
└── README.md        # You're here

```

```code
Let me know if you want to include usage examples, architecture diagrams, or badges (like Docker or GitHub stars) at the top!
```