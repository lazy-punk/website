import os

def remove_copy_prefix(file_name):
  """
  Removes the "Copy of " prefix from a file name.

  Args:
      file_name: The name of the file to be converted.

  Returns:
      The new file name without the "Copy of " prefix.
  """
  if file_name.startswith("Copy of "):
    return file_name[8:]  # Remove "Copy of " (length 8)
  else:
    return file_name

def rename_files(folder_path):
  """
  Renames all files in a folder by removing the "Copy of " prefix.

  Args:
      folder_path: The path to the folder containing the files to be renamed.
  """
  for file_name in os.listdir(folder_path):
    old_path = os.path.join(folder_path, file_name)
    new_name = remove_copy_prefix(file_name)
    new_path = os.path.join(folder_path, new_name)

    # Check if the new name is different before renaming
    if old_path != new_path:
      os.rename(old_path, new_path)
      print(f"Renamed: {old_path} to {new_path}")

# Replace 'your_folder_path' with the actual path to your folder
set
