import pinecone
import openai
import numpy as np

# set your Pinecone API key as an environment variable
pinecone.init(api_key="your-pinecone-key",environment="your-pinecone-environment")
openai.api_key = "your-openai-key"


# check that the Pinecone Index 'radiance-ai' exists
index_list = pinecone.list_indexes()
if ("radiance-ai" not in index_list):
    print("radiance-ai index NOT found. Please add the index to your Pinecone account.")
    break
else:
    print("radiance-ai index found")
    index = pinecone.Index("radiance-ai")

nlp_task = input('Give me a task: ')
nlp_task_prompt = f'Give me a numbered list of tasks to complete the following: {nlp_task}'

completions = openai.Completion.create(
    engine='text-davinci-002',
    prompt=nlp_task_prompt,
    max_tokens=1000,
    n=1,
    stop=None,
    temperature=0.7,
    )

subtasks = completions.choices[0].text.strip().split("\n")

logfile = open("output.txt","w")
logfile.write(nlp_task_prompt + "\n")
for i in subtasks:
    logfile.write(i + "\n")
    print(i)

for i in subtasks:
    if i == " " or i == "\n" or i == " \n" or i == "\n ":
        print("empty subtask")
        continue
    text = [f'Categorize the following task into one of these types (parsing text, reformatting text, classification, semantic search, summarization, sentiment analysis, chatting, logic problem, cause effect, text intention, complex summarization, coding, other): "{i}" \nThis task would be categorized as ']
    completions = openai.Completion.create(
        engine='text-curie-001',
        prompt=text,
        max_tokens=10,
        n=1,
        stop=None,
        temperature=0.7,
        )
    category = completions.choices[0].text

    prompt = [f"Embed the following text: '{i}'"]
    embed = openai.Embedding.create(
        input = prompt,
        model = "text-embedding-ada-002"
    )

    embedding = embed['data'][0]['embedding']

    try:
        index.upsert( namespace="radiance-ai", vectors=[ {"id": i , "metadata": {"category": category }, "values": embedding }] )
    except:
        print("invalid upsert")
    logfile.write(category)
    print(category)

print(f"test successful, {len(subtasks)} vectors written to file and database")