import xml.etree.ElementTree as ET


# https://stackoverflow.com/a/28651261
def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16)
                 for i in range(0, lv, lv // 3)) + (255, )


sld = ET.parse('lito.sld')
sld_root = sld.getroot()
color_dict = {}

for child in sld_root[0][1][1]:
    try:
        color_dict[child[2][0][1].text] = child[3][0][0].text
    except:
        pass

qml = ET.parse('milionesimo.qml')
qml_root = qml.getroot()
symbol_key = {}

for child in qml_root[1][0]:
    symbol_key[child.attrib["symbol"]] = child.attrib["value"]

not_found = []

for i, child in enumerate(qml_root[1][1]):
    try:
        child[0][1].attrib["v"] = "{},{},{},{}".format(
            *hex_to_rgb(color_dict[symbol_key[child.attrib["name"]]]))
    except KeyError:
        child[0][1].attrib["v"] = "255,255,255,255"
        not_found.append(symbol_key[child.attrib["name"]])

with open("not_found.txt", "w") as f:
    f.write("\n".join(not_found))
qml.write('milionesimo_lito.qml')
print("Done. %i layers missing." % len(not_found))
