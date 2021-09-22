import functools

import nltk
from nltk.tokenize.toktok import ToktokTokenizer


load_spanish_tokenizer = functools.partial(
    nltk.data.load,
    'tokenizers/punkt/PY3/spanish.pickle',
)

try:
    spanish_tokenizer = load_spanish_tokenizer()
except LookupError:
    # We haven't downloaded the pre-trained tokenizers.

    # To get around 'Error loading punkt ... certificate verify failed'
    # see: https://github.com/gunthercox/ChatterBot/issues/930#issuecomment-322111087
    import ssl
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context

    # The Punkt Sentence Tokenizer divides a text into a list of sentences using an unsupervised
    # algorithm to build a model for abbreviation words, collocations, and words that start
    # sentences.
    nltk.download('punkt')
    # TODO: I think these might be useful when using the toktok tokenizer
    # nltk.download('perluniprops')
    # nltk.download('nonbreaking_prefixes')
    spanish_tokenizer = load_spanish_tokenizer()

# TODO: for breaking sentences into inidividual tokens.
# toktok_tokenizer = ToktokTokenizer()
# tokens = toktok_tokenizer.tokenize(sentence)

with open('data/cadiz_ch_1_text.txt', 'r', encoding='utf-8') as fp:
    text = fp.read().replace('\n', ' ')

sentences = spanish_tokenizer.sentences_from_text(text)

for sentence in sentences:
    print(sentence)
    print()
