from repositories import FakeDocumentRepository, FakeWordRepository, FakePostingListRepository
from models import Document, Word, PostingList

document_repository = FakeDocumentRepository()
word_repository = FakeWordRepository()
posting_list_repository = FakePostingListRepository()

query = 'мама дядя'
