from repositories import FakeDocumentRepository, FakeWordRepository, \
    FakePostingListRepository, FakeDocumentLinkRepository
from models import Document, Word, PostingList

document_repository = FakeDocumentRepository()
word_repository = FakeWordRepository()
posting_list_repository = FakePostingListRepository()
document_link_repository = FakeDocumentLinkRepository()

query = 'мама дядя'
