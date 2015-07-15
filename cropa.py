import sys
import time
import os

#Entradas: video, w, h, nF

video = sys.argv[1]
w = int(sys.argv[2])
h = int(sys.argv[3])
nF = int(sys.argv[4])

name = video.split("_")
name = name[0]
newRes = str(w) + "x" + str(h)
out = time.strftime("%y_%m") + "/" + time.strftime("%d")
os.system("mkdir --p " + out) #creates results folder, if it insnt there already
r = open(out + "/" + "cropa_" + name + "_" + newRes + ".yuv", 'wb')

def cropa(seq, w, h, nF):
	size = seq.split("_")
	size = size[1].split("x")
	oldW = int(size[0])
	oldH = int(size[1])
	
	f = open("../../origCfP/" + seq + ".yuv", 'rb')
	leC = w/2
	lixoY = oldW - w
	lixoC = oldW/2 - leC
	restoY = oldH - h
	restoC = (oldH/2) - (h/2)
	
	for frames in range(0,nF): #executa nF vezes
		
		for l in range(0, h):
			Y = f.read(w)
			r.write(Y)
			f.read(lixoY)
		for l in range(0, restoY):
			f.read(oldW)
				
		for l in range(0, (h/2)):
			Cb = f.read(leC)
			r.write(Cb)
			f.read(lixoC) #descarta o restante dos bytes Cb
		for l in range(0, restoC):
			f.read(oldW/2)
				
		for l in range(0, (h/2)):
			Cr = f.read(leC)
			r.write(Cr)
			f.read(lixoC) #descarta o restante dos bytes Cr
		for l in range(0, restoC):
			f.read(oldW/2)
			
	f.close()
	r.close()

cropa(video, w, h, nF)
