import torch
from datasets import load_dataset
from generate_embeddings import query
from sentence_transformers.util import semantic_search
from syllabi import syllabi

faqs_embeddings = load_dataset('nigellobo/syllabi_embeddings')
dataset_embeddings = torch.from_numpy(faqs_embeddings["train"].to_pandas().to_numpy()).to(torch.float)

def getMostRelevantCourses(text):
    output = query(text)
    print('[getMostRelevantCourses] ')
    query_embeddings = torch.FloatTensor(output)
    hits = semantic_search(query_embeddings, dataset_embeddings, top_k=3)
    courses = ''
    for i in range(len(hits[0])):
        idx = [hits[0][i]['corpus_id']][0]
        course_code = list(syllabi.keys())[idx]
        course_name = list(syllabi.values())[idx][0]
        courses += f'{1+i}. {course_code} - {course_name}\n'
    return courses
