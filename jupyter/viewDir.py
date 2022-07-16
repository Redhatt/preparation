import os
from time import time
    
    
def DTree(d):
    return Tree_(os.walk(d))
    
def Tree_(v, prefix="", last=""):    
    try:
        d, dirs, files = *next(v),
    except StopIteration or ValueError:
        return
    
    basename = os.path.basename(d)
    string = ""
    
    for ff in files[:-1]:
        string += prefix + "├───" + ff + "\n"
    
    if files:
        ff = files[-1]
        if not dirs:
            string += prefix + "└───" + ff + "\n"
        else:
            string += prefix + "├───" + ff + "\n"
        
    for dd in dirs[:-1]:
        string += prefix + "├──>" + dd + "\n"
        string += Tree_(v, prefix + "│    ")
        
    if dirs:
        dd = dirs[-1]
        string += prefix + "└──>" + dd + "\n"
        string += Tree_(v, prefix + "     ")
    
    return string
        
