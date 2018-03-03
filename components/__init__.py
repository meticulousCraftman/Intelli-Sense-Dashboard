try:
	from . import speedometer
	from . import coolingUnit
except ImportError:
	from .components import *