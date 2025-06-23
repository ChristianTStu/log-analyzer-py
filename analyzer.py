import re

easy_log = open("sample_logs/auth_easy.log", "r")
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
    if count > 3:
        print(f"[!] {ip} had {count} failed login attempts")