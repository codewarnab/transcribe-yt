from fastapi import FastAPI
from youtube_transcript_api import YouTubeTranscriptApi

app = FastAPI()

@app.get("/")
async def home_root():
    return {"message": "Hello World"}


@app.get("/transcript/{video_id}")
async def get_transcript(video_id: str):
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = " ".join([item['text'] for item in transcript_list])
        return {"transcript": transcript}
    except Exception as e:
        return {"error": str(e)}