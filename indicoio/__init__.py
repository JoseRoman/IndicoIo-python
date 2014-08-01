JSON_HEADERS = {'Content-type': 'application/json', 'Accept': 'text/plain'}

Version, version, __version__, VERSION = ('0.4.1',) * 4

from text.sentiment import political, posneg
from text.sentiment import posneg as sentiment
from text.lang import language
from images.fer import fer
from images.features import facial_features
