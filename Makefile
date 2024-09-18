# Makefile for AuroraBriefo

# Variables
PYTHON = python3
PIP = pip3
APP = code/app.py
TEST = code/test_app.py
REQUIREMENTS = requirements.txt

# Set PYTHONPATH to include the code directory
export PYTHONPATH := $(PYTHONPATH):./code

# Install dependencies
install:
	$(PIP) install -r $(REQUIREMENTS)

# Run the Flask app
run:
	$(PYTHON) $(APP)

# Run the unit tests
test:
	$(PYTHON) -m unittest $(TEST)

# Clean up Python cache files
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete

# Lint the Python code
lint:
	flake8 .

# Help
help:
	@echo "Makefile commands:"
	@echo "  install   - Install Python dependencies"
	@echo "  run       - Run the Flask app"
	@echo "  test      - Run unit tests"
	@echo "  clean     - Clean up Python cache files"
	@echo "  lint      - Lint the code using flake8"
	@echo "  help      - Show this help message"
