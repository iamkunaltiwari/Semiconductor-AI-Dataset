import json
import logging
from pathlib import Path
from datetime import datetime
import pandas as pd

# -----------------------------
# Logging
# -----------------------------
def setup_logger(log_file):
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )

# -----------------------------
# Save JSON
# -----------------------------
def save_json(data, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

# -----------------------------
# Save CSV
# -----------------------------
def save_csv(data, output_file):
    df = pd.DataFrame(data)
    df.to_csv(output_file, index=False)

# -----------------------------
# File Size
# -----------------------------
def get_file_size(file_path):
    return Path(file_path).stat().st_size

# -----------------------------
# Line Count
# -----------------------------
def get_line_count(file_path):
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            return sum(1 for _ in f)
    except Exception:
        return 0

# -----------------------------
# Current Time
# -----------------------------
def current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")