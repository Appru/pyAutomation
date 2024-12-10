from pathlib import Path

def renameFiles():
    root_dir = Path('data')
    file_paths = root_dir.iterdir()
    for path in file_paths:
        new_filename = "new-" +path.stem +path.suffix
        new_filepath = path.with_name(new_filename)
        print(new_filepath)
        path.rename(new_filepath)

#renameFiles()

root_dir = Path('data')
file_paths = root_dir.glob("**/*")

for path in file_paths:
    if path.is_file():
        parent_folder = path.parts[-2]
        new_filename = parent_folder + '-'+ path.name
        print(new_filename)