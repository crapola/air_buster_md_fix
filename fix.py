# Generate the IPS fix for Air Buster.

import struct

def main():
	header=b"PATCH"
	eof=b"EOF"
	patch=(
	(b"\x00\xD2\x70",b"\x4e\xf9\x00\x07\x70\x00"),
	(b"\x07\x70\x00",b"\x02\x00\x00\x0f\xe5\x40\x0c\x80\x00\x00\x00\x28\x6f\x02\x70\x00\x4e\xf9\x00\x00\xd2\x76")
	)
	data=b"".join([p[0]+struct.pack(">h",len(p[1]))+p[1] for p in patch])
	all=header+data+eof
	with open("Air Buster (USA).ips","bw") as f:
		f.write(all)

if __name__=="__main__":
	main()