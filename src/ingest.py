# Handles collecting user input
from pathlib import Path

# Validate user input
def accept_input(input_filepath):
    try:
        if input_filepath.suffix.lower() == ".txt":
            with open(input_filepath, "r") as f:
                return f.read()
        else:
            raise ValueError("Invalid file type")
    except FileNotFoundError as e:
        raise FileNotFoundError("File not found") from e

