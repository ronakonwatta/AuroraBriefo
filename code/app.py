from flask import Flask, request, jsonify, render_template
from transformers import pipeline

app = Flask(__name__)

# Load the summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Summarization route with error handling
@app.route('/summarize', methods=['POST'])
def summarize():
    try:
        # Debugging: Check if request is properly received
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data received'}), 400

        document = data.get('document')
        summary_length = data.get('summary_length')

        # Debugging: Check if required fields are present
        if not document or not summary_length:
            return jsonify({'error': 'Document or summary length is missing!'}), 400

        # Define summary length settings
        length_settings = {
            'short': {'max_length': 50, 'min_length': 10},
            'medium': {'max_length': 130, 'min_length': 30},
            'detailed': {'max_length': 200, 'min_length': 80}
        }

        # Check if summary length is valid
        if summary_length not in length_settings:
            return jsonify({'error': 'Invalid summary length!'}), 400

        max_len = length_settings[summary_length]['max_length']
        min_len = length_settings[summary_length]['min_length']

        # Generate the summary using the model
        summary = summarizer(document, max_length=max_len, min_length=min_len, do_sample=False)

        # Debugging: Return the summary
        return jsonify({'summary': summary[0]['summary_text']})

    except Exception as e:
        # Log the error and return an error response
        print(f"Error: {e}")  # This will print the error to the console/terminal
        return jsonify({'error': 'An error occurred during summarization!'}), 500

if __name__ == '__main__':
    app.run(debug=True)
