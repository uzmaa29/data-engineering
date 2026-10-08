from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from cleaning.clean_data import clean_data
from transformation.transform_data import transform

if __name__ == "__main__":
    clean_data()
    transform()
    print("End-to-end ingestion, cleaning, and transformation pipeline completed.")
