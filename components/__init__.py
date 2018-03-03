try:
	from . import speedometer
	from . import coolingUnit
	from . import timer
except ImportError:
	from .components import *