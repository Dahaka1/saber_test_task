import sys
from src.main import execute_from_command_line, init_data
from src import logger_init


def main():
	if len(sys.argv) > 1:
		logger_init()
		init_data()
		execute_from_command_line(*sys.argv)
	else:
		raise AttributeError("There are no command-line args was founded.")


if __name__ == '__main__':
	main()
