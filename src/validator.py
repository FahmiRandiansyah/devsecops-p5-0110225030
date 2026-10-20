class InputValidator:
    @staticmethod
    def validate_positive_number(value: float) -> bool:
        if value < 0:
            return False
        return True