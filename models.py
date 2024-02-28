from dataclasses import dataclass


@dataclass
class Document:
    id: int
    url: str
    length: int
    weight: float


@dataclass
class Word:
    id: int
    word: str
    weight: float


@dataclass
class PostingList:
    id: int
    document_id: int
    word_id: int
    weight: float
