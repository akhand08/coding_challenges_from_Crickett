

import os

class CommandNameError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
        
        
def command_name_checker(command_name):
    
    if command_name != "ccwc":
        raise CommandNameError(f"Command Name Error: The command '{command_name}' is not valid")
    
    
class FlagError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
        
        
def flag_checker(flag):
    flaglist = ["-l", "-m", "-c", "-w"]
    
    if flag not in flaglist:
        raise FlagError(f"Flag Error: The '{flag}' is not valid")
    
    


class IncompleteCommandError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    
    
            

def validity_checker(command_name, **kwargs):
    
    file_name = kwargs["file_name"]
    
    
    
    try:
        command_name_checker(command_name)
    except CommandNameError as cne:
        print(cne)
        return False
    
    try: 
        flag_name = kwargs["flag_name"]
        if flag_name != None:
            flag_checker(flag_name)
        
    except FlagError as fe:
        print(fe)
        return False
        
    try:
        with open(file_name, "r") as file:
            pass
    except FileNotFoundError:
        print(f"Error: The '{file_name}' does not exist")
        return False
   
        
    return True


def standard_input_checker(utility, isPipe):
    if utility == "cat" and isPipe == "|":
        return True
    return False
        
        
        
def wc_tool(flag, file_name):
    
    line_count = None
    byte_size = None
    word_count = None
    char_count = None
    
    with open(file_name, "r") as file:
        content = file.readlines()
        line_count = len(content)
        word_count = sum(len(line.split()) for line in content)
    
    with open(file_name, "rb") as file:
        content = file.read()
        byte_size = len(content)
        char_count = byte_size
    
    if flag == "-l":
        print(f" {line_count}  {file_name}")
    
    elif flag == "-c":
        print(f" {byte_size}  {file_name}")
    
    elif flag == "-w":
        print(f" {word_count}   {file_name}")

    
    elif flag == "-m":
        print(f" {char_count}  {file_name}")
    
    elif flag == "all":
        print(f" {line_count}   {word_count}   {byte_size} ") 
       
            
        
        
        




command_input = input()

values = command_input.split(" ")
command_name = None
flag_name = None
file_name = None

if len(values) == 3:
    command_name = values[0]
    flag_name = values[1]
    file_name = values[2]
    
    if validity_checker(command_name, file_name = file_name, flag_name = flag_name) == True:
        wc_tool(flag_name, file_name)
    
    
    
elif len(values) == 2:
    command_name = values[0]
    file_name = values[1]
    
    if validity_checker(command_name, file_name = file_name, flag_name = None) == True:
        wc_tool("all", file_name)
        
        
elif len(values) == 5:
    command_name = values[3]
    flag_name = values[4]
    file_name = values[1]
    
    if standard_input_checker(values[0], values[2])  and validity_checker(command_name, file_name = file_name, flag_name = flag_name) :
        wc_tool(flag_name, file_name)
    
    
else:
    try:
        raise IncompleteCommandError("Incomplete Command Error: This is not a valid command")
    except IncompleteCommandError as ice:
        print(ice)
        
    


    


