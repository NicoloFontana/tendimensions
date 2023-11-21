import random
import string
from itertools import islice


def generate_alphanumeric_ids(num_ids, length, prefix=""):
    alphanumeric_chars = string.ascii_letters + string.digits
    ids = []

    for i in range(num_ids):
        unique_id = prefix + ''.join(random.choice(alphanumeric_chars) for _ in range(length))
        ids.append(unique_id)

    return ids


def chunks(data, SIZE=2):
    it = iter(data)
    chunks_list = []
    for i in range(0, len(data), SIZE):
        chunks_list.append({k: data[k] for k in islice(it, SIZE)})
    return chunks_list
