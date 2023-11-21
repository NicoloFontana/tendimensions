import json
import random
from datetime import datetime as dt
import os

import pandas as pd

import utils

PROJECT_PATH = "C:\\Users\\fonta\\PycharmProjects\\tendimensions"
DATASET_PATH = f"{PROJECT_PATH}\\data\\IBM_Debater_(R)_arg_quality_rank_30k\\arg_quality_rank_30k.csv"

df = pd.read_csv(DATASET_PATH)
k = 10
chunk_size = 2
id_len = 5
samples = random.sample(list(df["argument"]), k)
ids = utils.generate_alphanumeric_ids(k, id_len)
id_sample_pairs = zip(ids, samples)
samples_dict = dict(id_sample_pairs)
print("Samples extracted!")

DIR_NAME = dt.now().strftime("%Y%m%d%H%M")
OUT_DIR_PATH = f"{PROJECT_PATH}\\out\\{DIR_NAME}"
SCORING_PATH = f"{OUT_DIR_PATH}\\scoring"
SAMPLES_PATH = f"{OUT_DIR_PATH}\\samples"
CHUNKS_PATH = f"{SAMPLES_PATH}\\chunks"

os.mkdir(OUT_DIR_PATH)
os.mkdir(SCORING_PATH)
os.mkdir(SAMPLES_PATH)
os.mkdir(CHUNKS_PATH)
print("Directories made!")


OUT_NAME = f"{k}_samples_{DIR_NAME}"

OUT_FILE_NAME = f"{OUT_NAME}.txt"
OUT_FILE_PATH = f'{SAMPLES_PATH}\\{OUT_FILE_NAME}'
with open(OUT_FILE_PATH, 'w') as convert_file:
    convert_file.write(json.dumps(samples_dict))

chunks = utils.chunks(samples_dict, chunk_size)

for chunk in chunks:
    n_chunk = chunks.index(chunk)
    with open(f"{CHUNKS_PATH}\\chunk_{n_chunk}.txt", 'w') as convert_file:
        convert_file.write(json.dumps(chunk))
print("Samples file generated!")
