

import utils

def read_file(filename):
    with open(filename, "r") as file:
        content = file.read()
        return content
    
    
def make_pair(inside_object, object):
    
    index = 0
    size = len(inside_object)
    
    
    while index < size:
        key = ""
        while inside_object[index] != ":":
            key += inside_object[index]
            index += 1
        
        key = utils.is_real_key(key)
        if key == False and inside_object[index+1] != " ":
            return False
        else:
            
        
        
    
    
        
def JSON_parse(filename):
    content = read_file(filename)
    object = {}
    print(content[1])
    
    if content != "" and content[0] == "{" and content[-1] == "}":
        pass
    else:
        return False





if __name__ == "__main__":
    invalid_json_file = "./tests/step2/invalid.json"
    valid_json_file = "./tests/step2/valid.json"
    print(JSON_parse(invalid_json_file))