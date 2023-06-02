from .static import config
from typing import Any, Optional
from loguru import logger


class Settings:
	def __getattribute__(self, item) -> Any:
		out = getattr(config, item)
		if item == "DATA_BASE_DIR":
			out = out.replace('.', str())
			out = out + '/' if len(out) > 1 and not out.endswith('/') else out
		return out


settings = Settings()


def logger_init() -> None:
	for level in settings.LOGGING_LEVELS:
		logger.add(
			settings.ERRORS_OUTPUT_FILE,
			level=level,
			format=settings.LOGGING_FORMAT,
			rotation="1 MB",
			compression="zip"
		)


def stderror(content: str, exception: Optional[Exception] = None) -> None:
	logger.error(
		f'{content}' + (f': exception {exception.__class__.__name__} - {exception}' if not exception is None else '')
	)

