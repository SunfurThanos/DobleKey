# coding: utf-8

#---------------------------------------------------------------------------------------

####################################
# Cifrado con contraseña simple    #
####################################

cadena = "hola mundo como estas"

# cifrado -> ejemplo
passWord = "1234"
cifrado = cadena.Crypt(passWord)
print (cifrado)

# decifrado -> ejemplo
passWord = "1234"
decifrado = cifrado.Decrypt(passWord)
print (decifrado)

#---------------------------------------------------------------------------------------

#########################################
# Cifrado con contraseña profesional    #
#########################################

print ()

import hashlib

cadena = "hola mundo como estas"

passWord = hashlib.sha512(b"1234").hexdigest()
cifrado  = cadena.Crypt(passWord)
print (cifrado)

# decifrado -> ejemplo
passWord  = hashlib.sha512(b"1234").hexdigest()
decifrado = cifrado.Decrypt(passWord)
print (decifrado)

#---------------------------------------------------------------------------------------

########################################################
# programa basico de cifrado de string tipo "BYTES"    #
########################################################

import hashlib

# variables de entorno
CHUCK            = b"\x00DELIMITADOR_BASICO\x00"
CHUCK_START      = 512
DEFAULT_ENCODING = 'utf-8'

if isPython3:
	def toBytes(string):
		return bytes(string, DEFAULT_ENCODING)
else:
	def toBytes(string):
		return bytes(string)

# funciones tacticas
def comparar(new, cifrado):
	PASS = cifrado[:CHUCK_START].split(CHUCK)[0]
	return True if toBytes(hashlib.sha512(new).hexdigest()) == PASS else False

def CIFRAR(cadena, passWord):
	passWord = hashlib.sha512(passWord).hexdigest()
	return toBytes(passWord) + CHUCK + toBytes(cadena.Crypt(passWord))


# cifrando datos
cadena   = b"HELLO WORLD"
passWord = b"505090"
cifrado  = CIFRAR(cadena, passWord)


# comparando que sea la contraseña correcta
passWord = b"505090"
if comparar(passWord, cifrado):
	# decifrando datos
	passWord  = hashlib.sha512(passWord).hexdigest()
	cifrado   = cifrado[:CHUCK_START].split(CHUCK)[1]
	decifrado = cifrado.Decrypt(passWord)
	print (decifrado)
else:
	print ("clave incorrecta")