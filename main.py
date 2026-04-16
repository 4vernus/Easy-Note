import argparse
from dotenv import load_dotenv
from src.ingest import accept_input
from src.output import write_output
from src.process import process_input

def main():

    load_dotenv()
    parser = argparse.ArgumentParser(description="Input text files to get an AI generated summary.")
    parser.add_argument("file")
    parser.add_argument("-o","--output", type=str, help="Output file")
    args = parser.parse_args()

    try:
        input_text = accept_input(args.file)
        processed_text = process_input(input_text)
        write_output(args.file, processed_text, name=args.output)
    except FileNotFoundError:
        print("File not found")
    except ValueError:
        print("Invalid file type")

if __name__ == "__main__":
    main()
