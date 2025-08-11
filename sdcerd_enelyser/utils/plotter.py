import matplotlib.pyplot as plt
import pandas as pd
from typing import List

def get_graph_options(csv_type: str) -> List[str]:
  """Return available graph options for a given CSV type."""
  if csv_type == 'TypeA':
    return ['Value1 vs Timestamp', 'Value2 vs Timestamp']
  elif csv_type == 'TypeB':
    return ['Measurement vs Date']
  else:
    return ['Raw Table']

def plot_graph(data: pd.DataFrame, csv_type: str, graph_option: str):
  """Plot the selected graph for the data."""
  if csv_type == 'TypeA':
    if graph_option == 'Value1 vs Timestamp':
      plt.plot(data['timestamp'], data['value1'])
      plt.xlabel('Timestamp')
      plt.ylabel('Value1')
      plt.title('Value1 vs Timestamp')
    elif graph_option == 'Value2 vs Timestamp':
      plt.plot(data['timestamp'], data['value2'])
      plt.xlabel('Timestamp')
      plt.ylabel('Value2')
      plt.title('Value2 vs Timestamp')
  elif csv_type == 'TypeB':
    if graph_option == 'Measurement vs Date':
      plt.plot(data['date'], data['measurement'])
      plt.xlabel('Date')
      plt.ylabel('Measurement')
      plt.title('Measurement vs Date')
  else:
    data.plot()
    plt.title('Raw Table')
  plt.tight_layout()
  plt.show()
