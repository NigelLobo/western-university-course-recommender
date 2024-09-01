import pandas as pd
from generate_embeddings import query
from syllabi import syllabi

syllabi_descriptions = [value[1] for value in syllabi.values()]
output = query(syllabi_descriptions)
embeddings = pd.DataFrame(output)
embeddings.to_csv("syllabi_embeddings.csv", index=False)
print(f'Generated embeddings for {len(syllabi_descriptions)} courses')

