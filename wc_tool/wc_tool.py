

import os

class CommandNameError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
        
        
def command_name_checkr(command_name):
    if command_name != "wc":
        raise CommandNameError("It is invalid command. Please write the correct one")
    
    
class FlagError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
        
        
def flag_checkr(flag):
    flaglist = ["-l", "-m", "-c", "-w"]
    
    if flag not in flaglist:
        raise FlagError("The flag is not correct")
    
    


    
    
            

def validity_checkr(command_name, flag, file_name):
    try:
        command_name_checkr(command_name)
    except CommandNameError as cne:
        print(f"Command Error: The '{command_name}' is not valid")
        return False
    
    try: 
        flag_checkr(flag)
    except FlagError as fe:
        print({fe})
        return False
        
    try:
        with open(file_name, "r") as file:
            pass
    except FileNotFoundError:
        print(f"Error: The '{file_name}' does not exist")
        return False
    except Exception as e:
        print({e})
        return False
        
        
    return True
        
        
        
def wc_tool(flag, file_name):
    
    
    if flag == "-l":
        with open(file_name, "r") as file:
            lines = file.readlines()
            print(f"{len(lines)} {file_name}")
    
    elif flag == "-c":
        with open(file_name, "rb") as file:
            byte_size = len(file.read())
            print(f"{byte_size} {file_name}")
            
        return
    
    elif flag == "-w":
        with open(file_name, "r") as file:
            content = file.read()
            word_count = len(content.split())
            print(f"{word_count} {file_name}")
        return
    
    elif flag == "-m":
        with open(file_name, "rb"  ) as file:
            char_count = len(file.readlines())
            print(f"{char_count} {file_name}")
        return
            
        
        
        




command_input = input()


values = command_input.split(" ")
command_name = values[0]
flag = values[1]
file_name = values[2]

if validity_checkr(command_name, flag, file_name) == True:
    wc_tool(flag,file_name)
    


