#!/usr/bin/python
# coding: utf-8

#----------------------------------------------------------------------------------------

"""
	Autor       : Andrade Echarry -> ALF

	Pais        : Venezuela

	Sistema     : Windows / Linux / Mac OS X | x32 / x64

	Dependencia : Python 2.5 o superior | x32 / x64

	Uso         : permite instalar DobleKey en Python (no requiere permisos administrativos)

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
	exit ("InstallError: Ya existe una version anterior de DobleKey :)", time_sleep)
except: pass

#----------------------------------------------------------------------------------------

import sys, site, os, py_compile, shutil
from glob import glob as FindFile

plugin_archivo = "source-code/API.py"

#----------------------------------------------------------------------------------------

if sys.version_info[:2] <= (2, 6): directorio_install = site.USER_SITE
else: directorio_install = site.getusersitepackages()

#----------------------------------------------------------------------------------------

autorun_FrameWork_path = os.path.join(directorio_install, "usercustomize.py")
__GOD__ = "\nimport DobleKey"

if autorun_FrameWork_path.path.isfile:
  data = autorun_FrameWork_path.path.read() + __GOD__
  autorun_FrameWork_path.path.save(data).close()
else:
  autorun_FrameWork_path.path.save(__GOD__).close()

#----------------------------------------------------------------------------------------

if sys.version_info[:2] <= (2, 6): directorio_install = site.USER_SITE
else: directorio_install = site.getusersitepackages()
FrameWork_path_path = os.path.join(directorio_install, "DobleKey.pyc")

fileX = plugin_archivo
path_relative = os.path.relpath(fileX)
py_compile.compile(file=path_relative)

if float(sys.version.split(" ")[0][:3]) >= 3:
  pycache = os.path.relpath(FindFile(os.path.join(
  	"source-code","__pycache__", "API*"))[0])
  shutil.move(pycache, FrameWork_path_path )
  shutil.rmtree("source-code/__pycache__")
else:
  pycache = os.path.relpath(path_relative + "c")
  shutil.move(pycache, FrameWork_path_path)

#----------------------------------------------------------------------------------------

print ("LISTO")