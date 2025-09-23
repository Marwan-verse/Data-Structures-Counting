import time
import re
import json
from collections import defaultdict

uniqueIPs = list()


LOGFILE = 'sample_auth_small.txt'

def ip_parse(line):
    match = re.search(r'(?:\d{1,3}\.){3}\d{1,3}', line)
    if match:
        uniqueIPs.append(match.group(0))
        return match.group(0)
    return None

counts = defaultdict(int)           # Create a dictionary to keep track of IPs


def main():
    counter = 0  
    counts = defaultdict(int)
         
    with open(LOGFILE, 'r') as f:
        for line in f:
            counter =1 + counter
            if 'Failed password' in line or 'Invalid user' in line:
                ip = ip_parse(line)
                if ip:
                    counts[ip] += 1


    with open('failed_counts.txt', 'w') as f:  
        f.write(json.dumps(counts, indent=2))   


    print("Lines read:", counter)
    print("Unique IPs found:", len(counts))

    # Sort IPs by count descending
    top_attackers = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:5]
    print("Top 5 attacker IPs:")
    for i, (ip, count) in enumerate(top_attackers, 1):
        print(f"{i}. {ip} — {count}")


if __name__ == "__main__":
    main()

start = time.time()
# run counting
end = time.time()
print("Elapsed:", "{:.8f}".format(end-start), "seconds")
with open('timesSaved.log', 'a') as f:  
        f.write("\nElapsed: " + "{:.8f}".format(end-start) + " seconds\n")
