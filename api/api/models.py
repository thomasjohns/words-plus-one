import datetime as dt
from typing import Literal
from typing import Optional
from uuid import UUID

from sqlmodel import Field
from sqlmodel import SQLModel


class Table(SQLModel, table=True):
    id: UUID = Field(primary_key=True)


class User(Table):
    # TODO
    name: str
    active_source_language: str
    active_target_language: str


class Source(Table):
    # TODO
    title: str
    author: Optional[str] = None
    language: str
    upload_datetime: dt.datetime
    private: bool = Field(default=True)

    uploaded_by_user_id


class Fragment(Table):
    # TODO
    text: str

    source_id
    # TODO
    prev_context: str  # 3 sentences back?
    next_context: str  # 3 sentences forward?


# for a word text there are multiple meanings
#   for a meaning there are multiple translations
# first use an algorithm to assign a meaning based
# on word embeddings ?and? translation text matching?
# use an existing translation and bump count
# or create a new one


class WordBase:
    text: str
    language: str
    frequency_rank: Optional[int] = None


class IgnoredWord(Table, WordBase):
    kind: Literal['detected_proper_noun', 'user_ignored']


class Word(Table, WordBase):
    # TODO
    # wonder if it is possible to create word for
    # each context ... (for each tranlation?)
    # use language models?
    pass


class Lexeme(Table):
    # TODO this is like run
    pass


class WordForm(Table):
    # TODO this is like run, runs, ran, running
    text: str
    language: str
    frequency_rank: Optional[int] = None

    # many word forms for a single lexeme
    lexeme_id


# FIXME: Create a ideas.txt file and move these notes and
#        TODOs here to it.

# NOTE: One version of the app could assign a
#       single WordSense to each WordForm and
#       a single memory for each WordSense.
#       It seems like different WordForms might
#       have different senses anyway. One interesting
#       thing could be to bump the memory of other
#       WordForms of the same Lexeme when one instance
#       of a WordForm is reviewed, but that might be
#       tricky because it might not make sense to bump
#       all senses of a WordForm.

# TODO: Is there a way to represent the knowledge of a
#       grammar form? Could the recommendation algorithm
#       recommend a sentence with a new grammar form, but
#       with known word senses?

# TODO: Use containing discourse to determine sense?
#       I.e. look at e.g. whole paragraph?

# TODO: Some way to store word colocations? Maybe just let
#       the language model take care of this based on its
#       training?

# TODO: Handle garden-path sentences? Think this could
#       be done by assigning a memory to the fragments
#       in addition to the individual word senses composed
#       in the sentence.

# TODO: Similar sounding and spelling word
#       seperation/decorrelation in the memory algorithm? I.e.
#       handling similar words that are easily "mixed up".

# TODO: Get google translate, msft, and deepl fragment translations?

# TODO: Can there be some kind of memory link between different
#       word forms of the same morphology? (the linguistic terminology
#       in this sentence may be incorrect.)

# TODO: The amount that you would bump the memory of any given word,
#       depends on to what extent that word was recalled from long-term
#       memory or short term memory.

# TODO: Some kind of memory influence based on source to target
#       language cognates.

# TODO: Is it possible to provide a translation service a chunk in
#       context, i.e. pass a specific chunk and a full sentence to
#       the translation service, and get a translation for just the
#       chunk informed by the context?

# or WordMeaning ???
# or WordSense!!
class WordSense(Table):
    # TODO
    # in a sense, this is the actual word
    # is there a way to encode context?
    # something with word vector embeddings?
    text: str
    source_language: str
    target_language: str
    # link to another table with multiple tranlations
    # with rankings? this could be useful for informational
    # purposes if not academic purposes.
    translation: str
    # meaning ??? (a vector embedding?)
    # possible that this ^ should be done outside the
    # database?

    # could maybe use wordnet/nltk/lesk or a specialization of BERT?
    wordnet_sense: Optional[str]

    # TODO sense vector embedding?
    # TODO pointer into a GloVe resource?
    embedding_sense: Optional[...]

    # could also organize by part of speach taging!?
    # e.g. the noun 'giant' vs the adjective 'giant'
    part_of_speech: Optional[Literal[...]]

    # not sure about these
    semantic_role: Optional[Literal[...]]
    # SpaCy features fast statistical NER for named entity recognition
    named_entity: Optional[Literal[...]]
    # TODO: should variants for ^ be encoded in a pydantic Field?

    # also named entity recognition?

    # bitext word alignment!?

    # also maybe there is a way to incrementally add
    # complexity here to not get too hung up on it

    # example text (for this word meaning/sense)?

    # add one for each sense,
    # and then one for unknown sense?

    word_id


class WordSenseTranslationText(Table):
    # TODO
    # inferred text match based on translation
    text: str
    num_times_used: int

    word_sense_id


class WordSenseMemory(Table):
    # TODO
    # created for all words?
    # updated during review and reading
    strength: Optional[dt.timedelta]

    user_id
    word_sense_id


# FIXME ???
class WordSenseAppearance(Table):
    # TODO: keep track of all appearances of a particular sense
    #       of a particular word
    pass


class FragmentTranslationMemory(Table):
    # TODO
    # only created after lookup or review recommendation
    # updated during review (or reading if exact same?)
    strength: Optional[dt.timedelta]

    user_id
    fragment_id


class WordTranslationAppearance(Table):
    # TODO

    word_translation_id
    fragment_id
    word_translation_memory_id


class FragmentTranslation(Table):
    # TODO
    text: str
    datetime: dt.datetime
    target_language: str

    fragment_id


class Review(Table):
    # TODO
    correct: bool
    datetime: dt.datetime

    fragment_id
