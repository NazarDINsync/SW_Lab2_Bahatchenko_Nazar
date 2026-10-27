"""Схема сутностей і зв'язків для екстракції фактів"""

from typing import Literal
from pydantic import BaseModel

# 5 типів сутностей
EntityType = Literal["Artist", "Album", "Label", "Genre", "Person"]

# 6 типів зв'язків
Predicate = Literal[
    "released",       # Artist -> Album
    "signed_to",      # Artist -> Label
    "has_genre",      # Artist/Album -> Genre
    "influenced_by",  # Artist/Genre -> Artist/Genre/Person
    "founded",        # Person/Artist -> Label
    "member_of",      # Person -> Artist (гурт)
]


class Fact(BaseModel):
    subject: str
    subject_type: EntityType
    predicate: Predicate
    object: str
    object_type: EntityType
    evidence: str  # цитата з тексту, щоб легко перевірити факт вручну


class FactList(BaseModel):
    facts: list[Fact]
