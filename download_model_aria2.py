import subprocess
import sys

def main():
    cmd = [
        "aria2c",
        "-i", "aria2_inputs.txt",
        "-j", "4",
        "-x", "16",
        "-s", "16",
        "--summary-interval=10",
        "--continue=true",
        "--file-allocation=none"
    ]
    print("Starting download of Bernini-Diffusers files using aria2c...")
    
    try:
        # Run aria2c and forward stdout/stderr
        process = subprocess.Popen(cmd, stdout=sys.stdout, stderr=sys.stderr)
        process.wait()
        if process.returncode == 0:
            print("Model download completed successfully!")
        else:
            print(f"aria2c exited with error code {process.returncode}")
            sys.exit(process.returncode)
    except Exception as e:
        print(f"Error executing aria2c: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
