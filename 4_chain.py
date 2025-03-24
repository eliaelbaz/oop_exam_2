import random
import statistics

class Handler:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle(self, number_array):
        if self.next_handler:
            self.next_handler.handle(number_array)

class SortHandler(Handler):
    def handle(self, number_array):
        sort_choice = input("Sort the array? (yes/no): ").strip().lower()
        if sort_choice == "yes":
            number_array.numbers = sorted(number_array.numbers)
            print(f"Sorted array: {number_array.numbers}")
        super().handle(number_array)


class MultiplyHandler(Handler):
    def handle(self, number_array):
        multiply_choice = input("Multiply array elements by a number? (yes/no): ").strip().lower()
        if multiply_choice == "yes":
            factor = int(input("Enter the multiplication factor: "))
            number_array.numbers = [num * factor for num in number_array.numbers]
            print(f"Array after multiplication: {number_array.numbers}")
        super().handle(number_array)


class AverageHandler(Handler):
    def handle(self, number_array):
        average_choice = input("Calculate average? (yes/no): ").strip().lower()
        if average_choice == "yes":
            number_array.average = sum(number_array.numbers) / len(number_array.numbers)
            print(f"Average of numbers: {number_array.average}")
        super().handle(number_array)


class StdDevHandler(Handler):
    def handle(self, number_array):
        std_choice = input("Calculate standard deviation? (yes/no): ").strip().lower()
        if std_choice == "yes":
            if len(number_array.numbers) > 1:
                number_array.std_deviation = statistics.stdev(number_array.numbers)
                print(f"Standard deviation: {number_array.std_deviation}")
            else:
                print("Cannot calculate standard deviation with less than 2 numbers")
        super().handle(number_array)

class NumberArray:
    def __init__(self, size):
        self._numbers = [random.randint(1, 100) for _ in range(size)]
        self._average = None
        self._std_deviation = None

    @property
    def numbers(self):
        return self._numbers

    @property
    def average(self):
        return self._average

    @property
    def std_deviation(self):
        return self._std_deviation

    @numbers.setter
    def numbers(self, new_numbers):
        self._numbers = new_numbers

    @average.setter
    def average(self, value):
        self._average = value

    @std_deviation.setter
    def std_deviation(self, value):
        self._std_deviation = value

class ChainProcessor:
    def __init__(self):
        self.chain = SortHandler(MultiplyHandler(AverageHandler(StdDevHandler())))

    def process(self, number_array):
        self.chain.handle(number_array)


def main():
    size = int(input("Enter the size of the array: "))
    number_array = NumberArray(size)
    print(f"Original array: {number_array.numbers}")

    processor = ChainProcessor()
    processor.process(number_array)

    print(f"Final array: {number_array.numbers}")
    print("\nStored Statistics:")
    if number_array.average is not None:
        print(f"Average: {number_array.average}")
    if number_array.std_deviation is not None:
        print(f"Standard Deviation: {number_array.std_deviation}")

if __name__ == "__main__":
    main()