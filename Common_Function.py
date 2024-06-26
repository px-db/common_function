import pandas as pd
import os
import json
import subprocess

def mid(text:str, start_pos:int, length:int):
  """
  Posisi dimulai dari 1
  """
  # Pastikan start_pos dan length adalah bilangan bulat yang valid
  if not isinstance(start_pos, int) or not isinstance(length, int):
      raise ValueError("Start position and length must be integers")
  
  # Periksa apakah start_pos valid dan tidak melebihi panjang string
  if start_pos < 0 or start_pos >= len(text):
      raise ValueError("Invalid start position")
  
  # Ambil substring dari string berdasarkan posisi dan panjang
  start_pos -= 1
  return text[start_pos:start_pos+length]

def parse_string(self,input_string, start_pos, length):
  """
  Posisi dimulai dari 0
  """
  # Pastikan start_pos dan length adalah bilangan bulat yang valid
  if not isinstance(start_pos, int) or not isinstance(length, int):
      raise ValueError("Start position and length must be integers")
  
  # Periksa apakah start_pos valid dan tidak melebihi panjang string
  if start_pos < 0 or start_pos >= len(input_string):
      raise ValueError("Invalid start position")
  
  # Ambil substring dari string berdasarkan posisi dan panjang
  return input_string[start_pos:start_pos + length]

def scan_file_in_dir(directory)->list:
  """
  Scan file di dalam direktori tidak termasuk sub direktori
  """
  # Periksa apakah direktori valid
  if not os.path.isdir(directory):
      raise ValueError("Invalid directory")
  
  # Minta list nama file dalam direktori
  files = os.listdir(directory)
  
  # Kembalikan list nama file
  return files

def scan_dir_and_subdir(directory)->list:
  """
  Scan file dan sub direktori
  """
  # Periksa apakah direktori valid
  if not os.path.isdir(directory):
      raise ValueError("Invalid directory")
  
  # List untuk menyimpan semua nama file
  all_files = []
  
  # Lakukan pemindaian untuk setiap item dalam direktori
  for item in os.listdir(directory):
      # Gabungkan path lengkap
      item_path = os.path.join(directory, item)
      # Jika item adalah direktori, lakukan pemindaian rekursif
      if os.path.isdir(item_path):
          all_files.extend(scan_dir_and_subdir(item_path))
      else:
          # Jika item adalah file, tambahkan ke list
          all_files.append(item_path)
  
  return all_files

def file_exists(file_path):
  """
  Cek apakah file ada. return 'True' atau 'False'
  """
  return os.path.exists(file_path)

def convert_xlsx_to_csv(file_xlsx, file_csv=None):
  """
  Proses konversi xlsx ke csv.
  """
  # Read xlsx and convert csv
  if file_csv :
    pd.read_excel(file_xlsx).to_csv(file_csv, index=False)
  else :
    pd.read_excel(file_xlsx).to_csv(f'{file_xlsx}.csv', index=False)
  return None

def convert_hexa_to_bitlist(hexa):
  '''
  Fungsi ini untuk konversi hexa dalam string menjadi bit dalam list
  dengan urutan Low Significant Bit (LSB) terlebih dahulu.

  Contoh :
  'A' = 1010 ; return [0,1,0,1]

  Parameter :
    hexa:str
  
  return : list
  '''
  # convert to bit
  bit = bin(int(hexa,16))
  len_x = len(str(bit)[2:])

  # add padding in front
  pad = '0'*(32-len_x)+str(bit)[2:]

  # list in reverse list
  return list(pad)[::-1]

def key_in_dict(key_to_check, dict_to_test:dict):
  '''
  Cek apakah value 'key_to_check' ada di dalam key dictionary 'dict_to_test'
  '''
  if key_to_check in dict_to_test.keys() :
    return True
  return False

def in_list(test, list_to_test):
  '''
  Cek apakah value 'test' ada di dalam list 'list_to_test'
  '''
  if test in list_to_test :
    return True
  return False

def curl(curl):
  return subprocess.run(
      curl.split(),
      capture_output=True,
      text=True
      ).stdout

def join_list(list_name:list, sep=","):
  return sep.join(map(str,list_name))

def print_list(list_name):
  for i in list_name :
    print(i)
  return None

def print_dict(dict_name):
  for key, value in dict_name.items():
    print(key, ":", value)
  return None

def string_to_json(json_string):
  """
  Konversi string json ke dict
  """
  return json.loads(json_string)

def json_to_string(py_dict):
  """
  Konveri dict ke string json
  """
  return json.dumps(py_dict)
