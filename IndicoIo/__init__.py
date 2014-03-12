import os, pkgutil, imp

from config import active_modules

API_KEY = os.environ["INDICO_API_KEY"] or None

API_KEY = open("$HOME/.indico").read() or None

class Indico(object):

	def __init__(api_key = API_KEY):
		self.API_KEY = API_KEY

		for module in active_modules:
			actual_module = imp.new_module(module)
			for _, name, _ in pkgutil.iter_modules([module]):
				setattr(self, name, getattr(actual_module, name))
