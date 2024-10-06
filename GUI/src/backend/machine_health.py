import psutil
import os
import time
import yara
import logging
from pathlib import Path

def check_cpu_usage():
    cpu_percent = psutil.cpu_percent(interval=1)
    if cpu_percent > 80:
        print("High CPU usage detected: {}%".format(cpu_percent))
        # Perform further actions like generating alerts, logging, etc.

def check_memory_usage():
    memory_info = psutil.virtual_memory()
    if memory_info.percent > 90:
        print("High memory usage detected: {}%".format(memory_info.percent))
        # Perform further actions like generating alerts, logging, etc.

def check_disk_usage():
    disk_usage = psutil.disk_usage('/')
    if disk_usage.percent > 90:
        print("High disk usage detected: {}%".format(disk_usage.percent))
        # Perform further actions like generating alerts, logging, etc.

def check_malware_signature():
    # Set up logging
    logging.basicConfig(filename='malware_scan.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    # Load YARA rules
    rules_path = Path(__file__).parent / 'malware_rules.yar'
    if not rules_path.exists():
        logging.error(f"YARA rules file not found at {rules_path}")
        return

    try:
        rules = yara.compile(str(rules_path))
        logging.info("YARA rules compiled successfully")

        # Start scanning from root directory
        root_dir = Path('/')
        matches = []

        for path in root_dir.rglob('*'):
            try:
                if path.is_file():
                    file_matches = rules.match(str(path))
                    if file_matches:
                        matches.extend(file_matches)
                        logging.warning(f"Malware signature detected in {path}")
            except PermissionError:
                logging.info(f"Permission denied: Unable to scan {path}")
            except yara.YaraError as e:
                logging.error(f"YARA Error occurred: {e}")
            except yara.YaraSyntaxError as e:
                logging.error(f"YARA Syntax Error occurred: {e}")
            except Exception as e:
                logging.error(f"An unexpected error occurred during malware scan: {e}")

        if matches:
            logging.warning("Malware signatures detected:")
            for match in matches:
                logging.warning(f"  - {match}")
        else:
            logging.info("No malware signatures detected")

    except Exception as e:
        logging.error(f"An unexpected error occurred during malware scan: {e}")

def check_system_health():
    while True:
        check_cpu_usage()
        check_memory_usage()
        check_disk_usage()
        check_malware_signature()
        time.sleep(60)  # Check every 60 seconds

# Start the system health checker
check_system_health()