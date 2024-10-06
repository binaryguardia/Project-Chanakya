import subprocess

def analyze_disk():
    # Example command with The Sleuth Kit for disk analysis
    command = "fls -r /dev/sda1"  # Modify with the correct disk path
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

    if error:
        return f"Error: {error}"
    return output.decode()

if __name__ == "__main__":
    disk_report = analyze_disk()
    print(disk_report)
