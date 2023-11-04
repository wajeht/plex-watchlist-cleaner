# Plex Watchlist Cleaner

## Setup

- Install Python 3.7 or higher.
- Create a virtual environment and activate it:
  - Unix: `python3 -m venv env` then `source env/bin/activate`
  - Windows: `python -m venv env` then `env\Scripts\activate`
- Install dependencies: `pip install -r requirements.txt`.

## Configuration

- Create a `.env` file with your Plex credentials:

```
PLEX_USERNAME=your_username
PLEX_PASSWORD=your_password
```

## Run

- Execute the script: `python index.py`.
