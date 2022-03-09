import re

def eq_stam (elem, line, out):
    test = re.sub('$', '', line[elem])
    r = re.search('/',test)
    if(r != None):
        out.write("\'"+ test + "\'")
        return elem+1
    else:
        r = re.findall('\w+[\s\n]', test)
        if(len(r) > 1):
            out.write("[")
            for ele in r:
                out.write("\'" + ele + "\'")
            out.write("]")
        else:
             out.write("\'" + test + "\'")
        return elem+1     
#    r = re.findall('\w+[\s\n]', line[elem])
#    if (len(r) > 1):
#        for ele in r:
#            out.write("\'" + ele + "\' ")
#    out.write("\n")
#    return elem+1

def rule_stam (elem, line, out):
    r = re.findall("\w+[\s\n]", line[elem])
    if(len(r) > 0):
        out.write("input:\n")
        for ele in r:
            out.write("\t " + ele + ",\n")
        return shell_stam(elem+1, line, out)
    elif elem <= len(line)-1:
        return shell_stam(elem+1, line, out)
    else:
        return elem

def shell_stam (elem, line, out):
    r = re.search(r':', line[elem])
    if (r == None):
        out.write("shell: \n")
    while r == None:
            line[elem] = line[elem].strip()
            out.write("\'" + line[elem] + "\';\n")
            #r = re.search(r':', line[elem])
            if elem < len(line) - 1:
                elem += 1
                r = re.search(r':', line[elem])
            elif elem == len(line) - 1:
                out.write("\'" + line[elem] + "\';\n")
                break
            else:
                break
    return elem
#    else:
#        return elem



lines = []
with open('Testfile','r') as f:
    lines = f.readlines()

out = open('Snakefile', 'w')
i = 0
while i < len(lines):
    line = lines[i]
#    line = re.sub(r'$', ' ',line)
#    line = re.sub('(', '{',line)
#    line = re.sub(')','}',line)
    z = re.match("(\w+) =", line)
    if(z != None):
        
            out.write(z.group(1) + " =")
            i = eq_stam(i,lines,out)    
            continue
    
    z = re.match('(\w+):', line)
    if(z != None):
            out.write("rule "+z.group(1)+":\n");
            i = rule_stam(i, lines,out)
            continue
    

    out.write(lines[i])
    i+=1
            
    
out.close();

