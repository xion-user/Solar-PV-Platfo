
import simplekml, ezdxf

def export_kmz(gdf, path):
    kml = simplekml.Kml()
    for _,r in gdf.iterrows():
        coords=list(r.geometry.exterior.coords)
        pol=kml.newpolygon(outerboundaryis=coords)
    kml.save(path)

def export_dxf(gdf, path):
    doc=ezdxf.new()
    msp=doc.modelspace()
    for _,r in gdf.iterrows():
        coords=list(r.geometry.exterior.coords)
        msp.add_lwpolyline(coords)
    doc.saveas(path)
