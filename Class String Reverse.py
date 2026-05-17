class StringReverser:
    def reverse_words(self, s: str) -> str:
        """
        Reverses the string word by word.
        
        Args:
            s (str): The input string to be reversed.
            
        Returns:
            str: A new string with the words in reverse order.
        """
        # The split() method without arguments automatically splits by whitespace
        # and handles multiple spaces between words, returning a list of words.
        words = s.split()
        
        # Reverse the list of words using slicing
        reversed_words = words[::-1]
        
        # Join the words back together with a single space
        return " ".join(reversed_words)

if __name__ == "__main__":
    # Create an instance of the class
    reverser = StringReverser()
    
    # Test cases
    test_strings = [
        "hello world",
        "  a good   example  ",
        "Python programming is fun"
    ]
    
    print("--- String Word Reverser ---")
    for test in test_strings:
        result = reverser.reverse_words(test)
        print(f"Original: '{test}'")
        print(f"Reversed: '{result}'\n")
