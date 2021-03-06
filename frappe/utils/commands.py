import functools
import requests
from terminaltables import AsciiTable


@functools.lru_cache(maxsize=1024)
def get_first_party_apps():
	"""Get list of all apps under orgs: frappe. erpnext from GitHub"""
	apps = []
	for org in ["frappe", "erpnext"]:
<<<<<<< HEAD
		req = requests.get(f"https://api.github.com/users/{org}/repos", {"type": "sources", "per_page": 200})
=======
		req = requests.get("https://api.github.com/users/{0}/repos".format(org), {"type": "sources", "per_page": 200})
>>>>>>> c86f945bdab2473f784e9ca5ecf8f1b0d9624886
		if req.ok:
			apps.extend([x["name"] for x in req.json()])
	return apps


def render_table(data):
	print(AsciiTable(data).table)


def add_line_after(function):
	"""Adds an extra line to STDOUT after the execution of a function this decorates"""
	def empty_line(*args, **kwargs):
		result = function(*args, **kwargs)
		print()
		return result
	return empty_line


def add_line_before(function):
	"""Adds an extra line to STDOUT before the execution of a function this decorates"""
	def empty_line(*args, **kwargs):
		print()
		result = function(*args, **kwargs)
		return result
	return empty_line


def log(message, colour=''):
	"""Coloured log outputs to STDOUT"""
	colours = {
		"nc": '\033[0m',
		"blue": '\033[94m',
		"green": '\033[92m',
		"yellow": '\033[93m',
		"red": '\033[91m',
		"silver": '\033[90m'
	}
	colour = colours.get(colour, "")
	end_line = '\033[0m'
	print(colour + message + end_line)
