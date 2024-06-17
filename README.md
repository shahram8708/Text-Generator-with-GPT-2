# Text Generation with GPT-2 and Flask

This project demonstrates a web application built with Flask that utilizes the GPT-2 model from Hugging Face's `transformers` library to generate text based on user prompts. It provides a user-friendly interface where users can input a prompt, and the model generates coherent text as a response.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Credits](#credits)
- [License](#license)

## Overview

This application integrates a pre-trained GPT-2 model with a Flask web server to offer a simple yet powerful text generation tool. It leverages the capabilities of the `transformers` library from Hugging Face for natural language processing tasks.

The key features include:
- Input a prompt through a web form.
- Generate text responses using a fine-tuned GPT-2 model.
- Display the generated text with a scrollable interface for longer outputs.

## Installation

Follow these steps to set up the project locally:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/shahram8708/Text-Generator-with-GPT-2.git
   cd text-generation-flask
   ```

2. **Set up a virtual environment:**

   It's recommended to use a virtual environment to manage dependencies. If you're using `venv`:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

   This will install Flask, torch, transformers, and other necessary packages.

4. **Download pre-trained GPT-2 model:**

   Ensure you have the GPT-2 model and tokenizer from Hugging Face. You can download them using:

   ```bash
   python -c "from transformers import GPT2LMHeadModel, GPT2Tokenizer; tokenizer = GPT2Tokenizer.from_pretrained('gpt2'); model = GPT2LMHeadModel.from_pretrained('gpt2')"
   ```

   This command will download the model and tokenizer into your environment.

## Usage

1. **Run the Flask application:**

   Start the Flask development server:

   ```bash
   python app.py
   ```

   By default, the application will be accessible at `http://localhost:5000`.

2. **Access the application:**

   Open a web browser and navigate to `http://localhost:5000`.

3. **Generate text:**

   - Enter a prompt in the text area provided.
   - Click on the **Generate Text** button.
   - The generated text will appear in the scrollable text box below.

## Project Structure

The project structure is organized as follows:

```
text-generation-flask/
│
├── app.py               # Flask application code
├── static/
│   └── styles.css       # CSS for styling the web interface
├── templates/
│   └── index.html       # HTML template for the web interface
├── README.md            # Project README file
└── requirements.txt     # Python dependencies
```

## Credits

- **GPT-2 Model**: OpenAI's GPT-2 model trained by Hugging Face.
- **Flask**: Web framework for Python.
- **transformers**: Library by Hugging Face for NLP tasks.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
