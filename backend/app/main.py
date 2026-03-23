
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import geopandas as gpd
import tempfile, os, shutil
from app.services.layout import generate_layout
from app.services.export import export_kmz, export_dxf

app = FastAPI()

@app.get("/")
def root():
    return {"msg":"running"}

@app.post("/layout/")
async def layout(file: UploadFile = File(...)):
    tmp = tempfile.mkdtemp()
    path = os.path.join(tmp, file.filename)
    with open(path,"wb") as f: shutil.copyfileobj(file.file,f)
    gdf = gpd.read_file(path).to_crs(epsg=3857)
    layout = generate_layout(gdf)
    return {"layout": layout.to_json()}

@app.post("/export/kmz/")
async def kmz(file: UploadFile = File(...)):
    tmp = tempfile.mkdtemp()
    path = os.path.join(tmp, file.filename)
    with open(path,"wb") as f: shutil.copyfileobj(file.file,f)
    gdf = gpd.read_file(path).to_crs(epsg=3857)
    layout = generate_layout(gdf)
    out = os.path.join(tmp,"layout.kmz")
    export_kmz(layout,out)
    return FileResponse(out, filename="layout.kmz")

@app.post("/export/dxf/")
async def dxf(file: UploadFile = File(...)):
    tmp = tempfile.mkdtemp()
    path = os.path.join(tmp, file.filename)
    with open(path,"wb") as f: shutil.copyfileobj(file.file,f)
    gdf = gpd.read_file(path).to_crs(epsg=3857)
    layout = generate_layout(gdf)
    out = os.path.join(tmp,"layout.dxf")
    export_dxf(layout,out)
    return FileResponse(out, filename="layout.dxf")
