# FastAPI Benchmarking

This project is designed to facilitate benchmarking and comparison between FastAPI, Flask, and Go's Gin framework. It includes hands-on scripts to set up and run each framework in a local development environment.

## Getting Started

### Setting Up a Virtual Environment

Before running any Python-based frameworks, it's recommended to set up a virtual environment. This isolates your project dependencies and ensures that your development environment remains clean and manageable.

```bash
# Create a virtual environment
python3 -m venv myvenv

# Activate the virtual environment
source myvenv/bin/activate
```

### FastAPI

FastAPI is a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints. To set up FastAPI:

```bash
# Install FastAPI with all optional dependencies
pip install "fastapi[all]"

# Navigate to the FastAPI project directory
cd fastapi

# Start the FastAPI server with live reloading
uvicorn main:app --reload
```

### Flask

Flask is a lightweight WSGI web application framework. It's designed to make getting started quick and easy, with the ability to scale up to complex applications. For Flask setup:

```bash
# Navigate to the Flask project directory
cd flask

# Install Flask
pip install Flask

# Set the main application file for Flask to run
export FLASK_APP=main

# Start the Flask application
flask run
```

### Golang with Gin

Gin is a web framework written in Go (Golang). It features a Martini-like API with much better performance, up to 40 times faster. If you need smashing performance, get yourself some Gin. First, install Go from [https://go.dev/doc/install], then proceed with Gin setup:

```bash
# Navigate to the Go project directory
cd go

# Get the Gin package
go get -u github.com/gin-gonic/gin

# Run the main Go application
go run ./main.go
```
