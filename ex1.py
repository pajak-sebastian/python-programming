import subprocess
import time
import argparse
import csv

def get_arguments():
    """
    Parse CLI arguments
    """
    parser = argparse.ArgumentParser(description="Simple file listing tool")
    parser.add_argument(
        "-p",
        "--path",
        default=r"C:\Users\grove\python-programming",
        help="Path to a dir"
    )

    parser.add_argument(
        "-v",
        "--verbose",
        help="Increase output verbosity",
        action="store_true"
    )
    return parser.parse_args()

def main(target_path):
    """
    Main function. Printing dir content using default or user argument
    """
    print("Initializing time counter...")
    start_time = time.perf_counter()

    try:
        result = subprocess.run(
            ["dir", target_path],
            capture_output=True,
            text=True,
            check=True,
            shell=True
        )

        print(result.stdout)

        print(f"Total characters in listing:{len(result.stdout)}")

    except subprocess.CalledProcessError as e:
        print(f"Critical error during execution: {e.stderr}")

    except FileNotFoundError:
        print(f"Dir not found!")

    end_time = time.perf_counter()

    print(f"Operation finished in {end_time - start_time}")

if __name__ == "__main__":

    args = get_arguments()
    main(args.path)
