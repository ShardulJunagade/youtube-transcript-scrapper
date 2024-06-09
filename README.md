# YouTube Transcript Scraper

Automated script to fetch and save transcripts of all videos from a specified YouTube channel in a chosen language.

## Features

- Extracts video transcripts from a specified YouTube channel.
- Attempts to fetch transcripts in the specified language.
- If unavailable, tries to translate transcripts from available languages.
- Saves transcripts along with video titles to a specified folder in a text file.

## Requirements

- Python 3.x
- `youtube-transcript-api` library
- `scrapetube` library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/ShardulJunagade/youtube-transcript-scrapper.git
    cd youtube-transcript-scrapper
    ```

2. Install the required packages:
    ```sh
    pip install youtube-transcript-api scrapetube
    ```

## Usage

1. Set the following variables in the script:

    - `channel_id`: The YouTube Channel ID from which you want to fetch transcripts.
    - `file_name`: The name of the text file to save the transcripts.
    - `folder_path`: The path of the folder to save the text file.
    - `language_code`: The language code for the transcripts.

2. Run the script:
    ```sh
    python yt-transcript-scrapper.py
    ```

## Example

To fetch transcripts from TED's YouTube channel and save them in Marathi:

```python
channel_id = "UCAuUUnT6oDeKwE6v1NGQxug"
file_name = "ted"
folder_path = "Transcripts"
language_code = "mr"

## Rest of the code.

# Run the script
save_transcripts(channel_id, folder_path, file_name)
