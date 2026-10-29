from pathlib import Path

# ==========================================
# Semiconductor AI Dataset Configuration
# ==========================================

# Root directory (change only if your project moves)
ROOT_DIR = Path(r"C:\Users\kt598")

# Main Dataset Folder
DATASET_DIR = ROOT_DIR / "Semiconductor_AI_Dataset"

# Repository Scan Location
SOURCE_DIR = ROOT_DIR

# Output Directories
RTL_DIR = DATASET_DIR / "RTL"
SV_DIR = DATASET_DIR / "SystemVerilog"
SPICE_DIR = DATASET_DIR / "SPICE"
LEF_DIR = DATASET_DIR / "LEF"
DEF_DIR = DATASET_DIR / "DEF"
LIBERTY_DIR = DATASET_DIR / "Liberty"
GDS_DIR = DATASET_DIR / "GDS"

JSON_DIR = DATASET_DIR / "JSON"
CSV_DIR = DATASET_DIR / "CSV"
LOG_DIR = DATASET_DIR / "Logs"
METADATA_DIR = DATASET_DIR / "Metadata"

# Supported File Extensions
RTL_EXTENSIONS = [".v"]
SYSTEMVERILOG_EXTENSIONS = [".sv"]
SPICE_EXTENSIONS = [".spice", ".sp"]
LEF_EXTENSIONS = [".lef"]
DEF_EXTENSIONS = [".def"]
LIBERTY_EXTENSIONS = [".lib"]
GDS_EXTENSIONS = [".gds"]

# Scan Settings
IGNORE_FOLDERS = {
    ".git",
    "__pycache__",
    ".venv",
    "venv",
    "node_modules"
}

# Dataset Version
DATASET_VERSION = "0.1.0"