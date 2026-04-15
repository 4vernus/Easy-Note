# Writes extracted key points to a .md file
from pathlib import Path

def write_output(input_file,output):
    dst_folder = Path("outputs")
    dst_folder.mkdir(exist_ok=True)
    filename = f"{input_file.stem}.md"
    dst_path = dst_folder / filename

    with open(dst_path, "w") as f:
        f.write(output)
    
    return dst_path

