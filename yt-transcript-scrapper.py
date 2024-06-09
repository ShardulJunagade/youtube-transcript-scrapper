from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
import scrapetube
import os

# Enter the Youtube Channel ID
channel_id = ""

# Enter the name of the txt file to be saved
file_name = ""

# Enter the path of the folder to save the txt file
folder_path = ""

# Enter the language code
language_code = ""

# Ensure the folder path exists
os.makedirs(folder_path, exist_ok=True)

def extract_title(video):
    """Extract the video title from the video dictionary."""
    title_runs = video.get("title", {}).get("runs", [])
    if title_runs:
        return "".join([run.get("text", "") for run in title_runs])
    return "No title found"

def fetch_transcript(video_id):
    """Fetch the transcript for a given video ID, attempting different languages and translations."""
    try:
        # Try to get the transcript in Marathi
        return YouTubeTranscriptApi.get_transcript(video_id, languages=[language_code])
    except Exception:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        for lang in ["en", "en-US", "hi"]:
            try:
                transcript = transcript_list.find_transcript([lang])
                translated_transcript = transcript.translate(language_code)
                return translated_transcript.fetch()
            except Exception:
                continue
        raise Exception("No subtitles found")

def save_transcripts(channel_id, folder_path, file_name):
    """Save transcripts of all videos from a given YouTube channel to a text file."""
    videos = scrapetube.get_channel(channel_id)
    with open(os.path.join(folder_path, f"{file_name}.txt"), "a+", encoding="utf-8") as txt_file:
        for video in videos:
            video_id = video["videoId"]
            video_title = extract_title(video)
            try:
                transcript = fetch_transcript(video_id)
                formatter = TextFormatter()
                txt_formatted = formatter.format_transcript(transcript)
                txt_file.write(f"Title: {video_title}\n")
                txt_file.write(txt_formatted + "\n\n")
                print(f'Success! Transcript for video "{video_title}" saved.')
            except Exception:
                print(f'Subtitles not found for video "{video_title}".')

if __name__ == "__main__":
    save_transcripts(channel_id, folder_path, file_name)
