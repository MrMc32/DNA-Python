import os

def Startup():
	os.system("cls")
	os.system("pip install random")
	os.system("pip install colorama")
	os.system("pip install time")
	os.system("pip install WConio2")
	os.system("cls")
Startup()

import random, colorama, time, WConio2

StopSimulation = False

def PressToPause():
	key = WConio2.getkey()
	if(key == " "):
		StopSim()
	else:
		pass

def StopSim():
	global StopSimulation
	if(StopSimulation == False):
		StopSimulation = True
	else:
		StopSimulation = False

def PrintDNA():
	global StopSimulation

	x = 5
	y = 5
	spaces = 5
	direction = 1
	right_spaces = 5

	while True:
		if(StopSimulation == True):
			PressToPause()
		else:
			PressToPause()
			ColorLeft = random.randint(1, 4)
			ColorRight = random.randint(1, 4)
			LeftText = ""
			RightText = ""

			Description = ""
			
			if(ColorLeft == 1):
				if(ColorRight == 1):
					Description = "\033[0;37;41m \033[0;37;40m - Double-Cytosine"
				elif(ColorRight == 2):
					Description = "\033[0;37;41m \033[0;37;40m - Cytosine 		|		\033[0;37;42m \033[0;37;40m - Adenine"
				elif(ColorRight == 3):
					Description = "\033[0;37;41m \033[0;37;40m - Cytosine 		|		\033[0;37;45m \033[0;37;40m - Guanine"
				else:
					Description = "\033[0;37;41m \033[0;37;40m - Cytosine 		|		\033[0;37;43m \033[0;37;40m - Thymine"
				LeftText = "\033[0;37;41m"
			elif(ColorLeft == 2):
				if(ColorRight == 1):
					Description = "\033[0;37;42m \033[0;37;40m - Adenine 		|		\033[0;37;41m \033[0;37;40m - Cytosine"
				elif(ColorRight == 2):
					Description = "\033[0;37;42m \033[0;37;40m - Double-Adenine"
				elif(ColorRight == 3):
					Description = "\033[0;37;42m \033[0;37;40m - Adenine 		|		\033[0;37;45m \033[0;37;40m - Guanine"
				else:
					Description = "\033[0;37;42m \033[0;37;40m - Adenine 		|		\033[0;37;43m \033[0;37;40m - Thymine"
				LeftText = "\033[0;37;42m"
			elif(ColorLeft == 3):
				if(ColorRight == 1):
					Description = "\033[0;37;45m \033[0;37;40m - Guanine 		|		\033[0;37;41m \033[0;37;40m - Cytosine"
				elif(ColorRight == 2):
					Description = "\033[0;37;45m \033[0;37;40m - Guanine 		|		\033[0;37;42m \033[0;37;40m - Adenine"
				elif(ColorRight == 3):
					Description = "\033[0;37;45m \033[0;37;40m - Double-Guanine"
				else:
					Description = "\033[0;37;45m \033[0;37;40m - Guanine 		|		\033[0;37;43m \033[0;37;40m - Thymine"
				LeftText = "\033[0;37;45m"
			else:
				if(ColorRight == 1):
					Description = "\033[0;37;43m \033[0;37;40m - Thymine 		|		\033[0;37;41m \033[0;37;40m - Cytosine"
				elif(ColorRight == 2):
					Description = "\033[0;37;43m \033[0;37;40m - Thymine 		|		\033[0;37;42m \033[0;37;40m - Adenine"
				elif(ColorRight == 3):
					Description = "\033[0;37;43m \033[0;37;40m - Thymine 		|		\033[0;37;45m \033[0;37;40m - Guanine"
				else:
					Description = "\033[0;37;43m \033[0;37;40m - Double-Thymine"
				LeftText = "\033[0;37;43m"
			
			if(ColorRight == 1):
				RightText = "\033[0;37;41m"
			elif(ColorRight == 2):
				RightText = "\033[0;37;42m"
			elif(ColorRight == 3):
				RightText = "\033[0;37;45m"
			else:
				RightText = '\033[0;37;43m'
			
			DNALine = "\033[0;37;40m" + " " * spaces + "\033[0;37;47m#" + LeftText + "-" * x + RightText + "-" * y + "\033[0;37;47m#" + "\033[0;37;40m" + " " * right_spaces + Description
			print(DNALine)
			time.sleep(0.05)

			if(direction == 1):
				if(x <= 0):
					direction = -1
				else:
					spaces += 1
					right_spaces += 1 
					x -= 1
					y -= 1
			if(direction == -1):
				if(x >= 5):
					direction = 1
				else:
					spaces -= 1
					right_spaces -= 1
					x += 1
					y += 1

PrintDNA()