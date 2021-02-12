
DobleKey
========

Sistema Ultra ligero y Veloz de cifrado de datos, siendo la mejora por muchos de los sistema predecesores como el `Cifrado Cesar` y `cifrado RSA`, este nuevo sistema esta hecho desde 0 en Python, permitiendo una implementación muy amplia & portable.

---

> Ventajas de usarlo

1. No aumenta la longitud de los datos originales, solo cambia el tipo & orden de los caracteres, permitiendo una excelente implementación en BD de datos.

2. Desarrollo vivo & abierto a nuevas ideas.

3. !Gratis por siempre!

4. Hecho con amor & magia en Python

5. El algoritmo muta en base a la fuerza bruta, durante un ataque al insertar N posibles contraseñas para el descifrado de una cadena, esta cambiara continuamente pero nunca te dirá si haz insertado la contraseña correcta, eso sin contar que dependiendo la configuración de las variables establecidas durante el cifrado, el resultado siempre sera distinto, por primera vez tendrás un cifrado que podrás modificar a tu antojo.

---

*Consejo*: Si para ti vale mucho mantener un secreto !Entonces usa DobleKey!

---

> Python: ejemplos de uso

```python
####################################
# Cifrado con contraseña simple    #
####################################

cadena = "hola mundo como estas"

# cifrado -> ejemplo
passWord = "1234"
cifrado  = cadena.Crypt(passWord)
print (cifrado)

# decifrado -> ejemplo
passWord  = "1234"
decifrado = cifrado.Decrypt(passWord)
print (decifrado)
```


```python
#########################################
# Cifrado con contraseña profesional    #
#########################################

import hashlib

cadena = "hola mundo como estas"

passWord = hashlib.sha512(b"1234").hexdigest()
cifrado  = cadena.Crypt(passWord)
print (cifrado)

# decifrado -> ejemplo
passWord  = hashlib.sha512(b"1234").hexdigest()
decifrado = cifrado.Decrypt(passWord)
print (decifrado)
```


```python
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
```

---

## ¿Como instalar DobleKey en Python?

*PASO 1*
- Asegúrese de tener instalado Python 2.5 o superior

*PASO 2*
- Instale en Python el Potente FrameWork de productividad [DelosEgine](https://github.com/SunfurThanos/DelosEngine-ES)

*PASO 3*
- Ya puedes instalar DobleKey, ejecutando el archivo [install.py](install.py)

*FIN*
- Felicidades ya puedes usar DobleKey en Python :)

---

Para preguntas o explicaciones más técnicas de este nuevo cifrado puede contactarme por el siguiente correo & podre ayudarle a la brevedad posible.

[correo de contacto](hormigence123@gmil.com).

---

> herramientas en desarrollo, serán codificadas desde 0 en ¡Python ♥+!

1. Aumento de variables de ambiguedad.

2. Cifrado y descifrado multi-core, aumento de la velocidad en un 200%.

3. Soporte para reanudar el cifrado aun si el ordenador se apaga de manera forzosa.

4. Hiper-velocidad de cifrado y descifrado para GRANDES archivos, inter-conectando Nodos o Data centers de manera inteligente.

[<img src="source-code\donar.png">](https://www.paypal.me/SunfurThanos)

---

*Andrade Echarry -> 'ALF'* Si aprendes a estar abierto para adaptarte ¡seras invencible!