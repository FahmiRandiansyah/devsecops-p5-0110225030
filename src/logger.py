import datetime

class AppLogger:
    def log_action(self, message: str):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] LOG: {message}")