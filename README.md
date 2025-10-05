# Text Autocomplete Engine

A text autocomplete engine that suggests the most likely word completions for a given prefix. It uses the NLTK Brown corpus for word frequency information and a trie data structure for fast prefix lookup.

## Table of contents

- Overview
- How it works
- Features
- Requirements
- Setup
- Usage
- Project files
- Notes

## Overview

This project implements a simple autocomplete system that returns up to five suggested completions for a user's prefix input. Suggestions are ranked by frequency in the Brown corpus so more common words appear first.

## How it works

- The Brown corpus (from NLTK) is used to build a vocabulary and a frequency distribution of words.
- A trie stores every word from the corpus to allow efficient retrieval of all words that share a given prefix.
- When the user provides a prefix, the trie returns matched words which are then ranked using the frequency distribution (NLTK's `FreqDist`).
- The engine returns the top five (or fewer) most frequent completions. If no matches are found, an appropriate message is shown.

## Features

- Fast prefix lookup using a trie
- Frequency-based ranking using NLTK's Brown corpus
- Lightweight, easy to run locally

## Requirements

- Python 3.9 or newer
- pip
- virtual environment tooling such as `venv`
- NLTK and the Brown corpus data

## Setup

1. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install the required Python package:

```bash
pip install nltk
```

3. Check the installed nltk version

```bash
nltk --version
```

At the time this project was written, NLTK 3.9.2 was used; newer versions should also work, but if you see issues try using the same version.

## Usage

Start the autocomplete program with:

```bash
python3 driver.py
```

Follow the on-screen prompt to type a prefix and see up to five suggestions.


Example session (interactive):

```
> Enter a prefix (type 'exit' to quit): ac
Suggestions for 'ac': ['action', 'act', 'across', 'actually', 'according']
```

## Project files

- `driver.py` — Simple command-line driver that runs the interactive prompt.
- `textautocompleteengine.py` — Main engine: builds the trie and frequency data, exposes an API to request suggestions.
- `trie.py` — Trie implementation used for prefix lookups.
- `trienode.py` — Node implementation used by the trie.

## License & acknowledgements

This project uses the Natural Language Toolkit (NLTK) and the Brown corpus. See NLTK documentation for licensing details.

