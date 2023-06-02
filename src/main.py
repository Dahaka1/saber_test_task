import os
from .tests import test_cmd_args
from .static import strings
from .utils import init_yaml_strings, update_data_dir
from loguru import logger
from . import settings, stderror
import yaml


def execute_from_command_line(*args) -> None:
	args = args[1:]
	test_cmd_args(args)


def init_data() -> None:
	data_files = init_yaml_strings(dir(strings))
	base_dir_changed = update_data_dir(data_files)
	init_data_dirs(base_dir_changed, data_files)


def init_data_dirs(flag: bool, files: list[str]) -> None:
	if flag:
		logger.info(
			f"Base data files directory was successfully updated to '{settings.DATA_BASE_DIR}'"
		)
	else:
		if not all(file + settings.DATA_BASE_FILES_FORMAT in os.listdir(settings.DATA_BASE_DIR) for file in files):
			files_writing = write_yaml(files)
			if files_writing:
				logger.info(
					f"Data files {files} was successfully created at '{settings.DATA_BASE_DIR}'"
				)


def write_yaml(files: list[str]) -> bool:
	base_dir = settings.DATA_BASE_DIR
	try:
		for file in files:
			content = getattr(strings, file)
			filename = file + settings.DATA_BASE_FILES_FORMAT
			with open(base_dir + filename, 'w') as file_out:
				file_out.write(content)
		return True
	except Exception as exs:
		stderror("Data writing error", exs)
		return False
