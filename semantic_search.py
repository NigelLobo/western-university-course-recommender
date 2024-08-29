import torch
from datasets import load_dataset
from generate_embeddings import query
from sentence_transformers.util import semantic_search
from syllabus_embeddings import syl_list

faqs_embeddings = load_dataset('nigellobo/syllabi_embeddings')
dataset_embeddings = torch.from_numpy(faqs_embeddings["train"].to_pandas().to_numpy()).to(torch.float)

question = ["I hate web design"]
output = query(question)

query_embeddings = torch.FloatTensor(output)
hits = semantic_search(query_embeddings, dataset_embeddings, top_k=4)
print(hits)
print([['CS 1026', 'CS 1027', 'CS 1032', 'CS 1033'][hits[0][i]['corpus_id']] for i in range(len(hits[0]))])
