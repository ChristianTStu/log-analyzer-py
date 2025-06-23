from detections.brute_force import analyze_log

analyze_log("sample_logs/auth_easy.log", label="[EASY]")
analyze_log("sample_logs/auth_medium.log", label ="[MEDIUM]")
analyze_log("sample_logs/auth_hard.log", label ="[HARD]")