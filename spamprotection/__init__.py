"""Initial Directory."""
__version__ = "0.1.1"

try:
	from .client import SPBClient  # noqa: F401
except ModuleNotFoundError:
	# in setup.py, this import will cause problems
	# because dependencies aren't always installed
	pass
