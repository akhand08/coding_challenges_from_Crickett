
def read_file(filename):
    with open(filename, "r") as file:
        content = file.read()
        return content

def is_real_key(key):
    if key[0] == '"' and key[-1] == '"':
        return key
    
    return False

def is_valid_boolean(index, inside_json, json_size):
    value = None
    while index < json_size and inside_json[index] != ",":
        value += inside_json[index]
    value = value.strip()
    
    if value == "true":
        return index, True
    elif value == "false":
        return index, False
    else:
        return index, "Invalid"
    
    
    
def is_valid_string(index, inside_json, json_size):
    value = inside_json[index]
    index += 1
    
    while index < json_size and inside_json[index] != '"':
        value += inside_json[index]
        index += 1
    
    while index < json_size and inside_json[index] != ",":
        value += inside_json[index]
        index += 1
    
    
    value = value.strip()
    
    if value[0] == '"' and value[-1] == '"':
        return index, value[1:-1]
    
    return index, None
        



def retrieve_value(index, inside_json, json_size):
    value = None
    
    #  checking it is boolen or not
    
    if inside_json[index] == "t" or inside_json[index] == "f":
        index, value = is_valid_boolean(index, inside_json, json_size)
        
        if value == "Invalid":
            return index, None
        else:
            index, value
    
    if inside_json[index] == '"':
        index, value = is_valid_string(index, inside_json, json_size)
    
        
        
        if value == None:
            return index, None
        else:
            return index, value
        
