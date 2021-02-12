# coding: utf-8

"""

	AUTOR    : ANDRADE ECHARRY (ALF)
	USO      : CIFRADO MUTANTE -> 'Inspirado en la pelicula Duro de matar 4.0'
	LICENCIA : GPL-3

"""

#//

__version__ = 4.2

__build__   = (__version__, "11/02/2021", "12:02:18 PM")

__author__  = 'Andrade Echarry -> ALF'

__email__   = 'hormigence123@gmail.com'

#/

# variables modificables
cuantica           = NameSpace()
cuantica.espacial  = 10 # => group.split*
cuantica.radius    = 60 # range.while*
cuantica.FristHash = False

#/

def toPos(cadena, passWord):
	lista = []
	for char in passWord:
		lista+=[ord(char) % cadena.len]
	return lista

#/

def PRE_Cryto(codificado, passWord):

	list_pos = toPos(codificado, passWord)

	result = ""
	conteo = 0x0
	for char in codificado:
		if conteo >= cuantica.radius*len(codificado)/100:
			try:
				result+= chr( (ord(char)+1) )
			except:
				result+= chr( (ord(char)-1) )
			conteo=0
		else:
			try:
				result+= chr( (ord(char)-1) )
			except:
				result+= chr( (ord(char)+1) )
			conteo+=1


	codificado=result

	for POS in list_pos:
		tmp        = ""
		tmpL       = []
		activate_Z = False
		for num, char in enumerate(codificado):

			if activate_Z:
				tmpL+=[char]
				continue

			if num == POS:
				activate_Z = True

			tmp+=char
		tmpL.reverse()
		codificado = tmp + tmpL.join()

	return codificado

#/

def PRE_DCryto(codificado, passWord):

	list_pos = toPos(codificado, passWord)

	for POS in reversed(list_pos):
		tmp        = ""
		tmpL       = []
		IsCorona_virus = False
		for num, char in enumerate(codificado):

			if IsCorona_virus:
				tmpL+=[char]
				continue

			if num == POS:
				IsCorona_virus = True

			tmp+=char
		tmpL.reverse()
		codificado = tmp + tmpL.join()

	result = ""
	conteo = 0x0
	for char in codificado:
		if conteo >= cuantica.radius*len(codificado)/100:
			try:
				result+= chr( (ord(char)-1) )
			except:
				result+= chr( (ord(char)+1) )
			conteo=0
		else:
			try:
				result+= chr( (ord(char)+1) )
			except:
				result+= chr( (ord(char)-1) )
			conteo+=1

	codificado=result

	return codificado

#/

def CIFRAR(encryptado, passWord):
	matriz = list(encryptado).group(cuantica.espacial)

	DATA_2 = ""
	for lista in matriz:
		result = ""
		for char in lista:
			if char != False:
				if type(char) is int: char = chr(char) # support string type on Byte
				result+=char

		if not cuantica.FristHash:
			pass1 = passWord
			pass2 = passWord.hash.toS
		else:
			pass1 = passWord.hash.toS
			pass2 = passWord

		PRE=PRE_DCryto(result, pass1)
		DATA_2+=PRE_DCryto(PRE, pass2)
	return DATA_2

#//

def DECIFRAR(cadena, passWord):
	matriz = list(cadena).group(cuantica.espacial)
	DATA_1 = ""
	for lista in matriz:
		result = ""
		for char in lista:
			if char != False:
				if type(char) is int: char = chr(char) # support string type on Byte
				result+=char

		if not cuantica.FristHash:
			pass1 = passWord.hash.toS
			pass2 = passWord
		else:
			pass1 = passWord
			pass2 = passWord.hash.toS

		PRE=PRE_Cryto(result, pass1)
		DATA_1+=PRE_Cryto(PRE, pass2)
	return DATA_1

#/

# C-API => cifrado -> metodo
objs_types = (str, u"ó", bytes,)
name_space = "Crypt"

CPythonBuiltin.create(
    (objs_types, name_space, CIFRAR),
)

#//

# C-API => decifrado -> metodo
objs_types = (str, u"ó", bytes,)
name_space = "Decrypt"

CPythonBuiltin.create(
    (objs_types, name_space, DECIFRAR),
)