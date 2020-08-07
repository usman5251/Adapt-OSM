import overpy
import mylib
api = overpy.Overpass()
import os
# fetch all ways and nodes
result = api.query("""
    way(41.5661,-88.4290,42.0992,-87.0337) ["maxspeed"];
    (._;>;);
    out body;
    """)

for way in result.ways:
    print("Name: %s" % way.tags.get("name", "n/a")),
    print("maxspeed: %s" % way.tags.get("maxspeed", "n/a")),
    print("  Highway: %s" % way.tags.get("highway", "n/a"))
    print("  Nodes:")
    print(way.tags)
    mylib.AppendCSVs(os.path.join(os.getcwd(), 'maxspeed.csv'), mylib.ConvertToDataFrame(Data=[way.tags.get("maxspeed", "n/a"),way.tags.get("name", "n/a")], Columns=['a', 'b']))
    for node in way.nodes:
        print(node)
    #    print("    Lat: %f, Lon: %f" % (node.lat, node.lon))
