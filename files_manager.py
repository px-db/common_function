import os

def ls(path_dir:str, **kwargs) :
  result = []
  rec = kwargs.get('recursive', True)
  fil = kwargs.get('with_file', True)
  ext = kwargs.get('extension', None)

  # Validasi
  if not os.path.isdir(path_dir):
      raise ValueError("Invalid directory")
  
  # Scan file di dalam direktori tidak termasuk sub direktori
  if not rec :
    results = os.listdir(directory)

  # Scan file dan sub direktori
  if rec :
    for item in os.listdir(directory):
      # Gabungkan path lengkap
      item_path = os.path.join(directory, item)
      # Jika item adalah direktori, lakukan pemindaian rekursif
      if os.path.isdir(item_path):
          results.extend(ls(item_path, recursive=True))
      else:
          # Jika item adalah file, tambahkan ke list
          results.append(item_path)
  
  # Kembalikan list nama file
  return results
  
  
