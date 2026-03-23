
import geopandas as gpd
from shapely.geometry import box

def generate_layout(gdf):
    poly = gdf.geometry.iloc[0]
    minx,miny,maxx,maxy = poly.bounds
    panels=[]
    x=minx
    while x<maxx:
        y=miny
        while y<maxy:
            p=box(x,y,x+1,y+2)
            if poly.contains(p):
                panels.append({"geometry":p})
            y+=4
        x+=3
    return gpd.GeoDataFrame(panels, crs=gdf.crs)
