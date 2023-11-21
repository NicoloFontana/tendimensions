import json
import tendims



# load the model
model = tendims.TenDimensionsClassifier(is_cuda=True, models_dir = './models/lstm_trained_models', embeddings_dir='./embeddings')
# print the list of dimensions
dimensions = model.main_dimensions_list

## load sentences
DIR_NAME = "202311211114"
k = 10
IN_NAME = f"{k}_samples_{DIR_NAME}.txt"
IN_FILE_NAME = f"{IN_NAME}"
IN_FILE_PATH = f"C:\\Users\\fonta\\PycharmProjects\\tendimensions\\out\\{DIR_NAME}\\samples\\{IN_FILE_NAME}"
file = open(IN_FILE_PATH)
samples = json.load(file)
print("Samples loaded!")

scoring = {}
# compute overall score and per-sentence scores
for sample_id in samples:
    sentence = samples[sample_id]
    scoring.update({sample_id: {}})
    for dim in dimensions:
        score = model.compute_score(sentence, dim)
        scoring[sample_id].update({dim: score})
    print(f"{samples[sample_id]}:\n{scoring[sample_id]}")

OUT_FILE_NAME = f"LSTM.txt"
OUT_FILE_PATH = f"C:\\Users\\fonta\\PycharmProjects\\tendimensions\\out\\{DIR_NAME}\\scoring\\{OUT_FILE_NAME}"

with open(OUT_FILE_PATH, 'w') as convert_file:
     convert_file.write(json.dumps(scoring))
score_file = open(OUT_FILE_PATH)
scores = json.load(score_file)
print("Scores saved!")
