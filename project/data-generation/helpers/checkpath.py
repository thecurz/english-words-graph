import os
from pathlib import Path

def check_path():
  CWD = f'{os.getcwd()}'
  if Path(CWD).name == 'graph-english-words':
    os.chdir(r'./project/')
    return f'{os.getcwd()}'
  