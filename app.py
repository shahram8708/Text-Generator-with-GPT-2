from flask import Flask, render_template, request, jsonify
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

app = Flask(__name__)

tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

MAX_LENGTH = 150
NUM_RETURN_SEQUENCES = 1
TEMPERATURE = 0.7

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    prompt = data['prompt']

    inputs = tokenizer(prompt, return_tensors='pt')

    outputs = model.generate(
        input_ids=inputs['input_ids'],
        max_length=MAX_LENGTH,
        num_return_sequences=NUM_RETURN_SEQUENCES,
        temperature=TEMPERATURE,
        pad_token_id=tokenizer.eos_token_id
    )

    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return jsonify({'text': generated_text})

if __name__ == '__main__':
    app.run(debug=True)
