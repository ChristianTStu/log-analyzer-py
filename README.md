# Log Analyzer (Python)

A command-line tool to analyze system logs for signs of brute-force and other unauthorized access attempts.

## Features

- Parse Unix-style auth logs
- Detect repeated failed logins from same IP
- Modular detection logic in `/detections`

## File Structure
```
log-analyzer-py/
├── sample_logs/
│   └── auth.log            # Sample input log file
├── detections/             # Modular detection logic
│   ├── __init__.py
│   └── brute_force.py
├── analyzer.py             # Main Python script
├── requirements.txt        # Libraries used
├── README.md               # Project overview
└── .gitignore              # Ignore files like __pycache__
```

