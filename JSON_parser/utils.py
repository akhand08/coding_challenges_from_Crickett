
def read_file(filename):
    with open(filename, "r") as file:
        content = file.read()
        return content

def is_real_key(key):
    if key[0] == '"' and key[-1] == '"':
        return True
    
    return False