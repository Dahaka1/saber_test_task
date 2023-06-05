import os
import sys
from . import settings, models
from shutil import copy2
from typing import Optional, Any


def init_yaml_strings(args: list[str]) -> list[str]:
	"""
	finds strings in base static data file for writing in special data files
	"""
	return [arg for arg in args if not arg.startswith('__')]


def get_project_path() -> Optional[str]:
	"""
	:return: general project path
	"""
	main_file_path = os.path.realpath(sys.argv[0]) if sys.argv[0] else None
	if not main_file_path is None:
		return main_file_path.replace('\\main.py', '\\').replace('\\', '/')


def update_data_dir(args: list[str]) -> bool:
	"""
	function updates project directories if default data paths was
	changed in config-file and some data files already exists
	:param args: data files names
	"""
	files_moved = False
	if not os.path.exists(settings.DATA_BASE_DIR):
		os.mkdir(settings.DATA_BASE_DIR)
	if all(not file + settings.DATA_BASE_FILES_FORMAT in os.listdir(settings.DATA_BASE_DIR) for file in args):
		project_path = get_project_path()
		previous_files = find_data_filepaths(project_path, args)
		if not previous_files is None:
			previous_files_paths, previous_folder_path = find_data_filepaths(project_path, args)
			for file in previous_files_paths:
				copy2(file, settings.DATA_BASE_DIR)
				os.remove(file)
				files_moved = True
			with os.scandir(previous_folder_path) as p:
				if not(any(p)):
					os.rmdir(previous_folder_path)
	return files_moved


def find_data_filepaths(path: str, filenames: list[str]) -> Optional[tuple[list, str]]:
	"""
	:param path: project general path
	:param filenames: files that must be searched
	:return: None if files in previous data folder path wasn't founded or files paths and folder path if it was detected
	"""
	result = []
	for file in os.listdir(path):
		raw_filename = file.split('.')[0] if not os.path.isdir(path + file) else file
		if file.split('.')[0] in filenames:
			result.append(path + raw_filename)
			if len(result) == len(filenames):
				return result, path
		else:
			if os.path.isdir(path + file) and not file in ["venv", ".git", ".idea"]:
				for root, dirs, files in os.walk(path + file):
					if any(f.split('.')[0] in filenames for f in files):
						for f in files:
							if any(f.startswith(data_file) for data_file in filenames):
								f_path = f'{root}\\{f}'
								result.append(f_path)
								if len(result) == len(filenames):
									return result, root


def model_init(model_name: str) -> Any:
	"""
	:param model_name: model name that needs to be defined
	:return: class type hinting from models.py
	"""
	if not model_name.endswith('s'):
		model_name += 's'
	try:
		model_cls = getattr(models, model_name.title())
		return model_cls
	except Exception:
		raise AttributeError(f"Model named '{model_name}' isn't defined at 'src.models'")


