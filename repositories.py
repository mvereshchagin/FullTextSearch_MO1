from models import Document, Word, PostingList, DocumentLink
from irepositories import IDocumentRepository, IWordRepository, IPostingListRepository, IDocumentLinkRepository

from typing import List, Optional


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

    def set_weight(self, doc_id: int, weight: float) -> None:
        for doc in self.data:
            if doc.id == doc_id:
                doc.weight = weight


class FakeDocumentLinkRepository(IDocumentLinkRepository):

    data: List[DocumentLink] = [
        DocumentLink(id=1, doc_id_from=1, doc_id_to=6),
        DocumentLink(id=2, doc_id_from=1, doc_id_to=6),
        DocumentLink(id=3, doc_id_from=1, doc_id_to=5),
        DocumentLink(id=4, doc_id_from=1, doc_id_to=6),
        DocumentLink(id=5, doc_id_from=2, doc_id_to=4),
        DocumentLink(id=6, doc_id_from=2, doc_id_to=6),
        DocumentLink(id=7, doc_id_from=3, doc_id_to=4),
        DocumentLink(id=8, doc_id_from=3, doc_id_to=5),
        DocumentLink(id=9, doc_id_from=3, doc_id_to=6),
        DocumentLink(id=10, doc_id_from=3, doc_id_to=6),
        DocumentLink(id=12, doc_id_from=4, doc_id_to=3),
        DocumentLink(id=13, doc_id_from=4, doc_id_to=3),
        DocumentLink(id=14, doc_id_from=4, doc_id_to=6),
        DocumentLink(id=15, doc_id_from=5, doc_id_to=6),
        DocumentLink(id=16, doc_id_from=5, doc_id_to=5),
        DocumentLink(id=17, doc_id_from=5, doc_id_to=5),
        DocumentLink(id=18, doc_id_from=6, doc_id_to=6),
        DocumentLink(id=19, doc_id_from=6, doc_id_to=6),
        DocumentLink(id=20, doc_id_from=6, doc_id_to=6),
    ]

    def get_by_doc_id(self, doc_id: int) -> List[int]:
        return [document_link.doc_id_to for document_link in self.data
                if document_link.doc_id_from == doc_id]


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

    def get_by_word_id_an(self, word_id: int) -> List[PostingList]:
        # return [pl for pl in self.data if pl.word_id == word_id]
        for pl in self.data:
            if pl.word_id == word_id:
                yield pl

    def get_by_word_id_and_doc_id(self, word_id: int, doc_id: int) -> Optional[PostingList]:
        for pl in self.data:
            if pl.word_id == word_id and pl.document_id == doc_id:
                return pl

        return None
