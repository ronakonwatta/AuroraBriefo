from flask import Flask, request, jsonify, render_template
from transformers import pipeline
import os

# Initialize Flask app
app = Flask(__name__)

# Load the summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Function to summarize a single document
def summarize_document(document, max_length=130, min_length=30):
    summary = summarizer(document, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']

# Route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for summarizing documents
@app.route('/summarize', methods=['POST'])
def summarize():
    if request.method == 'POST':
        # Get document and summary length from form input
        document = request.form['document']
        summary_length = request.form['summary_length']
        
        # Define length parameters
        length_settings = {
            'short': {'max_length': 50, 'min_length': 10},
            'medium': {'max_length': 130, 'min_length': 30},
            'detailed': {'max_length': 200, 'min_length': 80}
        }

        max_len = length_settings[summary_length]['max_length']
        min_len = length_settings[summary_length]['min_length']

        # Generate summary
        summary = summarize_document(document, max_length=max_len, min_length=min_len)

        return jsonify({'summary': summary})

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
