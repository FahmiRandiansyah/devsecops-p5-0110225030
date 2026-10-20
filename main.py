from src.calculator import FinancialCalculator
from src.logger import AppLogger

def main():
    logger = AppLogger()
    logger.log_action("Aplikasi dimulai.")

    calc = FinancialCalculator()
    roi = calc.calculate_roi(5000, 25000)
    print(f"Hasil ROI: {roi}%")

    logger.log_action("Aplikasi selesai dijalankan.")

if __name__ == "__main__":
    main()