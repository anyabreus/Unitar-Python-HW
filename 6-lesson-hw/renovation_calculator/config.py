from pathlib import Path

APARTMENT_SIZE = 68.00
CATEGORIES = ["Матеріали", "Роботи"]

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DATA_FILE = DATA_DIR / "renovation.csv"
