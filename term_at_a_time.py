from config import document_repository, word_repository, posting_list_repository, query
from models import Word, Document, PostingList


def arrange_documents():

    scored = {}
    for qt in query.split():

        word = word_repository.get_word(qt)
        if word is None:
            continue

        pls = posting_list_repository.get_by_word_id(word.id)

        for pl in pls:
            doc = document_repository.get_by_id(pl.document_id)
            if doc is None:
                continue

            if doc.id not in scored:
                scored[doc.id] = 0
            scored[doc.id] += word.weight * pl.weight / doc.length

    scored = reversed(sorted(scored.items(), key=lambda x: x[1]))
    for doc_id, weight in scored:
        doc = document_repository.get_by_id(doc_id)
        print(f'{doc.url}: {weight}')


# launch
arrange_documents()
