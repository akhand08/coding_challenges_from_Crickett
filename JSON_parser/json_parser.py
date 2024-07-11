

import utils
import json
    
    
def make_pair(inside_json):
    
    object = {}
    index = 0
    size = len(inside_json)
    
    
    while index < size:
        key = inside_json[index]
        index += 1
        while inside_json[index] != '"' and index < size:
            key += inside_json[index]
            index += 1
        key += inside_json[index]
        
        while inside_json[index] != ":" and index < size:
            index += 1
            
        key = utils.is_real_key(key)
        
        
        if key == False:
            return False
    
        
        
        value = None
        index += 1
        while inside_json[index] == " " and index < size:
            index += 1
        
        
        index , value = utils.retrieve_value(index,inside_json, size)
        
     
        if value != None:
            object[key[1:-1]] = value
        else:
            return False
    
    return object
        
            
        
            
        
        
    
    
        
def JSON_parse(filename):
    content = utils.read_file(filename)
    content = content.strip()
    # print(content)
    if content != "" and content[0] == "{" and content[-1] == "}":
        object = make_pair(content[1:-1].strip())
        return object
    else:
        return False





if __name__ == "__main__":
    invalid_json_file = "./tests/step1/invalid.json"
    valid_json_file = "./tests/step2/valid.json"
    print(JSON_parse(valid_json_file))
    