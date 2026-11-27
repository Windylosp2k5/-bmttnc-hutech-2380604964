"""Điểm chạy thuận tiện: python lab_01/ex04/chay.py"""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from ex04.Main import main


if __name__ == "__main__":
    main()
