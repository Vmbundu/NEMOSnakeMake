import re

def eq_stam (elem, line, out):
    r = re.findall(r' \w+ ', line[elem])
    if (len(r) > 1):
        for ele in r:
            out.write("\'" + ele + "\' ")
    out.write("\n")
    return elem+1

def rule_stam (elem, line, out):
    r = re.findall("\w+ ", line[elem])
    if(len(r) > 0):
        out.write("input:\n")
        for ele in r:
            out.write("\t " + ele + ",\n")
        return shell_stam(elem, line, out)
    else:
        return elem+1

def shell_stam (elem, line, out):
    r = re.search(r':', line[elem])
    if (r == None):
        out.write("shell: \n")
        while r == None:
            out.write("\'" + line[elem] + "\';\n")
            elem += 1
            r = re.search(r':', line[elem])
        return elem
    else:
        return elem



lines = []
with open('Testfile.copy','r') as f:
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

