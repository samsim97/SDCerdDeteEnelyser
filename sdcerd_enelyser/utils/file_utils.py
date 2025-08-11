from pathlib import Path
from typing import List, Optional
import pandas as pd

def list_csv_files(directory: Path) -> List[Path]:
  """List all CSV files in the given directory."""
  return [f for f in directory.glob('*.csv') if f.is_file()]

def detect_csv_type(file_path: Path) -> Optional[str]:
  """Detect the type of CSV file based on its columns."""
  try:
    df = pd.read_csv(file_path, nrows=1)
    columns = set(df.columns)
    if {'timestamp', 'value1', 'value2'} <= columns:
      return 'TypeA'
    elif {'date', 'measurement'} <= columns:
      return 'TypeB'
    else:
      return 'Unknown'
  except Exception:
    return None
