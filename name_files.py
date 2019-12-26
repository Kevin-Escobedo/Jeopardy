#Author: Kevin C. Escobedo
#Email: escobedo001@gmail.com

def get_file_name(file_name:str = "") -> str:
    '''Adds a suffix to a file name if it already exists'''
    info = file_name.split(".")
    name = info[0]
    extension = info[1]
    failures = 1
    while True:
        try:
            with open(file_name, "r") as file:
                pass
        except FileNotFoundError:
            return file_name
        file_name = "{}-{}.{}".format(name, failures, extension)
        failures += 1
    
    
    
