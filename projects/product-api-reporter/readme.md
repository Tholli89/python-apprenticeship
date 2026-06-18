# Product API Reporter

A Python project that fetches product data from an external API, summarizes the results, and exposes the summary through a FastAPI endpoint.

## Purpose

This project builds on earlier JSON and CSV work by introducing live HTTP requests and a first local web API. The goal is to keep business logic separate from networking and routing.

## Features

- Fetch product data from Fake Store API
- Parse JSON responses with `requests`
- Normalize product data into a clean internal structure
- Summarize product prices and categories
- Test summary logic with pytest
- Expose a `/summary` endpoint with FastAPI
- Use Swagger UI at `/docs` for interactive testing

## Summary data produced

The project reports:

- Total products
- Average price
- Highest price
- Lowest price
- Total value
- Product counts by category

## Concepts practiced

- HTTP requests with `requests`
- JSON parsing
- Pure summary functions
- Testing with pytest
- FastAPI basics
- Uvicorn server startup
- Returning JSON from endpoints
- Reusing logic across CLI and API layers

## File structure

Typical files:

- `main.py`
- `summary.py`
- `test_summary.py`
- `api.py`

## How to run

Run tests:

```bash
python -m pytest -v
```

Run the CLI report:

```bash
python main.py
```

Run the FastAPI server:

```bash
python -m uvicorn api:app --reload
```

Then open:

```text
http://127.0.0.1:8000/docs
```

## Why this project matters

This is the first project in the apprenticeship that behaves like a real backend service. It consumes external API data, applies business logic, and serves a JSON response from a local endpoint.