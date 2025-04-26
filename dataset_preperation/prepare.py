from datasets import load_dataset
import pandas as pd

dataset = load_dataset("wdc/products-2017", split="train", trust_remote_code=True)
df = dataset.to_pandas()

#print(df.head())

# id_left
# title_left
# description_left
# brand_left
# category_left

df = df[['id_left', 'title_left', 'description_left', 'brand_left', 'category_left']]
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)
df.to_csv("products_cleaned.csv", index=False)