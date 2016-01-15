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
  




# HexEdges: Indicies
# A 0,1;
# B 1,2;
# C 2,3;
# D 3,4;
# E 4,5;
# F 5,0;




