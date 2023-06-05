DATA_BASE_DIR = "data"
DATA_BASE_FILES_FORMAT = ".yaml"  # only this format supports
SUPPORTED_COMMANDS = [
	"list",
	"get",
	"builds",
	"tasks",
	"task",
	"build"
]

LOGGING_FORMAT = '{time} {level} {message}'
ERRORS_OUTPUT_FILE = 'logs.log'
LOGGING_LEVELS = [
	"ERROR",
	"INFO"
]
