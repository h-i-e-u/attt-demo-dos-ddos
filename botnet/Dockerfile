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
COPY botnet.py /app/botnet.py
COPY botnet2.py /app/botnet2.py

# Set working directory
WORKDIR /app

#  bash
CMD ["bash"]
