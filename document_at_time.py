from config import document_repository, word_repository, posting_list_repository, query
from models import Word, Document, PostingList


def arrange_documents() -> None:
    scored = {}

    for doc in document_repository.get_all():
        for qt in query.split():
            word = word_repository.get_word(qt)
            pl = posting_list_repository\
                .get_by_word_id_and_doc_id(word_id=word.id, doc_id=doc.id)
            if pl is None:
                continue

            if doc.id not in scored.keys():
                scored[doc.id] = 0

            scored[doc.id] = word.weight * pl.weight / doc.length

    scored = reversed(sorted(scored.items(), key=lambda x: x[1]))
    for doc_id, weight in scored:
        doc = document_repository.get_by_id(doc_id)
        print(f'{doc.url}: {weight}')


arrange_documents()
