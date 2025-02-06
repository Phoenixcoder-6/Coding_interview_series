def permute(string,path=""):
    if not string:
        print(path)
        return
    for i in range(len(string)):
        rem= string[:i] + string[i+1:]
        permute(rem,path+string[i])
    
permute("ABC")
