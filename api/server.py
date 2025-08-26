from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pathlib import Path
import json

app = FastAPI(debug=True)
TOOLS_FOLDER = Path("api/tools/")


def is_inside_folder(path: Path, folder: Path):
    folder_str = str(folder.resolve().absolute())
    path_str = str(path.resolve().absolute())
    return path_str.startswith(folder_str)


@app.get("/api/tools/{path}")
async def get_tools(path: str):
    path: Path = TOOLS_FOLDER / path / "tools.json"
    if not path.exists() or not is_inside_folder(path, TOOLS_FOLDER):
        raise HTTPException(status_code=404, detail="Resource does not exist")
    with open(path, "r") as f:
        return JSONResponse(content=json.load(f))
