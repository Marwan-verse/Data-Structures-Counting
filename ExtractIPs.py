import time
import re
from collections import defaultdict

uniqueIPs = list()
counter = 0

LOGFILE = 'sample_auth_small.txt'

def ip_parse(line):
    match = re.search(r'(?:\d{1,3}\.){3}\d{1,3}', line)
    if match:
        uniqueIPs.append(match.group(0))
        return match.group(0)
    return None

print("Unique IPs found:", len(uniqueIPs))

counts = defaultdict(int)           # Create a dictionary to keep track of IPs


def main():
    counts = defaultdict(int)
            
    with open(LOGFILE, 'r') as f:
        for line in f:
            counter =+ 1
            if 'Failed password' in line or 'Invalid user' in line:
                ip = ip_parse(line)
                if ip:
                    counts[ip] += 1

    print("Lines read:", counts)

    # Sort IPs by count descending
    top_attackers = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:5]
    print("Top 5 attacker IPs:")
    for i, (ip, count) in enumerate(top_attackers, 1):
        print(f"{i}. {ip} — {count}")

start = time.time()
# run counting
end = time.time()
print("Elapsed:", end-start, "seconds")

if __name__ == "__main__":
    main()

