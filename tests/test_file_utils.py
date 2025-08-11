from sdcerd_enelyser.utils.file_utils import list_csv_files, detect_csv_type
from pathlib import Path
import tempfile
import pandas as pd

def test_list_csv_files():
  with tempfile.TemporaryDirectory() as tmpdir:
    d = Path(tmpdir)
    (d / 'a.csv').write_text('col1,col2\n1,2')
    (d / 'b.txt').write_text('not a csv')
    files = list_csv_files(d)
    assert len(files) == 1 and files[0].name == 'a.csv'

def test_detect_csv_type():
  with tempfile.TemporaryDirectory() as tmpdir:
    d = Path(tmpdir)
    # TypeA
    (d / 'typea.csv').write_text('timestamp,value1,value2\n1,2,3')
    # TypeB
    (d / 'typeb.csv').write_text('date,measurement\n2020-01-01,5')
    # Unknown
    (d / 'unknown.csv').write_text('foo,bar\n1,2')
    assert detect_csv_type(d / 'typea.csv') == 'TypeA'
    assert detect_csv_type(d / 'typeb.csv') == 'TypeB'
    assert detect_csv_type(d / 'unknown.csv') == 'Unknown'
