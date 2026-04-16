# Writes extracted key points to a .md file
from pathlib import Path

def write_output(input_file,output,name):
    filepath = Path(input_file)
    dst_folder = Path("outputs")
    dst_folder.mkdir(exist_ok=True)
    name_counter = 1

    if name is None:
        name = filepath.stem

    filename = f"{name}.md"
    dst_path = dst_folder / filename

    while dst_path.exists():
        name_counter += 1
        filename = f"{name}({name_counter}).md"
        dst_path = dst_folder / filename
        

    with open(dst_path, "w", encoding="utf-8") as f:
        f.write(output)
    
    return dst_path

