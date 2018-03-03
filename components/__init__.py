try:
	from . import speedometer
	from . import coolingUnit
	from . import timer
	from . import exitButton
except ImportError:
	from .components import *