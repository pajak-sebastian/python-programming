import subprocess
import time
import argparse

def run_system_check(host):
    print(f"--- Starting diagnostic for host: {host} ---")
    
    # Use performance counter for high-precision timing
    start_time = time.perf_counter()
    
    try:
        # Run the system command as a subprocess
        # args: list of command parts to prevent command injection
        # capture_output: redirect stdout and stderr to the Result object
        # text: return output as string instead of bytes
        # check: raise CalledProcessError if the command fails (non-zero exit code)
        result = subprocess.run(
            ["ping", "-n", "4", host], 
            capture_output=True, 
            text=True, 
            check=True
        )
        
        # Access the standard output from the completed process
        print("Command Output:")
        print(result.stdout)
        
    except subprocess.CalledProcessError as e:
        # Handle cases where the command returns a non-zero exit status
        print(f"Critical error during execution: {e.stderr}")
    except FileNotFoundError:
        # Handle cases where the executable (e.g., 'ping') is not found
        print("Error: The 'ping' command was not found in the system PATH.")
    
    end_time = time.perf_counter()
    # Calculate and format the elapsed time
    print(f"--- Operation finished in: {end_time - start_time:.2f} seconds ---")

if __name__ == "__main__":
    # Initialize the argument parser object
    parser = argparse.ArgumentParser(description="A simple network diagnostic tool.")
    
    # Define a positional argument 'target'
    parser.add_argument("target", help="The IP address or domain to check")
    
    # Parse the arguments from the command line (sys.argv)
    args = parser.parse_args()
    
    # Pass the parsed argument to the function
    run_system_check(args.target)