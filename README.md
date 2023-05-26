# AthenaSynth

AthenaSynth is an AI alignment experiment that generates responses to user questions based on the ethical perspective of Aristotle, the moral philosophy of Immanuel Kant, and the focus on reason from René Descartes. It uses OpenAI's GPT-3.5-turbo model to provide synthesized answers to questions, taking into account the context and summaries of the works of these philosophers.

## Installation

1. Ensure you have Python 3.6 or later installed.
2. Install the `openai` package using pip:

```bash
pip install openai
```

3. Get an API key from OpenAI and set it as an environment variable or store it in a `.env` file in the same directory as the script.

```
OPENAI_API_KEY=your_api_key_here
```

## Usage

1. Replace the example documents with your actual texts for Aristotle, Kant, and Descartes in the `document_aristotle`, `document_kant`, and `document_descartes` variables in the script.
2. Run the script:

```bash
python your_script_name.py
```

3. Enter your question when prompted.
4. The script will generate responses that consider the ethical perspective of Aristotle, the moral philosophy of Immanuel Kant, and the focus on reason from René Descartes, and then provide a synthesized answer.
5. The background responses of the three philosophers will be saved to a text file named `background_responses.txt`.
6. Type 'exit' or 'quit' to end the conversation.

## How it works

The script uses OpenAI's GPT-3.5-turbo to generate synthesized answers to questions. It first generates responses from Aristotle, Kant, and Descartes based on their summarized documents as context. These responses are saved to a file named `background_responses.txt`.

Next, the script generates a final response that considers the ethical perspective of Aristotle, the moral philosophy of Immanuel Kant, and the focus on reason from René Descartes. This response is provided to the user as the AI agent's synthesized answer.

## Contributing

If you'd like to contribute to this project, feel free to submit a pull request or open an issue for discussion.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
