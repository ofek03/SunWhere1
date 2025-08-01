from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Serve static files (optional)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templating
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def serve_map(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
