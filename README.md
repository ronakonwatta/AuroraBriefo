
# AuroraBriefo

**AuroraBriefo** is an AI-powered tool designed to help businesses summarize lengthy and complex documents into clear, concise insights, allowing for faster and more informed decisions.

## Description

AuroraBriefo leverages state-of-the-art Natural Language Processing (NLP) models to transform lengthy reports, legal documents, and other business materials into short, actionable insights. By summarizing essential information, the tool streamlines decision-making processes and boosts productivity for enterprise users.

### Key Features:
- Customizable summary length options (short, medium, detailed).
- Fast and accurate, powered by the **BART** model from Hugging Face's Transformers library.
- Summarizes various types of business documents with ease.

## Getting Started

### Prerequisites

To run **AuroraBriefo**, ensure you have the following installed:
- Python 3.x
- Flask
- Hugging Face Transformers
- PyTorch

### Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd aurorabriefo
   ```

2. **Install dependencies:**

   Install the necessary Python packages by running:

   ```bash
   pip3 install -r requirements.txt
   ```

3. **Run the application:**

   Start the Flask server by running:

   ```bash
   python3 code/app.py
   ```

4. **Run Unit Tests:**

   To run the unit tests, use:

   ```bash
   python3 -m unittest code/test_app.py
   ```

5. **Access the app:**

   Open your browser and navigate to `http://<your-server-ip>:5000` to use the AuroraBriefo web interface for summarizing documents.

## Usage

1. **Input the Document:**
   - On the main page, paste your document into the provided text area.

2. **Choose Summary Length:**
   - Select from **Short**, **Medium**, or **Detailed** summary length options depending on the level of detail required.

3. **Get Summary:**
   - Click **Summarize** to generate a summary. The result will be displayed instantly on the same page.

## Project Structure

Here’s the updated project structure:

```plaintext
AuroraBriefo/
│
├── Makefile              # Commands for installing, testing, and running the app
├── README.md             # Project documentation (this file)
├── apt.txt               # List of system dependencies for apt-get
├── code/                 # Code directory
│   ├── Untitled.ipynb    # Jupyter notebook (if needed)
│   ├── app.ipynb         # Main application notebook
│   ├── app.py            # Flask app
│   ├── templates/        # Directory for HTML files
│   │   └── index.html    # Main HTML file
│   └── test_app.py       # Unit tests for the app
├── data/                 # Directory for storing datasets or outputs
│   └── scratch/          # Sub-directory for temporary data
├── models/               # Directory for model-related files
├── postBuild.bash        # Post-build script (optional)
├── preBuild.bash         # Pre-build script (optional)
├── requirements.txt      # Python dependencies for the project
└── variables.env         # Environment variables file
```

## Built With

- [Flask](https://flask.palletsprojects.com/) - Web framework for Python.
- [Hugging Face Transformers](https://huggingface.co/transformers/) - NLP models for text summarization.
- [PyTorch](https://pytorch.org/) - Deep learning framework used to run the NLP models.

## Contributing

We welcome contributions to improve AuroraBriefo. Please follow these steps for contributing:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`.
3. Commit your changes: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature/your-feature-name`.
5. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, reach out to **Ronakon Wattanamongkolchoke** at [your-email@example.com].
