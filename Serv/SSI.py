from ctypes import *
dll = cdll.LoadLibrary('SSICoder.dll')
dll.hello.restype = c_char_p
#print(dll.hello().decode())
dll.SSI_Encrypt.argtypes=[POINTER(c_char)]
dll.SSI_Encrypt.restype = c_char_p
STR = (c_char * 128)(*bytes('Hello Python','utf-8'))
cast(STR, POINTER(c_char))
code = dll.SSI_Encrypt(STR)
print(code)
wer = dll.SSI_Encrypt(code)
print(wer.decode())
