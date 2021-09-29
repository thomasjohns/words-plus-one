import datetime as dt
from typing import Optional
from uuid import UUID

from sqlmodel import Field
from sqlmodel import SQLModel


class Table(SQLModel, table=True):
    id: UUID = Field(primary_key=True)


class User(Table):
    # TODO
    name: str


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


# for a word text there are multiple meanings
#   for a meaning there are multiple translations
# first use an algorithm to assign a meaning based
# on word embeddings ?and? translation text matching?
# use an existing translation and bump count
# or create a new one


class WordText(Table):
    # TODO
    # wonder if it is possible to create word for
    # each context ... (for each tranlation?)
    # use language models?
    text: str
    language: str
    frequency_rank: Optional[int]


# or WordMeaning ???
class WordMeaning(Table):
    # TODO
    # in a sense, this is the actual word
    # is there a way to encode context?
    # something with word vector embeddings?
    text: str
    source_language: str
    target_language: str
    # link to another table with multiple tranlations
    # with rankings?
    translation: str
    meaning ??? (a vector embedding?)

    word_text_id


class WordMeaningTranslationText(Table):
    # TODO
    # inferred text match based on translation
    text: str
    num_times_used: int

    word_meaning_id


# FIXME/HERE: how to handle `yo soy harry potter`
class IgnoredWord(Table):
    # TODO
    word_id

    user_id


class WordMeaningMemory(Table):
    # TODO
    # created for all words?
    # updated during review and reading
    strength: Optional[dt.timedelta]

    user_id
    word_id


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
