from models import Document, Word, PostingList

from typing import List, Optional


class IDocumentRepository:
    def get_all(self) -> List[Document]:
        pass

    def add(self, document: Document) -> None:
        pass

    def get_by_id(self, doc_id: int) -> Document or None:
        pass

    def set_weight(self, doc_id: int, weight: float) -> None:
        pass


class IDocumentLinkRepository:
    def get_by_doc_id(self, doc_id: int) -> List[int]:
        pass


class IWordRepository:
    def get_all(self) -> List[Word]:
        pass

    def add(self, word: Word) -> None:
        pass

    def get_words(self) -> List[str]:
        pass
    
    def get_word(self, word: str) -> Word or None:
        pass


class IPostingListRepository:
    def get_all(self) -> List[PostingList]:
        pass

    def add(self, positing_list: PostingList) -> None:
        pass

    def get_by_word_id(self, word_id: int) -> List[PostingList]:
        pass

    def get_by_word_id_and_doc_id(self, word_id: int, doc_id: int) -> Optional[PostingList]:
        pass
