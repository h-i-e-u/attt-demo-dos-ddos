FROM debian:stable-slim

# install tool
RUN apt update && apt install -y \
    hping3 \
    iputils-ping \
    curl \
    python3 \
    python3-pip

#  Python lib (requests)
RUN pip3 install requests --break-system-packages

# Copy file Python to container
COPY ddos_sim.py /app/ddos_sim.py
COPY attacker.py /app/attacker.py

# Set working directory
WORKDIR /app

# defaul bash
CMD ["bash"]
