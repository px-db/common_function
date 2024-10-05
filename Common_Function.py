import pandas as pd
import os
import json
import subprocess
import sqlite3
import csv

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

def file_list(files:list, extensions:list)->list:
  # Filter file dengan ekstensi tertentu
  return [file for file in files if any(file.endswith(ext) for ext in extensions)]

def list_to_sqlite(db_name:str, data_list:list, columns:list, table_name:str)->None:
  """
  Parameter :
    db_name : nama database (string)
    data_list : data dalam list
    columns : kolom table
      columns = [
          ('ID', 'INTEGER PRIMARY KEY'),
          ('Name', 'TEXT'),
          ('Age', 'INTEGER')
      ]
    table_name : nama tabel (string)

  """
  # Koneksikan ke database SQLite (atau buat database baru jika belum ada)
  conn = sqlite3.connect(db_name)
  
  # Buat cursor objek
  cursor = conn.cursor()

  columns_with_types = ', '.join([f'{col_name} {col_type}' for col_name, col_type in columns])
  create_table_sql = f'CREATE TABLE IF NOT EXISTS {table_name} ({columns_with_types})'
  # Buat tabel jika belum ada
  cursor.execute(create_table_sql)
  # Simpan perubahan

  # Masukkan data ke dalam tabel
  insert_sql = f'INSERT INTO {table_name} ({", ".join([col_name for col_name, _ in columns])}) VALUES ({", ".join(["?" for _ in columns])})'
  cursor.executemany(insert_sql, data_list)

  conn.commit()
  
  # Tutup koneksi
  conn.close()

def csv_to_List(fileCsv)->list:
  # Inisialisasi list kosong untuk menyimpan data
  data_list = []
  # Buka file CSV dan baca isinya
  with open(fileCsv, 'r') as file:
    csv_reader = csv.reader(file)    
    # Lewati baris header
    next(csv_reader, None)    
    # Iterasi setiap baris dalam file CSV
    for row in csv_reader:
      data_list.append(row)
  return data_list

def sqlite_to_list(file_database:str, query:str)->list:
  # Koneksi ke database SQLite
  conn = sqlite3.connect(file_database)
  # Membuat objek cursor
  cursor = conn.cursor()
  # Menjalankan query untuk mengambil data
  cursor.execute(query)
  # Mengambil hasil query dan mengubahnya menjadi list
  rows = cursor.fetchall()
  # Menutup koneksi
  conn.close()
  # return hasil sebagai list
  return rows

def sqlite_to_df(file_database:str, query:str):
  # Koneksi ke database SQLite
  conn = sqlite3.connect(file_database)
  # Membaca data dari SQLite (kolom tertentu) ke dalam DataFrame
  df = pd.read_sql_query(query, conn)
  # Menutup koneksi
  conn.close()
  return df

def list_to_csv(data:list, outputCsv:str):
  with open(outputCsv, mode='w', newline='') as file:
    writer = csv.writer(file)    
    # Menulis setiap baris dari list ke file CSV
    writer.writerows(data)
