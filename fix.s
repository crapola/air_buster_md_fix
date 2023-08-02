patch:
	ORG $D270
	JMP $77000
fix:
	ORG $77000
	; Moved instructions.
	ANDI.b #$0F,D0
	ASL.w #2,D0
	; The fix.
	CMPI.l #40,D0
	BLE ok
	CLR.l D0
ok:
	; Resume
	JMP $D276
