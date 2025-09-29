# Data-Structures-Counting

This repository contains scripts and tools for analyzing authentication logs, detecting brute force attacks, and extracting useful information from log files. The main focus is on using efficient data structures and algorithms for counting and detection tasks.

## Contents

- `ParseAuthAndBruteDetect.py`: Parses authentication logs and detects brute force attacks.
- `ExtractIPs.py`: Extracts IP addresses from log files.
- `ParseAuth.log`: Example log file for parsing.
- `sample_auth_small.txt`: Sample authentication log for testing.
- `failed_counts.txt`: Output file containing counts of failed authentication attempts.
- `bruteForceDetect.log`: Log file for detected brute force attempts.
- `timesSaved.log`: Log file for saved timestamps.
- `top_attackers.png`: Visualization of top attackers.

## Usage

1. **Parse Authentication Logs and Detect Brute Force Attacks**
   
	Run the main script:
	```bash
	python3 ParseAuthAndBruteDetect.py
	```
	This will process the authentication log and output results to the relevant files.

2. **Extract IP Addresses**
   
	Run the extraction script:
	```bash
	python3 ExtractIPs.py
	```
	This will extract IP addresses from the log files.

## Requirements

- Python 3.x
- Standard Python libraries (no external dependencies required)

## Visualization

- The `top_attackers.png` file provides a visualization of the most frequent attackers based on the parsed logs.

## License

This project is licensed under the MIT License.

## Author

Marwan-verse