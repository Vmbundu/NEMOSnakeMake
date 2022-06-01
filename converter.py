import re

# Analyzing initialization statement
def eq_stam (elem, line, word):
    test = re.sub('$', '', line[elem])
    r = re.search('/',test)
    if(r != None):
        m = re.findall('(\S+)', test)
        print(m[0] + ' ' + m[1]+ " \'"+ m[2] + "\'\n", end= " ")
        return elem+1
    else:
        r = re.findall('(\w+)[\s\n]+', test)
        if(len(r) > 2):
            print(r[0] + " = ", end= " ")
            print("[", end= " ")
            l = 1
            for ele in r:
                if ele != word and l < len(r) - 1:
                    print("\'" + ele + "\',", end= " ")
                    l += 1
                elif l == len(r) - 1:
                    print("\'" + ele + "\'", end=" ")
            print("]\n", end= " ")
        else:
             print(test)
        return elem+1     
#    r = re.findall('\w+[\s\n]', line[elem])
#    if (len(r) > 1):
#        for ele in r:
#            out.write("\'" + ele + "\' ")
#    out.write("\n")
#    return elem+1

#Handles the target title 
def rule_stam (elem, line):
    r = re.findall(' \w+', line[elem])
    if(len(r) > 1):
        print("\tinput:\n", end= " ")
        for ele in r:
            print("\t " + ele + ",\n", end= " ")
        return shell_stam(elem+1, line)
    elif elem <= len(line)-1:
        return shell_stam(elem+1, line)
    else:
        return shell_stam(elem+1, line)

#Handles shell portion
def shell_stam (elem, line):
    r = re.search(r':', line[elem])
    if(re.search(r'^\s+$', line[elem]) != None):
        return elem  
    elif (r == None):
        print("\tshell: \n", end= " ")
    while r == None and line[elem] != '':
            line[elem] = line[elem].strip()
            #out.write("\'" + line[elem] + "\';\n")
            #r = re.search(r':', line[elem])
            if elem < len(line) - 1 and line[elem] != '':
                print("\t  \'" + line[elem] + "\';\n", end= " ")
                elem += 1
                r = re.search(r':', line[elem])
            elif elem == len(line) - 1 and line[elem] != '':
                print("\t  \'" + line[elem] + "\';\n", end= " ")
                break
    return elem
#    else:
#        return elem


#Starts here
lines = []
with open('Testfile','r') as f:
    lines = f.readlines()

#out = open('Snakefile', 'w')
i = 0
while i < len(lines) - 1:
    line = lines[i]
#    line = re.sub(r'$', ' ',line)
#    line = re.sub('(', '{',line)
#    line = re.sub(')','}',line)
    z = re.match("(\w+) =", line)
    if(z != None):
        
#            out.write(z.group(1) + " =")
            i = eq_stam(i,lines, z.group(1))    
            continue
    
    z = re.match('(\w+):', line)
    if(z != None):
            print("rule "+z.group(1)+":\n", end= " ");
            i = rule_stam(i, lines)
            continue
    

    print(lines[i])
    i+=1
f.close()            
    


