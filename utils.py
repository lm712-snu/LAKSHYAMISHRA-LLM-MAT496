# Utility stubs for AuralMind - replace with real implementations when ready
import numpy as np

def fake_audio_embedding(duration_seconds=30):
    # returns a deterministic fake 'audio' embedding for testing (512-dim)
    rng = np.random.RandomState(42)
    return rng.rand(512).astype(float).tolist()

def fake_lyrics_embedding(text='sample lyrics'):
    rng = np.random.RandomState(sum(map(ord, text)) % 1000)
    return rng.rand(384).astype(float).tolist()
