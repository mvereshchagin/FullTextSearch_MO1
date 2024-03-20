from typing import Any, List, Dict, Tuple, Iterator

from config import document_link_repository, document_repository
from models import Document

alpha = 0.15
max_roll_count = 500


def roll() -> None:

    doc_rank_dict: Dict[int, List[float]] = {}
    for doc in document_repository.get_all():
        links: List[int] = document_link_repository.get_by_doc_id(doc.id)
        rank: float = doc.weight
        for doc_id, rank in map_fn(doc.id, (rank, links)):
            if doc_id not in doc_rank_dict:
                doc_rank_dict[doc_id] = [0, ]
            doc_rank_dict[doc_id].append(rank)

    # doc_ranks_res: Dict[int, float] = {}
    # for doc_id, ranks in doc_rank_dict.items():
    #     res_rank, _ = reduce_fn(doc_id, ranks)
    #     doc_ranks_res[doc_id] = res_rank
    #
    # for doc_id, rank in sorted(doc_ranks_res.items(), key=lambda x: x[1]):
    #     doc = document_repository.get_by_id(doc_id)
    #     print(f'{doc.url}, rank = {rank}')
    #     document_repository.set_weight(doc_id, rank)

    doc_ranks_res: List[Tuple[float, int]] = []
    for doc_id, ranks in doc_rank_dict.items():
        doc_ranks_res.append(reduce_fn(doc_id, ranks))

    for rank, doc_id in sorted(doc_ranks_res):
        doc = document_repository.get_by_id(doc_id)
        print(f'{doc.url}, rank = {-rank}')
        document_repository.set_weight(doc_id, -rank)


def map_fn(doc_id: int, value: Tuple[float, List[int]]) -> Iterator[Tuple[int, float]]:
    rank, doc_ids = value
    yield doc_id, 0

    if len(doc_ids):
        for doc_id_to in doc_ids:
            yield doc_id_to, float(rank) / len(doc_ids)
    else:
        all_docs = document_repository.get_all()
        for doc_id_to in all_docs:
            yield doc_id_to, float(rank) / len(all_docs)


def reduce_fn(doc_id: int, values: List[float]) -> Tuple[float, int]:
    all_docs = document_repository.get_all()
    return - ((1 - alpha) * sum(values) + alpha / len(all_docs)), doc_id


def main():
    for i in range(max_roll_count):
        print(f'----------------- roll {i + 1} --------------------')
        roll()
        print(f'-----------------------------------------------')
        print()


if __name__ == '__main__':
    main()
