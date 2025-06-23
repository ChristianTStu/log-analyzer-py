# Log Analyzer (Python)

A command-line tool to analyze system logs for signs of brute-force and other unauthorized access attempts.

## Features

- Parse Unix-style SSH auth logs
- Detect repeated failed logins from the same IP
- Modular detection logic in `/detections`
- Threshold-based brute-force detection

## File Structure
```
log-analyzer-py/
├── analyzer.py # Entry point script that imports detection logic
├── detections/ # Detection logic modules
│ ├── init.py
│ └── brute_force.py # Contains analyze_log() function
├── sample_logs/ # Test log files for analysis
│ ├── auth_easy.log
│ ├── auth_medium.log
│ └── auth_hard.log
├── README.md # Project documentation
├── requirements.txt # Python dependencies (currently minimal)
└── .gitignore # Ignore venvs, cache files, etc.
```

## 🚀 Usage

Run the analyzer script using Python:

```
python analyzer.py

This will analyze all log files listed and output IP addresses with more than 3 failed login attempts by default.
To change the detection threshold or add custom labels, edit the analyze_log calls in analyzer.py:

analyze_log("sample_logs/auth_easy.log", threshold=5, label="[EASY]")
```

## 🛠️ Current Progress

- Parses auth log files and extracts failed SSH login attempts
- Uses regex to detect and count failed attempts per IP address
- Modular detection logic moved to detections/brute_force.py
- Accepts threshold and label arguments for flexibility
- Cleaned file structure for clarity and reusability

### 🧪 Current Example Output
```
[!] Inside of [EASY] log report, 192.168.1.45 had 4 failed login attempts
[!] Inside of [MEDIUM] log report, 203.0.113.10 had 4 failed login attempts
[!] Inside of [HARD] log report, 198.51.100.77 had 6 failed login attempts
[!] Inside of [HARD] log report, 192.168.1.101 had 6 failed login attempts
```

📌 Next Steps

- Add CLI argument support (argparse) to accept file paths, thresholds, and labels from the terminal
- Add support for exporting results to a .csv or .json file
- Improve detection rules (e.g., support for different types of suspicious activity)
- Add unit tests for detection logic
- End Goal: Create a simple CLI or dashboard interface

