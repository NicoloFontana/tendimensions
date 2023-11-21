from transformers import pipeline, Conversation

converse = pipeline("conversational")
conversation_1 = Conversation("Going to the movies tonight - any suggestions?")
conversation_2 = Conversation("What's the last book you have read?")
out = converse([conversation_1, conversation_2])
print(out)
