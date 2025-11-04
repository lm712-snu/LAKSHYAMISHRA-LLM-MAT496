# seed_data.py - example seeding script that demonstrates how to index a small set of tracks locally.
# NOTE: This script uses fake embeddings and mock metadata. Replace with real API calls and embeddings.
import json, os
from utils import fake_audio_embedding, fake_lyrics_embedding
OUT='seed_tracks.json'
tracks = []
for i in range(1,21):
    t = {
        'track_uid': f'mock_{i:03d}',
        'title': f'Mock Song {i}',
        'artist': f'Artist {i%5}',
        'platform': 'mock_platform',
        'audio_embedding': fake_audio_embedding(),
        'lyrics_embedding': fake_lyrics_embedding(f"lyrics {i}"),
        'metadata': {'genre':'indie','popularity': 50 - i}
    }
    tracks.append(t)

with open(OUT,'w') as f:
    json.dump(tracks, f, indent=2)
print('Wrote', OUT)
