import itertools
from pathlib import Path

def build_prompt(path):
    root_dir = Path(path)
    
    combined_content = []
    for file_path in root_dir.rglob("*"):
        if file_path.suffix in [".py", ".md"]:
            combined_content.append([str(file_path.relative_to(root_dir)), file_path.read_text()])
    
    return "\n==================\n".join([f"[start of file: {f}]\n\n{c}\n\n[end of file: {f}]" for f,c in combined_content])

