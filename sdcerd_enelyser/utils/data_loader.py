from pathlib import Path
import pandas as pd
from typing import Optional

def load_csv_data(file_path: Path) -> Optional[pd.DataFrame]:
  """Load CSV data into a pandas DataFrame."""
  try:
    return pd.read_csv(file_path)
  except Exception as e:
    print(f"Error loading CSV: {e}")
    return None
