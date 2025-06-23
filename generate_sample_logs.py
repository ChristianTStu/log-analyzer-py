import random
from datetime import datetime, timedelta

LOG_FILE = "aggregated_synthetic_access_data.log"
TOTAL_LINES = 10000
NORMAL_IPS = [f"192.168.1.{i}" for i in range(1, 50)]
MALICIOUS_IPS = ["10.0.0.200", "198.51.100.42", "172.16.0.1"]
ENDPOINTS = ["/home", "/about", "/contact", "/products", "/cart", "/checkout", "/login"]
METHODS = ["GET", "POST"]
USERNAMES = ["root", "admin", "user", "test"]

# Reserve 5 known-legit IPs and exclude them from random pools
LEGITIMATE_IPS = random.sample(NORMAL_IPS, 5)
RESTRICTED_NORMAL_IPS = [ip for ip in NORMAL_IPS if ip not in LEGITIMATE_IPS]

def random_timestamp(start_time, seconds_offset):
    return (start_time + timedelta(seconds=seconds_offset)).strftime("%Y-%m-%d %H:%M:%S")

def write_log(file, timestamp, ip, message):
    file.write(f"{timestamp} IP:{ip} - {message}\n")

def generate():
    with open(LOG_FILE, "w") as f:
        start_time = datetime(2023, 10, 15, 10, 0, 0)
        seconds_offset = 0

        for i in range(TOTAL_LINES):
            # Normal web traffic
            if i % 5 != 0:
                ip = random.choice(NORMAL_IPS)
                method = random.choice(METHODS)
                endpoint = random.choice(ENDPOINTS)
                msg = f"{method} {endpoint}"
                write_log(f, random_timestamp(start_time, seconds_offset), ip, msg)

            # Excessive connection burst from malicious IP
            elif i % 50 == 0:
                for _ in range(10):
                    ip = "192.168.1.101"
                    msg = f"GET /products"
                    write_log(f, random_timestamp(start_time, seconds_offset), ip, msg)
                    seconds_offset += 1

            # Failed SSH password attempts from attackers and non-legit users
            elif i % 75 == 0:
                if random.random() < 0.6:
                    # Brute-force attacker
                    ip = random.choice(["10.0.0.200", "198.51.100.42"])
                    attempts = random.randint(3, 6)
                else:
                    # Non-legit normal IP (excluding the reserved 5)
                    ip = random.choice(RESTRICTED_NORMAL_IPS)
                    attempts = random.choice([1, 2])

                for _ in range(attempts):
                    username = random.choice(USERNAMES)
                    msg = f"Failed password for {username} from {ip} port 22 ssh2"
                    write_log(f, random_timestamp(start_time, seconds_offset), ip, msg)
                    seconds_offset += random.randint(1, 2)

            # Unauthorized access attempts
            elif i % 120 == 0:
                ip = "172.16.0.1"
                msg = "Unauthorized access attempt to /admin"
                write_log(f, random_timestamp(start_time, seconds_offset), ip, msg)

            # Malformed line
            elif i % 333 == 0:
                f.write("MALFORMED LINE NO TIMESTAMP OR STRUCTURE\n")

            seconds_offset += random.randint(1, 3)

        # Inject known legitimate login failures (1–2 per IP)
        for ip in LEGITIMATE_IPS:
            attempts = random.choice([1, 2])
            for _ in range(attempts):
                username = random.choice(USERNAMES)
                msg = f"Failed password for {username} from {ip} port 22 ssh2"
                write_log(f, random_timestamp(start_time, seconds_offset), ip, msg)
                seconds_offset += random.randint(1, 3)

if __name__ == "__main__":
    generate()
