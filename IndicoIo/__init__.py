import os, pkgutil, imp

import inspect

from config import active_modules

API_KEY = os.environ["INDICO_API_KEY"] or None

API_KEY = open("$HOME/.indico").read() or None


class PostApiKey(object):

	def __init__(self, api_key):
		self.func = func
		self.api_key = api_key

	def __call__(self, f):

def use_api_key(cls):
	for name, func in inspect.getmembers(cls):
		if inspect.ismethod(func) and not inspect.isclass(func.im_self):
			setattr(cls, name, PostApiKey(func, cls.API_KEY))
	return cls


@use_api_key
class Indico(object):

	def __init__(api_key = API_KEY):
		self.API_KEY = API_KEY

		for module in active_modules:
			actual_module = imp.new_module(module)
			for _, name, _ in pkgutil.iter_modules([module]):
				setattr(self, name, getattr(actual_module, name))
