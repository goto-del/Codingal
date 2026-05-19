class IntegerToRoman:
    """
    A class to convert integer values to their corresponding Roman numeral representations.
    """
    def __init__(self):
        # A list of tuples mapping integer values to their Roman numeral representations.
        # It's ordered from largest to smallest to facilitate the conversion algorithm.
        self.value_map = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]

    def convert(self, num: int) -> str:
        """
        Converts a given integer to a Roman numeral.

        Args:
            num (int): The integer to convert. Must be between 1 and 3999.

        Returns:
            str: The Roman numeral representation of the integer.

        Raises:
            TypeError: If the input is not an integer.
            ValueError: If the input is out of the valid range (1-3999).
        """
        if not isinstance(num, int):
            raise TypeError("Input must be an integer.")
        if not (0 < num < 4000):
            raise ValueError("Input must be between 1 and 3999 (inclusive).")

        roman_numeral = ""
        # Iterate through the values and symbols
        for value, symbol in self.value_map:
            # While the remaining number is greater than or equal to the value,
            # append the symbol to the result and subtract the value from the number.
            while num >= value:
                roman_numeral += symbol
                num -= value
                
        return roman_numeral

# Example Usage
if __name__ == "__main__":
    # Create an instance of the class
    converter = IntegerToRoman()

    # Test cases
    test_numbers = [3, 58, 1994, 2026, 3999]
    
    print("Integer to Roman Numeral Conversion:")
    print("-" * 40)
    for number in test_numbers:
        roman = converter.convert(number)
        print(f"{number:<5} ->  {roman}")
