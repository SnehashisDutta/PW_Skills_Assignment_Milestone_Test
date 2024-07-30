# file_operations.py

def read_file(file_path):
  """Reads data from a file.

  Args:
      file_path (str): The path to the file to read.

  Returns:
      str: The contents of the file, or an empty string if the file is empty.
  """
  try:
    with open(file_path, 'r') as file:
      return file.read()
  except FileNotFoundError:
    print(f"Error: File not found at '{file_path}'")
    return ""

def write_file(file_path, data):
  """Writes data to a file, overwriting the existing content.

  Args:
      file_path (str): The path to the file to write to.
      data (str): The data to write to the file.
  """
  try:
    with open(file_path, 'w') as file:
      file.write(data)
    print(f"Data written to '{file_path}' successfully.")
  except Exception as e:
    print(f"Error writing to file: {e}")

def append_file(file_path, data):
  """Appends data to an existing file.

  Args:
      file_path (str): The path to the file to append to.
      data (str): The data to append to the file.
  """
  try:
    with open(file_path, 'a') as file:
      file.write(data)
    print(f"Data appended to '{file_path}' successfully.")
  except Exception as e:
    print(f"Error appending to file: {e}")