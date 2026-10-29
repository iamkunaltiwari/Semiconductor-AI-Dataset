from tqdm import tqdm
import re

from config import (
    SOURCE_DIR,
    SPICE_DIR,
    LOG_DIR
)

from utils import (
    save_csv,
    setup_logger,
    get_file_size,
    get_line_count,
)

SPICE_EXTENSIONS = [".spice", ".sp", ".cir"]


def find_spice_files():
    spice_files = []

    for extension in SPICE_EXTENSIONS:
        spice_files.extend(SOURCE_DIR.rglob(f"*{extension}"))

    return spice_files


def count_subckts(file_path):
    try:
        text = file_path.read_text(
            encoding="utf-8",
            errors="ignore"
        )

        return len(
            re.findall(
                r"\.subckt",
                text,
                re.IGNORECASE
            )
        )

    except Exception:
        return 0


def extract_spice_metadata():

    spice_files = find_spice_files()

    dataset = []

    print(f"\nFound {len(spice_files)} SPICE files.\n")

    for file in tqdm(spice_files):

        try:

            dataset.append({

                "repository": file.parts[2] if len(file.parts) > 2 else "Unknown",

                "file_name": file.name,

                "path": str(file),

                "size_bytes": get_file_size(file),

                "line_count": get_line_count(file),

                "subckt_count": count_subckts(file),

                "extension": file.suffix

            })

        except Exception as e:

            print(f"Error: {file}")
            print(e)

    return dataset


def save_spice_metadata():

    setup_logger(LOG_DIR / "spice_extractor.log")

    dataset = extract_spice_metadata()

    output_file = SPICE_DIR / "spice_metadata.csv"

    save_csv(dataset, output_file)

    print("\n==============================")
    print("SPICE Extraction Finished")
    print(f"Files Processed : {len(dataset)}")
    print(f"CSV Saved At    : {output_file}")
    print("==============================\n")


if __name__ == "__main__":
    save_spice_metadata()