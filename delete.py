#!/usr/bin/python
# coding: utf-8

#----------------------------------------------------------------------------------------

"""
	Autor       : Andrade Echarry -> ALF

	Pais        : Venezuela

	Sistema     : Windows / Linux / Mac OS X | x32 / x64

	Dependencia : Python 2.5 o superior | x32 / x64

	Uso         : permite borrar DobleKey en Python (no requiere permisos administrativos)

	Copyright (C) 2021 Andrade Echarry -> ALF. All rights reserved.

"""

if not hasattr(__builtins__, "delos"):
	print ("InstallError: DelosEngine no esta instalado :("); exit()

#----------------------------------------------------------------------------------------

setWorkingDir()

#----------------------------------------------------------------------------------------

time_sleep = 0.8 if isConsole else 0

#----------------------------------------------------------------------------------------

try:
	__import__("DobleKey")
except:
	exit ("InstallError: NO existe una version de DobleKey instalada :)", time_sleep)

#----------------------------------------------------------------------------------------

import sys, site, os
from glob import glob as FindFile

plugin_archivo = "APP-Doblekey.py"

#----------------------------------------------------------------------------------------

if sys.version_info[:2] <= (2, 6): directorio_install = site.USER_SITE
else: directorio_install = site.getusersitepackages()

#----------------------------------------------------------------------------------------

autorun_FrameWork_path = os.path.join(directorio_install, "usercustomize.py")
__GOD__ = "\nimport DobleKey"

if autorun_FrameWork_path.path.isfile:
  autorun_FrameWork_path.path.save(
  	autorun_FrameWork_path.path.read().Replace(__GOD__)
  ).close()

#----------------------------------------------------------------------------------------

import DobleKey
DobleKey.__file__.path.delete()

#----------------------------------------------------------------------------------------

print ("LISTO")