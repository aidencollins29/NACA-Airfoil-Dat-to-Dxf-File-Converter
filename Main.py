cord = []

from pathlib import Path

directory = Path('DatFile')
for file_path in directory.glob('*.dat'):
    content = file_path.read_text(encoding='utf-8')

lines = content.splitlines()

for x in lines:
    result = x.strip()
    result = result.replace("  ", " ")

    cord.append(result)

for x in cord:
    notletter = any(char.isalpha() for char in x)
    if notletter:
        cord.remove(x)

cord = [word for item in cord for word in item.split()]




DXF = """0
SECTION
2
ENTITIES
0
POLYLINE
8
0
66
1
70
1
0
"""

for i in range(0, len(cord), 2):
    DXF += f"""VERTEX
8
0
10
{cord[i]}
20
{cord[i+1]}
30
0.0
0
"""


DXF += """SEQEND
0
ENDSEC
0
EOF
"""


with open("DxfFile/AirFoil.dxf", "w") as file:
    file.write(DXF)