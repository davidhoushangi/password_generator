# Python Password Generator Toolkit
<img width="700" height="600" alt="image" src="https://github.com/user-attachments/assets/77dc730a-b5ff-44dd-ba13-5a37df850ca5" />

## Project Description
A Python-based toolkit designed to generate various types of passwords. Built using Object-Oriented Programming (OOP) principles, this project provides a flexible architecture for creating numeric PINs, highly randomized string passwords, and memorable word-based passwords.

## Features
*   **Abstract Base Class**: Uses an ABC `PasswordGenerator` to ensure a consistent interface for all generators.
*   **PIN Generator**: Creates numeric-only PINs of a specified length.
*   **Random Password Generator**: Creates complex passwords using letters, numbers, and symbols based on user preferences.
*   **Memorable Password Generator**: Creates easy-to-remember passwords using a vocabulary of words, with options for capitalization and custom separators.

## Project Structure
```text
password-generator/
│
├── src/
│   └── password_generator.py  # Main script containing all classes
|   └── dashboard.py # used streamlit to showcase
│── requirements.txt
└── README.md
```
## Requirements
- Python 3.7+
- nltk (Optional: Currently imported but not yet utilized in the core logic)

## Installation
1. Clone the repository:
```bash
https://github.com/davidhoushangi/password_generator.git

```
## Usage
You can import the classes into your own Python scripts to generate passwords programmatically.

1. Generate a PIN
```python

from src.password_generator import PinGenerator

pin_gen = PinGenerator(length=6)
print(pin_gen.generate())  # Example output: "049281"

```
2. Generate a Random Password
```python

from src.password_generator import RandomPasswordGenerator

# Generate an 12-character password with numbers and symbols
rand_gen = RandomPasswordGenerator(length=12, include_numbers=True, include_symbols=True)
print(rand_gen.generate())  # Example output: "aB3$kL9!mN2@"

```
3. Generate a Memorable Password

```python
from src.password_generator import MemorablePasswordGenerator

# Generate a 3-word password, capitalized, separated by underscores
mem_gen = MemorablePasswordGenerator(number_of_words=3, separator="_", capitalization=True)
print(mem_gen.generate())  # Example output: "ALEX_DAVID_ELENA"

```


## Running the Script
The script includes a basic if __name__ == "__main__": block to demonstrate functionality. You can run it directly from your terminal:

```bash
python src/password_generator.py
```

## Notes & Future Improvements

- Unused Import: nltk is currently imported but not utilized. In the future, this could be used to pull a larger, more diverse vocabulary for the MemorablePasswordGenerator.

- Vocab Bug: In MemorablePasswordGenerator, if a custom vocab list is passed, the code currently doesn't save it to self.vocab. Adding an else block (else: self.vocab = vocab) will fix this.

- Testing: Add unit tests using pytest or unittest to ensure the generators handle edge cases properly.


