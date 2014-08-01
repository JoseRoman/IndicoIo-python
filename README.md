indicoio-python
===============

A wrapper for a series of APIs made by Indico Data Solutions.

Check out the main site on:

http://indico.io

Our APIs are totally free to use, and ready to be used in your application. No data or training required.

Current APIs
------------

Right now this wrapper supports the following apps:

- Political Sentiment Analysis
- Positive/Negative Sentiment Analysis
- Facial Emotion Recognition
- Facial Feature Extraction
- Language Detection

Examples
--------
```
>>> import numpy as np

>>> from indicoio import political, sentiment, fer, facial_features, language

>>> political("Guns don't kill people. People kill people.")
{u'Libertarian': 0.22934946808893228, u'Liberal': 0.2025395008382684, u'Green': 0.0, u'Conservative': 1.0}

>>> sentiment('Worst movie ever.')
{u'Sentiment': 0.07062467665597527}

>>> sentiment('Really enjoyed the movie.')
{u'Sentiment': 0.8105182526856075}

>>> test_face = np.linspace(0,50,48*48).reshape(48,48).tolist()

>>> fer(test_face)
{u'Angry': 0.08843749137458341, u'Sad': 0.39091163159204684, u'Neutral': 0.1947947999669361, u'Surprise': 0.03443785859010413, u'Fear': 0.17574534848440568, u'Happy': 0.11567286999192382}

>>> facial_features(test_face)
[0.0, -0.02568680526917187, 0.21645604230056517, -0.1519435786033145, -0.5648621854611555, 3.0607368045577226, 0.11434321880792693, -0.02163810928547493, -0.44224330594186484, 0.3024315632285246, -2.6068048934495276, 2.497798330306638, 3.040558335205844, 0.741045340525325, 0.37198135618478817, -0.33132377802172325, -0.9804190889833034, 0.5046575784709395, -0.5609132323152847, 1.679107064439151, 0.6825037853544341, -1.5977176226648016, 1.8959464303080562, -0.7812860715595836, -2.998394007543733, -0.22637273967347724, -0.9642457010679496, 1.4557274834236749, 2.412244419186633, 2.3151771738421965, 0.7881483386786367, 1.6622850935863422, 0.1304768990234367, 1.9344501393866649, 3.1271558035162914, -0.10250886439220543, 1.4921395116492966, 2.761645355670677, 1.6903473594991179, 1.009209807271491, 0.07273926986120445, -1.4941708135718021, -2.082786362439631, 1.0160924044870847, 2.5326580674673895, -0.8328208491083264, 2.0390177029762935, 3.0342637531932777]

>>> language_dict = language('Quis custodiet ipsos custodes')
>>> language_dict
{u'Swedish': 0.00033330636691921914, u'Lithuanian': 0.007328693814717631, u'Vietnamese': 0.0002686116137658802, u'Romanian': 8.133913804076592e-06, u'Dutch': 0.09380619821813883, u'Korean': 0.00272046505489883, u'Danish': 0.0012556466207667206, u'Indonesian': 6.623391878530033e-07, u'Latin': 0.8230599921384231, u'Hungarian': 0.0012793617391960567, u'Persian (Farsi)': 0.0019848504383980473, u'Turkish': 0.0004606965429738638, u'French': 0.00016792646226101638, u'Norwegian': 0.0009179030069742254, u'Russian': 0.0002643396088456642, u'Thai': 7.746466749651003e-05, u'Finnish': 0.0026367338676522643, u'Spanish': 0.011844579596827902, u'Bulgarian': 3.746416283126873e-05, u'Greek': 0.027456554742563633, u'Tagalog': 0.0005143018200605518, u'English': 0.00013517846159760138, u'Esperanto': 0.0002599482830232367, u'Italian': 2.650711180999111e-06, u'Portuguese': 0.013193681336032896, u'Chinese': 0.008818957727120736, u'German': 0.00011732494215411359, u'Japanese': 0.0005885208894664065, u'Czech': 9.916434007248934e-05, u'Slovak': 8.869445598583308e-05, u'Hebrew': 3.70933525938127e-05, u'Polish': 9.900290296255447e-05, u'Arabic': 0.00013589586110619373}

>>> sorted(language_dict.keys(), key=lambda x: language_dict[x], reverse=True)
[u'Latin', u'Dutch', u'Greek', u'Portuguese', u'Spanish', u'Chinese', u'Lithuanian', u'Korean', u'Finnish', u'Persian (Farsi)', u'Hungarian', u'Danish', u'Norwegian', u'Japanese', u'Tagalog', u'Turkish', u'Swedish', u'Vietnamese', u'Russian', u'Esperanto', u'French', u'Arabic', u'English', u'German', u'Czech', u'Polish', u'Slovak', u'Thai', u'Bulgarian', u'Hebrew', u'Romanian', u'Italian', u'Indonesian']

```

Installation
------------
```
pip install indicoio
```
