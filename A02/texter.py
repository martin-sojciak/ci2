"""Count all words and capitalized words in a text file."""
import sys


class Texter:
    """Process a text file and print word statistics."""

    def __init__(self, file_name):
        self.file_name = file_name

    def run(self):
        """Print the number of words and of capitalized words."""
        with open(self.file_name, encoding="utf-8") as file:
            words = file.read().split()
        capitalized = [w for w in words if w[0].isupper()]
        print("Number of words:", len(words))
        print("Number of words starting with a capital letter:",
              len(capitalized))


def main():
    if len(sys.argv) < 2:
        print("Usage: python texter.py <text_file>")
        return
    Texter(sys.argv[1]).run()


if __name__ == "__main__":
    main()
