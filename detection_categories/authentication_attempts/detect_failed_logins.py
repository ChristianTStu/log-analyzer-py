import re

def detect_failed_logins(path, threshold=3):
    easy_log = open(path, "r")
    failed_ip_counts = {}
    for line in easy_log:
        if "Failed password" in line:
            ip_matches = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", line)
            if ip_matches:
                ip = ip_matches[0]
                if ip in failed_ip_counts:
                    failed_ip_counts[ip] += 1
                else:
                    failed_ip_counts[ip] = 1
    for ip, count in failed_ip_counts.items():
        if count > threshold:
            print(f"[Suspicious] Log report, {ip} had {count} failed login attempts")
        else:
            print(f"[Normal] Log report, {ip} had {count} failed attempts.")

