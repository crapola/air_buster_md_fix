# Generate the IPS files for Air Buster.

import struct

def create_ips(filename:str,patch:tuple):
	with open(filename,"bw") as f:
		data=b"".join([p[0]+struct.pack(">h",len(p[1]))+p[1] for p in patch])
		f.write(b"PATCH"+data+b"EOF")

def main():
	patch_us=(
		(b"\x00\xD2\x70",b"\x4e\xf9\x00\x07\x70\x00"),
		(b"\x07\x70\x00",b"\x02\x00\x00\x0f\xe5\x40\x0c\x80\x00\x00\x00\x28\x6f\x02\x70\x00\x4e\xf9\x00\x00\xd2\x76")
		)
	create_ips("Air Buster (USA).ips",patch_us)
	patch_jp=(
		(b"\x00\xD2\x54",b"\x4e\xf9\x00\x07\x70\x00"),
		(b"\x07\x70\x00",b"\x02\x00\x00\x0f\xe5\x40\x0c\x80\x00\x00\x00\x28\x6f\x02\x70\x00\x4e\xf9\x00\x00\xd2\x5a")
		)
	create_ips("Aero Blasters (Japan).ips",patch_jp)

if __name__=="__main__":
	main()