# -*- coding: utf-8 -*-

import os
from shutil import copyfile

reg_data = ""
dir_path = os.path.dirname(os.path.realpath(__file__))

with open('Giants.reg', 'r', encoding='utf-16-le') as reg_file:
    reg_data = reg_file.read()

# https://pcgamingwiki.com/wiki/Giants:_Citizen_Kabuto
print("Using Giants.reg as template")

print("Data: " + "D:\\\\Program Files (x86)\\\\Giant")
print("Replaced by: " + dir_path.replace("\\", "\\\\"))

reg_data = reg_data.replace('D:\\\\Program Files (x86)\\\\Giants', dir_path.replace('\\', '\\\\'))

print("Saving...")

copyfile('Giants.reg', 'Giants_patched.reg')
with open('Giants_patched.reg', 'w', encoding='utf-16-le') as reg_file:
    reg_file.write(reg_data)

print("Custom register saved as Giants_patched.reg ...")

print("Applying Giants_patched.reg")
# https://norfipc.com/comandos/comandos-batch-modificar-registro.html
os.system("REG IMPORT Giants_patched.reg")

os.system("pause")
