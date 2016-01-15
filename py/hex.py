# File:
# Desc:

import math;

# param: hType, hexType, 0 for Flat topped, 30 if Pointy topped
# param: center, Vector2Point, hex center
# param: radius, size of hex
# param: index, indexPoint corner of hex, 0-5
# returns: Vector2Point hex corner
def GeneratePointHEX(hType, center, radius, index):
	vec[0];
	angle_deg = 60 * index + hType; # 0 if Flat, 30 if Pointy
	angle_rad = math.pi / 180 * angle_deg;
	vec[0].x = center.x + size * cos(angle_rad);
	vec[0].y = center.y + size * sin(angle_rad);
	return vec;

# param: hType, hexType, 0 for Flat topped, 30 if Pointy topped
# param: center, Vector2Point, hex center
# param: radius, size of hex
# returns: Vector2[] hex corners
def GenerateVectorsHEX(hType, center, radius):
	vec[0];
	for val in range(6):
		angle_deg = 60 * val + hType; # 0 if Flat, 30 if Pointy
		angle_rad = math.pi / 180 * angle_deg;
		vec[val].x = center.x + size * cos(angle_rad);
		vec[val].y = center.y + size * sin(angle_rad);
	return vec;
  

def PrintInfo():
	print "=====[[ Hexagons ]]=====";
	print "(00) Definitons, Equations, ";
	print "(01) Storage, Tables, "
	print "(02) Generation, ";
	return;


# HexEdges, Indices
# A 0,1;
# B 1,2;
# C 2,3;
# D 3,4;
# E 4,5;
# F 5,0;

# HexTriangles, Indices (Index 6 as Center)
# A 6,0,1;
# B 6,1,2;
# etc

# Triangle Fan -> Center(0),First(1),Second(2), ...

# Hexagon area:
# A = ((3 sqrt 3) / 2 ) size^2
# Perimeter: 6 * size
# Slices 60 deg, 60 deg, 60 deg
# Total internal angles: 720 deg
# Internal angle: 120 deg
# 

dirs:
flat
Lines: East, SouthEast, SouthWest, West, NorthWest, NorthEast
Edges: SouthEast, South, SouthWest, NorthWest, North, NorthEast
pointy
Lines: SouthEast, South, SouthWest, NorthWest, North, NorthEast
Edges: East, SouthEast, SouthWest, West, NorthWest, NorthEast


# Unicode Character 'WHITE HEXAGON' (U+2B21)
# HTML Entity (decimal)                 &#11041;
# HTML Entity (hex)                     &#x2b21;
# How to type in Microsoft Windows      Alt +2B21
# UTF-8 (hex)                           0xE2 0xAC 0xA1 (e2aca1)
# UTF-8 (binary)                        11100010:10101100:10100001
# UTF-16 (hex)                          0x2B21 (2b21)
# UTF-16 (decimal)                      11,041
# UTF-32 (hex)                          0x00002B21 (2B21)
# UTF-32 (decimal)                      11,041
# C/C++/Java source code                "\u2B21"
# Python source code                    u"\u2B21"

# Unicode Character 'BLACK HEXAGON' (U+2B22)
# HTML Entity (decimal)                 &#11042;
# HTML Entity (hex)                     &#x2b22;
# How to type in Microsoft Windows      Alt +2B22
# UTF-8 (hex)                           0xE2 0xAC 0xA2 (e2aca2)
# UTF-8 (binary)                        11100010:10101100:10100010
# UTF-16 (hex)                          0x2B22 (2b22)
# UTF-16 (decimal)                      11,042
# UTF-32 (hex)                          0x00002B22 (2b22)
# UTF-32 (decimal)                      11,042
# C/C++/Java source code                "\u2B22"
# Python source code                    u"\u2B22"











# hex grid flat, vertical orientation
# Width = HexSize * 2
# horiz = width * 3/4
# height = sqrt(3)/2 * width.
# dist vertical = height.

# hex grid pointy, horizontal orientation
# height = hxsize * 2
# vert = height * 3/4
# width = sqrt(3)/2 * height.
# dist horiz = width.

offset coords
# Pointy top                         Pointy top
# "odd-r" Horizontal layout          "even-r" Horizontal layout
# (0,0) (1,0) (2,0) (3,0) (4,0)	        (0,0) (1,0) (2,0) (3,0) (4,0)
#    (0,1) (1,1) (2,1) (3,1) (4,1)   (0,1) (1,1) (2,1) (3,1) (4,1)
# (0,2) (1,2) (2,2) (3,2) (4,2)         (0,2) (1,2) (2,2) (3,2) (4,2)
#    (0,3) (1,3) (2,3) (3,3) (4,3)   (0,3) (1,3) (2,3) (3,3) (4,3)
# (0,4) (1,4) (2,4) (3,4) (4,4)         (0,4) (1,4) (2,4) (3,4) (4,4)

# Flat top                 Flat top
# "odd-q" Vertical layout  "even-q" Vertical layout
# (0,0) (2,0) (4,0)           (1,0) (3,0) (5,0)
#    (1,0) (3,0) (5,0)     (0,0) (2,0) (4,0)
# (0,1) (2,1) (4,1)           (1,1) (3,1) (5,1)
#    (1,1) (3,1) (4,1)     (0,1) (2,1) (4,1)
# (0,2) (2,2) (4,2)           (1,2) (3,2) (5,2)
#    (1,2) (3,2) (5,2)     (0,2) (2,2) (4,2)


cube coords
axial coords	
interlaced/doubled coords

Coord conversions::

function cube_to_hex(h): # axial
    var q = h.x
    var r = h.z
    return Hex(q, r)

function hex_to_cube(h): # axial
    var x = h.q
    var z = h.r
    var y = -x-z
    return Cube(x, y, z)
    
# convert cube to even-q offset
col = x
row = z + (x + (x&1)) / 2

# convert even-q offset to cube
x = col
z = row - (col + (col&1)) / 2
y = -x-z

# convert cube to odd-q offset
col = x
row = z + (x - (x&1)) / 2

# convert odd-q offset to cube
x = col
z = row - (col - (col&1)) / 2
y = -x-z

# convert cube to even-r offset
col = x + (z + (z&1)) / 2
row = z

# convert even-r offset to cube
x = col - (row + (row&1)) / 2
z = row
y = -x-z

# convert cube to odd-r offset
col = x + (z - (z&1)) / 2
row = z

# convert odd-r offset to cube
x = col - (row - (row&1)) / 2
z = row
y = -x-z
	

NEIGHBOURS::
>>cube<<

var directions = [
   Cube(+1, -1,  0), Cube(+1,  0, -1), Cube( 0, +1, -1),
   Cube(-1, +1,  0), Cube(-1,  0, +1), Cube( 0, -1, +1)
]

function cube_direction(direction):
    return directions[direction]

function cube_neighbor(hex, direction):
    return cube_add(hex, cube_direction(direction))
    

    
>>axial<<

var directions = [
   Hex(+1,  0), Hex(+1, -1), Hex( 0, -1),
   Hex(-1,  0), Hex(-1, +1), Hex( 0, +1)
]

function hex_direction(direction):
    return directions[direction]

function hex_neighbor(hex, direction):
    var dir = hex_direction(direction)
    return Hex(hex.q + dir.q, hex.r + dir.r)


    
>>offset<< (4 different implementations depending on grid type)

>>odd-r<<
var directions = [
   [ Hex(+1,  0), Hex( 0, -1), Hex(-1, -1),
     Hex(-1,  0), Hex(-1, +1), Hex( 0, +1) ],
   [ Hex(+1,  0), Hex(+1, -1), Hex( 0, -1),
     Hex(-1,  0), Hex( 0, +1), Hex(+1, +1) ]
]

function offset_neighbor(hex, direction):
    var parity = hex.row & 1
    var dir = directions[parity][direction]
    return Hex(hex.col + dir.col, hex.row + dir.row)

>>even-r<<
var directions = [
   [ Hex(+1,  0), Hex(+1, -1), Hex( 0, -1),
     Hex(-1,  0), Hex( 0, +1), Hex(+1, +1) ],
   [ Hex(+1,  0), Hex( 0, -1), Hex(-1, -1),
     Hex(-1,  0), Hex(-1, +1), Hex( 0, +1) ]
]

function offset_neighbor(hex, direction):
    var parity = hex.row & 1
    var dir = directions[parity][direction]
    return Hex(hex.col + dir.col, hex.row + dir.row)
    
>>odd-q<<
var directions = [
   [ Hex(+1,  0), Hex(+1, -1), Hex( 0, -1),
     Hex(-1, -1), Hex(-1,  0), Hex( 0, +1) ],
   [ Hex(+1, +1), Hex(+1,  0), Hex( 0, -1),
     Hex(-1,  0), Hex(-1, +1), Hex( 0, +1) ]
]

function offset_neighbor(hex, direction):
    var parity = hex.col & 1
    var dir = directions[parity][direction]
    return Hex(hex.col + dir.col, hex.row + dir.row)
    
>>even-q<<
var directions = [
   [ Hex(+1, +1), Hex(+1,  0), Hex( 0, -1),
     Hex(-1,  0), Hex(-1, +1), Hex( 0, +1) ],
   [ Hex(+1,  0), Hex(+1, -1), Hex( 0, -1),
     Hex(-1, -1), Hex(-1,  0), Hex( 0, +1) ]
]

function offset_neighbor(hex, direction):
    var parity = hex.col & 1
    var dir = directions[parity][direction]
    return Hex(hex.col + dir.col, hex.row + dir.row)
    
    
>>Diagonals<<
var diagonals = [
   Cube(+2, -1, -1), Cube(+1, +1, -2), Cube(-1, +2, -1), 
   Cube(-2, +1, +1), Cube(-1, -1, +2), Cube(+1, -2, +1)
]

function cube_diagonal_neighbor(hex, direction):
    return cube_add(hex, diagonals[direction])
