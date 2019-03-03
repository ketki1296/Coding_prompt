import os
import yaml

#Parses the path which is given as an input and calls 'saveyaml' to load the files. Also returns merged output that has to be saved to the file and printed.
def parsepath(x):
    splitpath = x.split("/") #splits the path about "/" and stores in an array splitpath
    l = len(splitpath)
    j = 0
    b = []

  
    for i in range(l,1,-1):
        path = "/".join(splitpath[0:i-1]) + "/" + splitpath[l-1] #joins the array elements about "/" to create path. Starts from child and goes up the heirarchy
        if os.path.exists(path): #checks if the path created by joining exits or not
            b.append(saveyaml(path)) #stores the data in the files in an array "b".
            j = j + 1
        else:
            break #breaks if path isn't found
    for i in range(1,j):
        for key1 in b[0]: #b[0] is the array element which has data of the child (the file of input path)
            if key1 in b[i]: #checking for duplicate keys in files that are in the parent directories
                dupkeys(b[0],b[i],key1)  #calls dupkeys to handle duplicate keys
        b[0].update(b[i]) #merges the data 
        
    return b[0] #returns the output to be printed

#handles duplicate keys and their values 
def dupkeys(child,parent,key1):
    c = {}
    if (type(child[key1]) == list) and (type(parent[key1]) == list): #if both the values of duplicate keys are lists
            for j in range(len(parent[key1])):
                child[key1].append(parent[key1][j])   #append them
            del parent[key1]  #deletes that duplicate key from parent
            
    elif (type(child[key1]) == list) and ((type(parent[key1]) == int) or (type(parent[key1]) == float) or (type(parent[key1]) == str) or (type(parent[key1]) == dict)):
        child[key1].append(parent[key1]) #if value of the dupliacte child key is list and value of the duplicate parent key is int/float/str/dict, append them
        del parent[key1]                 #deletes the duplicate parent key
        
    elif ((type(child[key1]) == int) or (type(child[key1]) == str) or (type(child[key1]) == float)) and ((type(parent[key1]) == int) or (type(parent[key1]) == list) or (type(parent[key1]) == str) or (type(parent[key1]) == dict) or (type(parent[key1]) == float)):
        del parent[key1] #deletes the duplicate parent key if the child key is str/int/float
        
    elif (type(child[key1]) == dict) and ((type(parent[key1]) == int) or (type(parent[key1]) == list) or (type(parent[key1]) == str) or (type(parent[key1]) == float)):
        del parent[key1] #deletes the duplicate parent key
        
    elif type((child[key1]) == dict) and (type(parent[key1]) == dict): #handles the case if there are nested keys
        for key2 in child[key1]: 
            if key2 in parent[key1]: #if nested keys are dupliacte too
                dupkeys(child[key1],parent[key1],key2) #recursive call to the function again
        parent[key1].update(child[key1]) #updates the parent with the child values for duplicate keys
        
        #manages those keys which arent in child but in parent (nested inside a duplicate key)
        for key2 in parent[key1]:
            if key2 not in child[key1]: 
                child[key1][key2] = parent[key1][key2]

#open the file and loads the data into a variable. Handles errors 
def saveyaml(x):
    with open(x,'r') as stream:
        try:
            data = yaml.load(stream)
            return data
        except yaml.YAMLError as exc:
            print(exc)

#Writes to the given input file
def writetofile(y,concat):
    with open(y,'w') as output:
        output.write(yaml.dump(concat,default_flow_style=False))

#reads the given input file
def readfile(y):
    with open(y,'r') as stream:
        try:
            data = yaml.load(stream)
            print_concat = yaml.dump(data, default_flow_style=False) #converts the data into yaml format
            print(print_concat) #prints the output

        except yaml.YAMLError as exc:
            print(exc)
        
if __name__== "__main__":
    file_path = input("Enter the path to the file: \t") #takes file path as the input
    concat = parsepath(file_path) #parses the filepath and reads the data, stores merged data in concat
    writetofile(file_path,concat) #writes into the file mentioned at input
    readfile(file_path) #reads the file for final merged output

