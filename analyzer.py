import os
import re

easy_log = open("sample_logs/auth_easy.log", "r")
medium_log = open("sample_logs/auth_medium.log", "r")
hard_log = open("sample_logs/auth_hard.log", "r")

easy_log_list = []
failed_ip_counts = {}


for line in easy_log:
    if "Failed password" in line:
      easy_log_list.append(line)  

for line in easy_log_list:
    ip_matches = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", line)
    if ip_matches:
        ip = ip_matches[0]
        if ip in failed_ip_counts:
            failed_ip_counts[ip] += 1
        else:
            failed_ip_counts[ip] = 1

print(failed_ip_counts)
    

        # do something with ip
