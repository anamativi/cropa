import sys

#Entradas: video, res, w, h, nF

video = sys.argv[1]
res = sys.argv[2]
w = int(sys.argv[3])
h = int(sys.argv[4])
nF = int(sys.argv[5])
out = "../../Results/cropa_"
name = video.split("_")
name = name[0]

def cropa(seq, res, w, h, nF):
	newRes = str(w) + "x" + str(h)
	f = open("../../origCfP/" + seq + ".yuv", 'rb')
	r = open(out + name + "_" + newRes + ".yuv", 'wb')
	res = res.split('x')
	oldW = int(res[0])
	oldH = int(res[1])
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

cropa(video, res, w, h, nF)
