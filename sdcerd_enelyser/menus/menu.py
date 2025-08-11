from pathlib import Path
from typing import Optional
from sdcerd_enelyser.utils.file_utils import list_csv_files, detect_csv_type
from sdcerd_enelyser.utils.data_loader import load_csv_data
from sdcerd_enelyser.utils.plotter import plot_graph

class Menu:
  def __init__(self):
    self.selected_file: Optional[Path] = None
    self.data = None
    self.csv_type: Optional[str] = None
    self.last_action = ""
    self.exit_requested = False

  def print_logo(self):
    print(r"""
   _____ _____     _____             _   _____        _                               _                     
  / ____|  __ \   / ____|           | | |  __ \      | |            /\               | |                    
 | (___ | |  | | | |     ___ _ __ __| | | |  | | __ _| |_ __ _     /  \   _ __   __ _| |_   _ ___  ___ _ __ 
  \___ \| |  | | | |    / _ \ '__/ _` | | |  | |/ _` | __/ _` |   / /\ \ | '_ \ / _` | | | | / __|/ _ \ '__|
  ____) | |__| | | |___|  __/ | | (_| | | |__| | (_| | || (_| |  / ____ \| | | | (_| | | |_| \__ \  __/ |   
 |_____/|_____/   \_____\___|_|  \__,_| |_____/ \__,_|\__\__,_| /_/    \_\_| |_|\__,_|_|\__, |___/\___|_|   
                                                                                         __/ |              
                                                                                        |___/               
""")
    print("==================== SDCerdEnelyser ====================\n")

  def display_menu(self):
    self.print_logo()
    print("===== Main Menu =====")
    print(f"1. Select data file{' [' + str(self.selected_file) + ']' if self.selected_file else ''}")
    print("2. Select graph to show")
    print("3. Exit")
    if self.last_action:
      print(f"\n{self.last_action}")

  def get_user_choice(self, min_val: int, max_val: int, prompt: str) -> int:
    while True:
      try:
        choice = int(input(prompt))
        if min_val <= choice <= max_val:
          return choice
        else:
          print(f"Please enter a number between {min_val} and {max_val}.")
      except ValueError:
        print("Invalid input. Please enter a number.")

  def select_file(self):
    files = list_csv_files(Path("data"))
    if not files:
      self.last_action = "No CSV files found in ./data directory."
      return
    print("\nSelect a CSV file:")
    for idx, file in enumerate(files, 1):
      print(f"  [{idx}] {file.name}")
    choice = self.get_user_choice(1, len(files), "Enter file index: ")
    self.selected_file = files[choice - 1]
    self.csv_type = detect_csv_type(self.selected_file)
    self.data = load_csv_data(self.selected_file)
    self.last_action = f"Selected file: {self.selected_file.name} (type: {self.csv_type})"

  def select_graph(self):
    if self.data is None:
      self.last_action = "No data loaded. Please select a file first."
      return
    graph_options = plot_graph.get_graph_options(self.csv_type)
    print("\nSelect graph to show:")
    for idx, name in enumerate(graph_options, 1):
      print(f"  [{idx}] {name}")
    choice = self.get_user_choice(1, len(graph_options), "Enter graph index: ")
    plot_graph(self.data, self.csv_type, graph_options[choice - 1])
    self.last_action = f"Displayed graph: {graph_options[choice - 1]}"

  def run(self):
    while not self.exit_requested:
      self.display_menu()
      choice = self.get_user_choice(1, 3, "Enter choice: ")
      if choice == 1:
        self.select_file()
      elif choice == 2:
        self.select_graph()
      elif choice == 3:
        self.exit_requested = True
