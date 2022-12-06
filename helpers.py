from pathlib import Path
from typing import Callable, Any, Optional


def read_file_as_list(filepath: str, apply_func: Callable, fallback: Any, strip_str: Optional[str] = None) -> list:
    file = Path(filepath).open()
    lines = []
    for line in file.readlines():
        line = line.strip(strip_str)
        try:
            line = apply_func(line)
        except ValueError:
            line = fallback
        lines.append(line)
    return lines
