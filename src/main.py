import os
from .tests import test_cmd_args
from .static import strings
from .utils import init_yaml_strings, update_data_dir, model_init
from loguru import logger
from . import settings, stderror


def execute_from_command_line(*args) -> None:
	"""
	:param args: command line args that needs to parsing
	"""
	args = args[1:]
	test_cmd_args(args)
	execute_command(args)


def execute_command(cmd: tuple[str, ...]) -> None:
	"""
	:param cmd: handled and tested cmdline args
	"""
	query, model_name, obj_name = cmd[0], cmd[1], None
	if len(cmd) == 3:
		obj_name = cmd[2]
	model_obj = model_init(model_name)()
	model_obj.execute_query(query, obj_name)


def init_data() -> None:
	"""
	datafiles and their paths initializing
	"""
	data_files = init_yaml_strings(dir(strings))
	base_dir_changed = update_data_dir(data_files)
	init_data_dirs(base_dir_changed, data_files)


def init_data_dirs(flag: bool, files: list[str]) -> None:
	"""
	:param flag: bool instance that showing if paths changed
	:param files: defined data storage files paths
	"""
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
	"""
	:param files: defined data storage files paths
	"""
	base_dir = settings.DATA_BASE_DIR
	try:
		for file in files:
			content = getattr(strings, file)
			filename = file.lower() + settings.DATA_BASE_FILES_FORMAT
			with open(base_dir + filename, 'w') as file_out:
				file_out.write(content)
		return True
	except Exception as exs:
		stderror("Data writing error", exs)
		return False
