import streamlit as st
import requests

API_URL = st.sidebar.text_input('API URL', 'http://localhost:8000')

st.title('AuralMind 2.0 - Prototype UI')

mode = st.selectbox('Mode', ['recommend', 'search', 'analyze', 'generate'])
query = st.text_input('Your query or prompt')

if st.button('Send'):
    with st.spinner('Contacting backend...'):
        try:
            resp = requests.post(API_URL + '/api/v1/search', json={'user_id':'test','query':query,'mode':mode}, timeout=15)
            data = resp.json()
            payload = data.get('payload', {})
            cards = payload.get('cards', [])
            st.success(f"Received {len(cards)} results")
            for c in cards:
                st.subheader(c['title'] + ' — ' + c['artist'])
                st.write('Platform:', c['platform'])
                st.write('Why:', c.get('explanation',''))
        except Exception as e:
            st.error(f'Error: {e}')
