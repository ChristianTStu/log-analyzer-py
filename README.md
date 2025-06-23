# 🛡️ Log Analyzer (Python)

A modular command-line tool for analyzing system and access logs to detect suspicious behavior, such as brute-force login attempts and network anomalies.

Built to support cybersecurity learning and practical detection logic through Python.

---

## ✅ Features

- Detects and classifies **failed login attempts**
- Flags IPs with **excessive authentication failures**
- Differentiates between:
  - `[Suspicious]` – likely brute-force or bot activity
  - `[Normal]` – borderline behavior
  - `[Benign]` – likely human error (e.g., password typos)
- Includes synthetic log generator that simulates:
  - Normal traffic
  - Brute-force attacks
  - Legitimate user login mistakes
  - Malformed lines and log noise
 
---

## 📁 File Structure
```
log-analyzer-py/
├── analyzer.py # Main CLI script
├── generate_sample_logs.py # Synthetic log generator (10K+ lines)
├── aggregated_synthetic_access_data.log
│
├── detection_categories/
│ ├── authentication_attempts/
│ │ └── detect_failed_logins.py
│ └── network_anomalies/
│ └── excessive_connections.py
├── README.md # Project documentation
├── requirements.txt # Python dependencies (currently minimal)
└── .gitignore # Ignore venvs, cache files, etc.
```
---

## 🚀 Usage

Run the analyzer script using Python:

```
1. Generate the synthetic log file
- python generate_sample_logs.py

2. Run the Log Analyzer 
- python analyzer.py
```
---

## ⚙️ Detection Thresholds

By default, the failed login detector uses a threshold of 3 failed attempts per IP.

| Count   | Classification                        |
|---------|----------------------------------------|
| `< 3`   | `[Benign]` – likely human error        |
| `== 3`  | `[Normal]` – borderline                |
| `> 3`   | `[Suspicious]` – needs investigation   |

---

## 🧪 Sample Output

```
[Suspicious] Log report, 198.51.100.42 had 104 failed login attempts
[Normal] Log report, 192.168.1.39 had 3 failed login attempts
[Benign] Log report, 192.168.1.22 had 2 failed attempts (likely user error)
```

---

## 📌 Next Steps

- Add CLI argument support (argparse) to accept file paths, thresholds, and labels from the terminal
- Add support for exporting results to a .csv or .json file
- Improve detection rules (e.g., support for different types of suspicious activity)
- Add unit tests for detection logic
- End Goal: Create a simple CLI or dashboard interface

