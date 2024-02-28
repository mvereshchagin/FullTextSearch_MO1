from models import Document, Word, PostingList
from irepositories import IDocumentRepository, IWordRepository, IPostingListRepository

from typing import List


class FakeDocumentRepository(IDocumentRepository):

    data: List[Document] = [
        Document(1, 'yandex.ru', 200, 12),
        Document(2, 'rf.gov', 250, 20),
        Document(3, 'microsoft.com', 300, 35),
        Document(4, 'linux.org', 200, 23),
        Document(5, 'kaggle.com', 124, 12),
        Document(6, 'kantiana.ru', 123, 5),
    ]

    def get_all(self) -> List[Document]:
        return self.data

    def add(self, document: Document) -> None:
        self.data.append(document)

    def get_by_id(self, doc_id: int) -> Document or None:
        for doc in self.data:
            if doc.id == doc_id:
                return doc
        return None


class FakeWordRepository(IWordRepository):

    data: List[Word] = [
        Word(id=1, word='мама', weight=100),
        Word(id=2, word='папа', weight=120),
        Word(id=3, word='дедушка', weight=60),
        Word(id=4, word='бабушка', weight=80),
        Word(id=5, word='тетя', weight=15),
        Word(id=6, word='дядя', weight=5),
    ]

    def get_all(self) -> List[Word]:
        return self.data

    def add(self, word: Word) -> None:
        self.data.append(word)

    def get_words(self) -> List[str]:
        return [item.word for item in self.data]

    def get_word(self, word: str) -> Word or None:
        for w in self.data:
            if w.word.lower() == word.lower():
                return w

        return None


class FakePostingListRepository(IPostingListRepository):

    data: List[PostingList] = [
        PostingList(id=1, document_id=6, word_id=3, weight=70),
        PostingList(id=1, document_id=4, word_id=5, weight=56),
        PostingList(id=1, document_id=2, word_id=2, weight=123),
        PostingList(id=1, document_id=1, word_id=1, weight=200),
        PostingList(id=1, document_id=4, word_id=4, weight=156),
        PostingList(id=1, document_id=1, word_id=6, weight=103),
        PostingList(id=1, document_id=1, word_id=5, weight=156),
        PostingList(id=1, document_id=4, word_id=1, weight=34),
        PostingList(id=1, document_id=2, word_id=1, weight=21),
    ]

    def get_all(self) -> List[PostingList]:
        return self.data

    def add(self, positing_list: PostingList) -> None:
        self.data.append(positing_list)

    def get_by_word_id(self, word_id: int) -> List[PostingList]:
        return [pl for pl in self.data if pl.word_id == word_id]
