# PY LLM Lib
> :warning: **NOT** a working implementation: just an interview task

A small Python library designed to interact with Large Language Models.

## Setup instructions
### Prerequisites
- Python 3.8 or higher
- Docker (optional, to run tests in a containerized environment)

### Installing Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/lpezzolla/py-llm-lib.git
   cd py-llm-lib
   ```

2. (Optional) Create and activate a Python virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Using Docker
1. Build the Docker image:
   ```bash
   docker-compose build
   ```
2. Start the container:
   ```bash
   docker-compose up
   ```

## Running tests
### Locally
Run the test suite with `pytest`:
```bash
pytest --maxfail=1 --disable-warnings
```

### With Docker
Run tests inside the Docker container:
```bash
docker-compose up
```
By default, the `docker-compose.yml` file runs the test suite when the container starts.