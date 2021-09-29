from uuid import UUID

from sqlmodel import Field
from sqlmodel import SQLModel


# TODO: Can `table=true` be moved to here?
class Table(SQLModel):
    id: UUID = Field(primary_key=True)


class TextSource(Table, table=True):
    # TODO
    pass


class Fragment(Table, table=True):
    # TODO
    pass


class Word(Table, table=True):
    # TODO
    pass


class WordAppearance(Table, table=True):
    # TODO
    fragment_id: UUID


# TODO: Not sure if there should also be a word translation.
class FragmentTranslation(Table, table=True):
    # TODO
    pass


class Review(Table, table=True):
    # TODO
    pass


class User(Table, table=True):
    # TODO
    pass
