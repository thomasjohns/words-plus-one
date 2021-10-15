import nltk
from nltk.tokenize import word_tokenize


'''
try:
    nltk.download('wordnet')
    nltk.download('omw')  # open multilingual wordnet
except LookupError:
    # see comment in tokenize_sentences.py
    import ssl
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context
    nltk.download('wordnet')
    nltk.download('omw')  # open multilingual wordnet
'''

from nltk.corpus import wordnet
from nltk.wsd import lesk


#for sense in wordnet.synsets('casco', lang='spa'):
#    print(sense, sense.definition(), sense.examples())

for sense in wordnet.synsets('perro', lang='spa'):
    print(sense, sense.definition(), sense.examples())
print()

ctx = lesk(
    word_tokenize('Es un ladrido de perro.'),
    'perro',
    synsets=wordnet.synsets('perro', lang='spa'),
)
print(ctx, ctx.definition(), ctx.examples())
#ctx = lesk(
#    word_tokenize('Este hombre es un perro.'),
#    'perro',
#    synsets=wordnet.synsets('perro', lang='spa'),
#)
#print(ctx, ctx.definition(), ctx.examples())
#ctx = lesk(
#    word_tokenize('Tengo sed.'),
#    'tener',
#    synsets=wordnet.synsets('tener', lang='spa'),
#)
#print(ctx, ctx.definition(), ctx.examples())

#ctx1 = lesk(
#    word_tokenize(
#        'El casco antiguo de Barcelona es muy bonito'
#    ),
#    'casco',
#    synsets=wordnet.synsets('casco', lang='spa'),
#)
#print()
## TODO: dir(ctx1) shows many possibilities!
#print(ctx1, ctx1.definition(), ctx1.examples())
## NOTE: the context seemse like it records `n` for e.g. "noun" too!
#
#ctx2 = lesk(
#    word_tokenize(
#        'El casco nuevo que te has comprado para la motocicleta no me gusta'
#    ),
#    'casco',
#    synsets=wordnet.synsets('casco', lang='spa'),
#)
#print()
#print(ctx2, ctx2.definition(), ctx2.examples())
#
#print()
#
#print(dir(ctx2))
#
#print()
