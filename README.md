# AuralMind 2.0 - Project Scaffold

This scaffold contains code templates, LangGraph YAML, and a starter Jupyter notebook for the AuralMind 2.0 project:
A LangGraph-orchestrated cross-platform multimodal music intelligence system.

**What's inside:**
- `langgraph.yaml` - LangGraph-style agent definitions (pseudoyaml) and edges.
- `fastapi_app.py` - FastAPI skeleton with example endpoints and agent stubs.
- `streamlit_app.py` - Streamlit prototype UI (mock backend integration).
- `requirements.txt` - Python dependencies to install.
- `seed_data.py` - Example seeding script (placeholder; requires API keys to run).
- `utils.py` - Utility helpers (embeddings placeholders, audio feature stubs).
- `AuralMind_project.ipynb` - Jupyter notebook walkthrough and runnable code cells (where possible).
- `LICENSE` - MIT license template.

**Important:** This scaffold is a *developer starting point*. External API access (Spotify, YouTube, Genius, Tavily, Riffusion) requires your API keys and credentials. Audio processing (librosa, openl3) requires native libs that may need system-level packages.

See the notebook for step-by-step setup instructions and how to replace placeholders with your API keys.
