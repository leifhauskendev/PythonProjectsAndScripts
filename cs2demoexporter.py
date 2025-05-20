import sys
import os
import subprocess

def install_and_import(package):
    try:
        __import__(package)
    except ImportError:
        print(f"Installing {package}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install_and_import("zstandard")

import zstandard as zstd

OUTPUT_FOLDER_PATH = "C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\game\csgo"

# take in inputs
input_file = sys.argv[1]
output_file_name = sys.argv[2]

# format file extensions if they do not exist
if not input_file.endswith('.zst'):
    if not input_file.endswith('.dem'):
        input_file = input_file + '.dem.zst'
    else:
        input_file = input_file + '.zst'

if not output_file_name.endswith('.dem'):
        output_file_name = output_file_name + '.dem'

# build file paths
input_file_path = os.path.join("C:\\Users\\leifh\\Downloads", input_file)
output_file_path = os.path.join(OUTPUT_FOLDER_PATH, output_file_name)

# extract and export
try:
    with open(input_file_path, 'rb') as compressed:
        with open(output_file_path, 'wb') as destination:
            dctx = zstd.ZstdDecompressor()
            dctx.copy_stream(compressed, destination)

    print(f"Successfully exported {input_file} to {OUTPUT_FOLDER_PATH} as {output_file_name}!")

except Exception as e:
    print(f"An issue occurred extracting and moving the demo: {e}'")
