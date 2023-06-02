from . import settings


def test_cmd_args(args: tuple) -> None:
	if len(args) == 3:
		args = args[:-1]
	assert len(args) in [2, 3], "Non-standard amount of command-line arguments"
	assert all(item in settings.SUPPORTED_COMMANDS for item in args[:-1]), "Non-supported command was found"
