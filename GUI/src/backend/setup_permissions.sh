#!/bin/bash

# Define paths
SCRIPT_DIR="/home/neeraj/Chanakya/Cyber Swipe/src/backend"
PYTHON_SCRIPT="$SCRIPT_DIR/machine_health.py"
YARA_RULES="$SCRIPT_DIR/malware_rules.yar"
SCAN_DIR="/home/neeraj/scan_directory"

# Create scan directory if it doesn't exist
mkdir -p "$SCAN_DIR"

# Set permissions for the Python script
chmod 755 "$PYTHON_SCRIPT"

# Set permissions for the YARA rules file
chmod 644 "$YARA_RULES"

# Set permissions for the scan directory
chmod 755 "$SCAN_DIR"

# Set permissions for the script directory
chmod 755 "$SCRIPT_DIR"

echo "Permissions set successfully."
echo "Python script: $PYTHON_SCRIPT"
echo "YARA rules: $YARA_RULES"
echo "Scan directory: $SCAN_DIR"

# Optionally, create some test files in the scan directory
touch "$SCAN_DIR/test_file1.txt"
touch "$SCAN_DIR/test_file2.txt"
echo "Test files created in scan directory."

echo "You can now run your Python script to scan the directory:"
echo "python3 $PYTHON_SCRIPT"