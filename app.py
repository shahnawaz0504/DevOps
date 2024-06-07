from fastapi import FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse, FileResponse#, StreamingResponse

app = FastAPI()

@app.get('/')
def index():
    return {'hello': 'raand'}

@app.get('/script', response_class=HTMLResponse)
def read_root():
    return '<script>alert("This is JS")</script>'

@app.get('/amazon', response_class=RedirectResponse)
def redirect():
    return 'https://www.amazon.com'

@app.get("/video", response_class=FileResponse)
async def video():
    return '/Users/asadullahshaikh/Downloads/WhatsApp Video 2024-05-15 at 19.42.41.mp4'

@app.get("/jinit", response_class=FileResponse)
async def jinit():
    return '/Users/asadullahshaikh/Downloads/20240607_080318.jpg'

# @app.get("/")
# def main():
#     def iterfile():
#         with open(video_path, mode="rb") as file:
#             yield from file

#     return StreamingResponse(iterfile(), media_type="video/mp4")