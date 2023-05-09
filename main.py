import sys

def main():
    # Get command line arguments
    arguments = sys.argv[1:]

    # Check if arguments are provided
    if len(arguments) == 0:
        print("No arguments provided")
    else:
        print("Arguments:")
        for arg in arguments:
            print(arg)

if __name__ == "__main__":
    main()