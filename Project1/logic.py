from functools import reduce

class Logic:
    @staticmethod
    def add(values: list[float]) -> float:
        """Add all negative numbers."""
        num = [0]  # Initialize with zero
        for item in values:
            if item < 0:
                num.append(item)  # Append Negative only
        return sum(num)

    @staticmethod
    def subtract(values: list[float]) -> float:
        """Subtract all positive numbers."""
        num = []
        for item in values:
            if item > 0:
                num.append(item)  # Append Positive
        if len(num) < 1:
            num.append(0)  # If no positive numbers, start zero
        # Subtract sequentially
        return reduce(lambda x, y: x - y, num)

    @staticmethod
    def multiply(values: list[float]) -> float:
        """Multiply all non-zero numbers."""
        num = []
        for item in values:
            if item != 0:
                num.append(item)
        if len(num) < 1:
            num.append(0)  # If zero, then zero
        # Multiply sequentially
        return reduce(lambda x, y: x * y, num)

    @staticmethod
    def divide(values: list[float]) -> float:
        """Divide numbers sequentially."""
        return reduce(lambda x, y: sys.exit("It's illegal to divide by 0") if y == 0 else x / y, values)
