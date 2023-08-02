## Air Buster Fix
This is an IPS patch for **Air Buster** / **Aero Blasters** on the Sega Genesis that fixes the freeze in stage 5 and 6.

#### Detailed description

The bug happens in low gravity sections when you press too many directions at the same time (specifically left, down and right).\
The faulty function:
````
loc_0000D26A:
	SUBQ.w	#4, $1A(A1)
	MOVE.w	D1, D2
	ANDI.b	#$0F, D0
	ASL.w	#2, D0
	JMP	loc_0000D27A(PC,D0.l)
; Followed by 11 jump destinations.
````
At this point, D0's lower nibble contains input information in the form:
```
direction: RLDU
      bit: 3210
```
There are 11 functions to jump to, so the valid range for D0 before alignment
is (0,10).\
A value of 10 corresponds to right (8) + down (2) which is probably the highest you could get using the original hardware.
A modern emulator that doesn't filter "wrong" inputs makes it easy to exceed this value and cause a crash.


