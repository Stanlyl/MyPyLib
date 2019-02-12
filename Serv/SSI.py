from ctypes import *
import os

def SSI_init():
	global dll
	dll = cdll.LoadLibrary('SSICoder.dll')
	dll.Greetings.restype = c_char_p
	dll.SSI_Encrypt.restype = c_char_p
	dll.SSI_Encrypt.argtypes=[POINTER(c_char)]

#print(dll.Greetings().decode())

def OUT_process(message):
	STR = (c_char * 128)(*bytes(message,'utf-8'))
	cast(STR, POINTER(c_char))
	return dll.SSI_Encrypt(STR)

def In_process(code):
	return dll.SSI_Encrypt(code).decode()

def main():
	SSI_init()
	code = OUT_process('programme never die')
	print(code)
	message = In_process(code)
	print(message)

if __name__ == '__main__':
	main()
	print(os.path.abspath('../'))
	