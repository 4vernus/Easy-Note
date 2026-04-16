# Writes extracted key points to a .md file
from pathlib import Path

def write_output(input_file,output,name):
    filepath = Path(input_file)
    dst_folder = Path("outputs")
    dst_folder.mkdir(exist_ok=True)
    if name is None:
        filename = f"{filepath.stem}.md"
    else:
        filename = f"{name}.md"
    dst_path = dst_folder / filename

    with open(dst_path, "w") as f:
        f.write(output)
    
    return dst_path

