

namespace alpha
{
	enum SoldierStance
	{
		STANCE_STANDING,
		STANCE_HISUPP,
		STANCE_HUNCH,
		STANCE_LOSUPP,
		STANCE_KNEEL,
		STANCE_SITTING,
		STANCE_PRONE,
		STANCE_QUART, // Dir R/L
		STANCE_BACK
	};
}

// Action - Aim - MoveToCorrect

AIM:
0   - Center mass
1.a - High
  2.x - Head
    3.x - Face
	  4.x - EyeRight
	    5.x - Brain (Some req. anatomy to approx position)
		  6.x - SubParts
	      - Nose
	    - BackOfHead
		- RightSide
      - Neck
	  - Torso
1.b - Low
+Additional action
+Fast
+Heavy
+Precise
+Non-lethal
+Gen.Offensive
+Gen.Defensive



SKILLS:


SNAPDEGREE - MoveToCorrect:
DegreeSnaps
       0
    22.5
      45
    67.5
      90
   112.5
     135
   157.5
     180
   202.5
     225
   247.5
     270
   292.5
     315
   337.5
     360

