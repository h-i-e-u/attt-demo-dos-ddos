import sys

def sum_args(args):
    total = 0
    for arg in args:
        try:
            total += float(arg)
        except ValueError:
            print(f"Warning: '{arg}' is not a number and will be ignored.")
    return total

def main():
    print("Enter numbers separated by space. Type 'stop' to exit.")
    
    # First sum from command line arguments (excluding script name)
    if len(sys.argv) > 1:
        total = sum_args(sys.argv[1:])
        print(f"Sum of command-line arguments: {total}")
    else:
        total = 0

    while True:
        user_input = input("Enter numbers (or 'stop'): ").strip()
        if user_input.lower() == "stop":
            print("Stopping. Goodbye!")
            break
        args = user_input.split()
        total += sum_args(args)
        print(f"Current total: {total}")

if __name__ == "__main__":
    main()
