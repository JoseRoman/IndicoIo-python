JSON_HEADERS = {'Content-type': 'application/json', 'Accept': 'text/plain'}
__version__ = '0.3.3'

from text.sentiment import political, posneg
from text.sentiment import posneg as sentiment
from text.lang import language
from images.fer import fer
from images.features import facial_features
