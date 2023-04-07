# Radiance-AI
Radiance-AI is an experimental, organically growing Artificial General Intelligence (AGI) project that leverages the Pinecone vector database for long-term relational self-referencing and utilizes OpenAI's NLP models in a sophisticated tiered agent structure for increased speed and reduced costs. The project's architecture is inspired by the Chunks and Rules Cognitive Agent Architecture found in W3C Cognitive Agent Architecture.

## Features
Pinecone vector database integration for efficient long-term memory storage and retrieval.
Advanced tiered agent structure that efficiently delegates tasks to OpenAI's NLP models based on length, difficulty, and complexity, resulting in faster processing and reduced operational costs.
Implements ideas from the Chunks and Rules Cognitive Agent Architecture to develop a more human-like understanding and reasoning capability.
Tiered Agent Structure
Radiance-AI's tiered agent structure is designed to maximize the efficiency of processing tasks while minimizing the costs associated with running large NLP models. The system intelligently delegates tasks to different models based on factors such as length, difficulty, and complexity. This approach enables Radiance-AI to achieve optimal performance while reducing the overall costs of running the program.

The tiered agent structure consists of the following components:

**Task Analyzer**: Analyzes incoming tasks and estimates their complexity, length, and difficulty.

**Model Selector**: Selects the appropriate NLP model from OpenAI's model suite (e.g., GPT-3, Codex) based on the analysis provided by the Task Analyzer.

**Task Executor**: Executes the task using the selected NLP model, retrieves the results, and returns them to the user or other components within the system.
By utilizing this tiered agent structure, Radiance-AI ensures that complex tasks are delegated to more powerful NLP models, while simpler tasks are handled by smaller, faster, and more cost-effective models.

## Getting Started
Prerequisites
Python 3.6+
Pinecone API key
OpenAI API key
## Installation
### Clone the repository:


```
git clone https://github.com/TopJimmies/Radiance-AI.git
```
### Install the required Python packages:

```
cd radiance-ai
pip install -r requirements.txt
```
### Set up your Pinecone and OpenAI API keys as environment variables:

```
export PINECONE_API_KEY=your_pinecone_api_key
export OPENAI_API_KEY=your_openai_api_key
```
## Usage
After setting up the environment, you can use the Radiance-AI system to store, retrieve, and process information using its advanced tiered agent structure and Pinecone-powered memory.

Check the provided examples and documentation for more information on how to use Radiance-AI's features.

## Contributing
Radiance-AI is an open-source project, and we welcome contributions from the community. If you'd like to contribute, please follow these steps:

Fork the repository.
Create a new branch for your changes.
Make your changes and commit them to your branch.
Open a pull request with a detailed description of your changes.
Please make sure to follow the code style guidelines and include tests for any new features or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
The Radiance-AI project is inspired by the W3C Cognitive Agent Architecture.
Special thanks to Pinecone for providing an efficient vector database solution.
Gratitude
