try:
	from . import speedometer
	from . import coolingUnit
	from . import timer
	from . import exitButton
	from . import otherStats
except ImportError:
	from .components import *