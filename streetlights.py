import overpy
import mylib
api = overpy.Overpass()
import os
# fetch all ways and nodes
data = []
result = api.query("""
    way(41.5661,-88.4290,42.0992,-87.0337) ["lit"];
    (._;>;);
    out body;
    """)
counter = 0
for way in result.ways:
    print("Name: %s" % way.tags.get("name", "n/a")),
    print("lit: %s" % way.tags.get("lit", "n/a")),
    print("  Highway: %s" % way.tags.get("highway", "n/a"))
    print("  Nodes:")
    data.append([])
    data[counter].append("{}".format(way.tags.get("lit", "n/a")))
    data[counter].append("{}".format(way.tags.get("name", "n/a")))
    counter += 1
print(data[211])
mylib.AppendCSVs(os.path.join(os.getcwd(), 'lit.csv'), mylib.ConvertToDataFrame(Data=data, Columns=['a', 'b']))
    #for node in way.nodes:
    #    print(node)
    #    print("    Lat: %f, Lon: %f" % (node.lat, node.lon))
