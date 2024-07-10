

import utils
import json
    
    
def make_pair(inside_json, object):
    
    index = 0
    size = len(inside_json)
    
    
    while index < size:
        key = ""
        while inside_json[index] != ":":
            key += inside_json[index]
            index += 1
        
        key = utils.is_real_key(key)
        if key == False and inside_json[index+1] != " ":
            return False
        else:
            pass
            
        
        
    
    
        
def JSON_parse(filename):
    content = utils.read_file(filename)
    object = {}
    if content != "" and content[0] == "{" and content[-1] == "}":
        return True
    else:
        return False





if __name__ == "__main__":
    invalid_json_file = "./tests/step1/invalid.json"
    valid_json_file = "./tests/step1/valid.json"
    print(JSON_parse(valid_json_file))
    