from __future__ import annotations
from typing import Optional, Union
import yaml
from dataclasses import dataclass
from . import settings


@dataclass
class YamlData:
	"""
	general data class defining main methods such as getting objects data from storage and taking
	queries from command line
	"""
	data: dict
	name: Optional[str]

	def __init__(self):
		self.data = self.get_data()

	def get(self):
		pass

	def get_data(self) -> dict[str, Union[str, list[str]]]:
		"""
		:return: returns readed data searched using class specs
		"""
		class_name = self.__class__.__name__
		filename = settings.DATA_BASE_DIR + class_name.lower() + settings.DATA_BASE_FILES_FORMAT
		try:
			data = yaml.load(open(filename), yaml.CLoader).get(class_name.lower())
			return data
		except FileNotFoundError:
			raise FileNotFoundError(f"Datafile named '{class_name}' wasn't found")
		except KeyError:
			raise KeyError(f"Incorrect datafile '{class_name}' format")

	def __repr__(self):
		"""
		:return: string defining for CLI query "list", specifying list of all data objects
		"""
		try:
			return f"List of available {self.__class__.__name__.lower()}:\n" \
				+ '\n'.join([f"* {obj['name']}" for obj in self.data])
		except KeyError:
			raise KeyError(f"Got an incorrect data attribute of class '{self.__class__.__name__}'")

	def execute_query(self, query: str, obj_name: Optional[str]) -> None:
		"""
		:param query: CLI-query "list" or "get"
		:param obj_name: obj name that needs to search
		"""
		if query == "list":
			print(self.__repr__())
		elif query == "get" and not obj_name is None:
			self.name = obj_name
			self.get()
			print(str(self))


class Builds(YamlData):
	"""
	class defining build with their dependencies founded in data storage
	"""
	def __init__(self,
				 name: Optional[str] = None):
		super().__init__()
		self.name = name
		self.tasks: Optional[list[Tasks]] = None

	def __str__(self):
		tasks_queue = []
		for task in self.tasks:
			task_with_depends = (f"{', '.join(task.dependencies)}, " if not task.dependencies is None else '') + \
								task.name
			tasks_queue.append(task_with_depends)
		return f"Build info:\n" \
			   f"* name: {self.name}\n" \
			   f"* tasks: {', '.join(tasks_queue)}"

	def get(self):
		"""
		defines objects of tasks that build owns
		"""
		if not self.name is None:
			try:
				tasks = next(filter(lambda item: item["name"] == self.name, self.data)).get('tasks')
			except StopIteration:
				raise Exception(f"Build named {self.name} wasn't found")
			self.tasks = [Tasks(task) for task in tasks]
			for task in self.tasks:
				task.get()


class Tasks(YamlData):
	"""
	class defining task with their dependencies founded in data storage
	"""
	def __init__(self,
				 name: Optional[str] = None):
		super().__init__()
		self.name = name
		self.dependencies: Optional[list[str]] = None

	def __str__(self):
		return f"Task info:\n" \
			   f"* name: {self.name}\n" \
			   f"* dependencies: {', '.join(self.dependencies) if any(self.dependencies) else 'not found'}"

	def get(self) -> None:
		"""
		defines task dependencies
		"""
		if not self.name is None:
			try:
				self.dependencies = next(filter(lambda item: item["name"] == self.name, self.data)).get('dependencies')
			except StopIteration:
				raise Exception(f"Task named {self.name} wasn't found")
