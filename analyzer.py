from detection_categories.authentication_attempts.detect_failed_logins import detect_failed_logins

detect_failed_logins("sample_logs/auth_easy.log", label="[EASY]")
detect_failed_logins("sample_logs/auth_medium.log", label ="[MEDIUM]")
detect_failed_logins("sample_logs/auth_hard.log", label ="[HARD]")