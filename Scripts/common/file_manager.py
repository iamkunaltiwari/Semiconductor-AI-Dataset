from pathlib import Path


def ensure_directory(path):
    """
    Create directory if it does not exist.
    """
    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)
    return path


def file_exists(path):
    """
    Check whether a file exists.
    """
    return Path(path).exists()


def get_all_files(root, extensions=None):
    """
    Return all files under a directory.
    """
    root = Path(root)

    files = []

    if extensions is None:
        return list(root.rglob("*"))

    for ext in extensions:
        files.extend(root.rglob(f"*{ext}"))

    return files