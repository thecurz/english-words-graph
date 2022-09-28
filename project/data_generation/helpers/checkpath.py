import os
from pathlib import Path

def check_path():
  CWD = f'{os.getcwd()}'
  if Path(CWD).name == 'graph-english-words':
    os.chdir(r'./project/')
    return os.getcwd()
  if Path(CWD).name == 'data_generation':
    os.chdir(r'../')
    return os.getcwd()
  