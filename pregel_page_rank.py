from pregel import Pregel, Vertex
from config import document_repository, document_link_repository

num_workers = 4
num_vertices = 10
alpha = 0.15
max_count = 50


def main():

    vertices = {doc.id: PageRankVertex(id=doc.id, value=doc.weight, out_vertices=[])
                for doc in document_repository.get_all()}

    global num_vertices
    num_vertices = len(vertices)

    for vertex in vertices.values():
        link_ids = document_link_repository.get_by_doc_id(vertex.id)
        vertex.out_vertices = [vertices[link_id] for link_id in link_ids]

    p = Pregel(vertices.values(), num_workers)
    p.run()

    for vertex in vertices.values():
        doc = document_repository.get_by_id(vertex.id)
        print(f'{doc.url}: {vertex.value}')


class PageRankVertex(Vertex):

    def update(self):

        if self.superstep >= max_count:
            self.active = False
            return

        self.value = alpha / num_vertices + (1 - alpha) * sum(
            [pagerank for (vertex, pagerank) in self.incoming_messages])

        if len(self.out_vertices) == 0:
            outgoing_pagerank = self.value / num_vertices
        else:
            outgoing_pagerank = self.value / len(self.out_vertices)

        self.outgoing_messages = [(vertex, outgoing_pagerank)
                                  for vertex in self.out_vertices]


if __name__ == "__main__":
    main()
