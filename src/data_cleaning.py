import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

raw_path = BASE_DIR / "data" / "vgsales_raw.csv"
processed_path = BASE_DIR / "data" / "vgsales_processed.csv"

df = pd.read_csv(raw_path)

df["Publisher"] = df["Publisher"].fillna("Unknown")
df.to_csv(processed_path, index = False)

cols = ["Publisher", "Name", "Platform"]

for col in cols:
    df[col] = df[col].str.title()

print("Dataset listo para analisis")
df.to_csv(processed_path, index = False)