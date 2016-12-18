import sys
from PIL import Image

path = sys.argv[1]

def dec(im):

	cnt =0
	pix = im.load()
	s = ""
	result = ""
	for i in range(im.size[0]):
		for j in range(im.size[1]):
			s += chr((pix[i,j][3] & 1)+ord('0'))
			if len(s) > 7 and s[-8:-1] == "0"*7:
				print "".join([chr(int(s[i:i+7],2)) for i in range(0,len(s),7)])[:-1]
				return 0
			if len(s) > 700:
				print "Error: reveal text between 1-100 only"
				return 1
			
	print "Hidden Text not Found!"
	return 1
		
def enc(im):
	text = raw_input("Enter the Text: ")
	cnt = 0
	pix = im.load() # Pixels
	s = "".join([bin(ord(i))[2:].zfill(7) for i in text])
	s += ("0"*7)

	for i in range(im.size[0]):
		for j in range(im.size[1]):
			
			t = (pix[i,j][0], pix[i,j][1], pix[i,j][2], int(s[cnt],2))
			pix[i,j] = t
			cnt += 1
			if cnt == len(s):
				im.save(path)
				print "Hidding success!"
				return 0



	print "Hidding failed!"
	return 1
def main(flag, im):
	
	if flag == "d":
		dec(im)
	elif flag == "e":
		enc(im)
	else:
		print "Error: Choose 'd' for reveal the Text or 'e' for hide his"
	


if __name__ == "__main__":
	try:

		if len(sys.argv) == 3:	

			im = Image.open(path)
			main(sys.argv[2],im)
			im.close()
		else:
			print "Usage: {} <FileName> <Flag [d\e]>".format(sys.argv[0])
	except IOError:
		print "Error: could not open file {}.".format(sys.argv[1])

	
