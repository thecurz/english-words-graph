import os
from pathlib import Path

def check_path():
  CWD = f'{os.getcwd()}'
  if Path(CWD).name == 'english-words-graph':
    os.chdir(r'./project/')
    return f'{os.getcwd()}'
  if Path(CWD).name == 'data_generation':
    os.chdir(r'../')
    return f'{os.getcwd()}'
  return CWD