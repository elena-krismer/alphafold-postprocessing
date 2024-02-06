from pathlib import Path
from typing import Any, Optional, TypedDict, cast
import pickle

def load_pkl(path: Path) -> dict[str, Any]:
    """Load a single pkl file"""
    with open(path, "rb") as stream:
        data: dict[str, Any] = pickle.load(stream)
        return data


def load_optional_pkl(path: Path) -> Optional[dict[str, Any]]:
    """Load a single pkl file if it exists, otherwise return None"""
    try:
        return load_pkl(path)
    except FileNotFoundError:
        return None
