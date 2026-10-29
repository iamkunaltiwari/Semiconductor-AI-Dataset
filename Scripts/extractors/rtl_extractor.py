from pathlib import Path
import re

from tqdm import tqdm

from config import (
    SOURCE_DIR,
    RTL_DIR,
    LOG_DIR,
    RTL_EXTENSIONS,
)

from utils import (
    save_csv,
    setup_logger,
    get_file_size,
    get_line_count,
)


def find_rtl_files():
    """Find all RTL (.v) files."""
    rtl_files = []

    for ext in RTL_EXTENSIONS:
        rtl_files.extend(SOURCE_DIR.rglob(f"*{ext}"))

    return rtl_files


def count_modules(file_path: Path):
    """Count Verilog modules inside a file."""
    try:
        text = file_path.read_text(
            encoding="utf-8",
            errors="ignore"
        )

        return len(re.findall(r"\bmodule\b", text))

    except Exception:
        return 0


def extract_rtl_metadata():
    """Extract metadata from RTL files."""

    rtl_files = find_rtl_files()

    dataset = []

    print(f"\nFound {len(rtl_files)} RTL files.\n")

    for file in tqdm(rtl_files):

        try:

            dataset.append(
                {
                    "repository": file.parts[2] if len(file.parts) > 2 else "Unknown",
                    "file_name": file.name,
                    "path": str(file),
                    "extension": file.suffix,
                    "size_bytes": get_file_size(file),
                    "line_count": get_line_count(file),
                    "module_count": count_modules(file),
                }
            )

        except Exception as e:
            print(f"Error: {file}")
            print(e)

    return dataset


def save_rtl_metadata():

    setup_logger(LOG_DIR / "rtl_extractor.log")

    dataset = extract_rtl_metadata()

    output_file = RTL_DIR / "rtl_metadata.csv"

    save_csv(dataset, output_file)

    print("\n==============================")
    print("RTL Extraction Finished")
    print(f"Files Processed : {len(dataset)}")
    print(f"CSV Saved At    : {output_file}")
    print("==============================\n")


if __name__ == "__main__":
    save_rtl_metadata()