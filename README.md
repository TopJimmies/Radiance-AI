# Radiance AI - NLP Task Subtask Generation and Embedding
Radiance AI is a powerful Python script that uses OpenAI GPT-3 and Pinecone to automatically generate subtasks for a given NLP task, categorize them, and store their embeddings in a Pinecone index. This tool is perfect for researchers, data scientists, and developers working on NLP projects who need to break down high-level tasks into manageable subtasks and store them efficiently for future use.

## Features
**Subtask Generation**: Given an NLP task, Radiance AI uses OpenAI's GPT-3 engine (text-davinci-002) to generate a numbered list of subtasks required to complete the task.
**Subtask Categorization**: For each generated subtask, Radiance AI utilizes GPT-3 (text-curie-001) to automatically categorize it into one of several predefined NLP categories.
**Embedding Generation**: Radiance AI generates embeddings for each subtask using OpenAI's text-embedding-ada-002.
**Pinecone Index Storage**: All subtasks, along with their categories and embeddings, are stored in a Pinecone index for efficient retrieval and future use.
**Logging**: The generated subtasks and their categories are logged in an output.txt file.

## Use Case
Radiance AI is designed for users who need to break down complex NLP tasks into smaller, more manageable subtasks. With its automated subtask generation, categorization, and embedding capabilities, users can save time and focus on implementing the core functionality of their NLP projects.

## Getting Started
### Prerequisites
Python 3.6+
Pinecone: 'pip install pinecone-client'
OpenAI: 'pip install openai'
API Keys
Make sure to set up your Pinecone and OpenAI API keys before running the script.

```
pinecone.init(api_key="your-pinecone-key", environment="your-pinecone-environment")
openai.api_key = "your-openai-key"
```
## Running the Script
Clone this repository and navigate to the project directory.
Run python radiance_ai.py and enter your NLP task when prompted.
The script will generate subtasks, categorize them, and store them in the Pinecone index.
The generated subtasks and their categories will be logged in an output.txt file.
## License
This project is licensed under the MIT License - see the LICENSE file for details.