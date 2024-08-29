import pandas as pd
from generate_embeddings import query
from syllabi import syllabi

syl_list = [syllabi['CS 1026'], syllabi['CS 1027'], syllabi['CS 1032'], syllabi['CS 1033']]
output = query(syl_list)
embeddings = pd.DataFrame(output)
embeddings.to_csv("syllabi_embeddings.csv", index=False)

