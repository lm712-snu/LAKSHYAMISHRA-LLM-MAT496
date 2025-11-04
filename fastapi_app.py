from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI(title='AuralMind 2.0 - API (skeleton)')

class SearchRequest(BaseModel):
    user_id: str
    query: str
    mode: str = 'recommend'  # 'search'|'analyze'|'generate'|'recommend'

@app.post('/api/v1/search')
async def search(req: SearchRequest):
    # NOTE: This is a skeleton. Replace with actual LangGraph orchestration calls.
    # For now we return a mock response to let the frontend prototype work.
    if not req.query:
        raise HTTPException(status_code=400, detail='Empty query')
    # Mock payload
    payload = {
        'cards': [
            {'title':'Mock Song A', 'artist':'Artist X', 'platform':'Spotify', 'preview_url':None, 'explanation':'Matches mood and tempo.'},
            {'title':'Mock Song B', 'artist':'Artist Y', 'platform':'YouTube', 'preview_url':None, 'explanation':'Similar lyrical theme.'},
        ],
        'playlist_id': 'mock_playlist_001'
    }
    return {'session_id':'mock_session_123','payload':payload}

@app.post('/api/v1/analyze')
async def analyze(req: dict):
    # Placeholder analysis endpoint
    return {'analysis':{'title':'Mock Song','bpm':80,'mood':'melancholic','lyrics_summary':'A short narrative about loss.'}}

@app.post('/api/v1/generate')
async def generate(req: dict):
    # Placeholder generation endpoint
    return {'audio_url':None, 'metadata': {'prompt': req.get('prompt','') } }

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
