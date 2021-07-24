import re
def isDelimiter(ch):
    if ( ch == '(' or ch == ')' or ch == '[' or ch == ']' or ch == '{' or ch == '}'):
        return(True)
    else:
        return(False)
def isOperator(ch):
    if (ch == '+' or ch == '-' or ch == '*' or 
        ch == '/' or ch == '>' or ch == '<' or 
        ch == '='):
        return (True)
    return (False)
def isSeparators(ch):
    if(ch == ',' or ch == ';'):
        return(True)
    return (False)
def isKeyword(ch):
    if ( ch == "if" or ch == "else" or ch == "else" or ch == "while" or ch == "do" or ch == "break" or ch == "continue" or ch == "int" or ch =="char" or ch == "case"
        or ch == "char" or ch == "return" or ch == "float" or ch == "double" or ch == "sizeof" or ch == "long" or ch == "short" or ch == "typedef" or ch == "switch"or ch == "unsigned"
        or ch == "void" or ch == "static" or ch == "struct" or ch == "goto"):
        return(True)
    return(False)
def isIndifiers(ch):
    if isKeyword(ch):
        return(False)
    else :
        regex1 = '^[A-Z]\w*'
        regex2 = '^[a-z]\w*'
        regex3 = '^_\w*'
        if(re.search(regex1, ch) or re.search(regex2, ch) or re.search(regex3, ch)):
            return(True)
        else:
            return(False)
def isLibrery(ch):
    if (ch == "stdio.h" or ch == 'math.h' or ch == 'ctype.h' or ch == 'string.h' or ch == 'time.h'):
        return(True)
    return(False)
    
Keywords = []
Identifiers = []
Operators = []
Separators = []
Constants =[]
Delimiter = []
Strings = []
Librery = []
f1= open("P_1.txt","r")
r = f1.read().splitlines()
#print(r)
n = len(r)
for i in range(n):
    m = r[i]
    if '//' in m:
        replaces= m.find('//')
        content = m[replaces:]
        m = m.replace(content,'')
    l = m.split(" ")
    #print(l)
    k = len(l)
    for j in range(k):
        #print(m[j])
        if l[j] == "#include":
            l[j] = ''
            print("#include is used to include the librery..")

        if '<' in l[j]:
            l[j] = l[j].replace('<','')
            Operators.append('<')
        
        if '>' in l[j]:
            l[j] = l[j].replace('>','')
            Operators.append('>')

        if '('in l[j]:
            str = l[j][0:l[j].find('(')]
            if isKeyword(str):
                Keywords.append(str)
            if isIndifiers(str):
                Identifiers.append(str)
            l[j] = l[j].replace(str,'')
            l[j] = l[j].replace('(','')
            Delimiter.append('(')
        if ')'in l[j]:
            #str1 = l[j][0:l[j].find(')')]
            '''if isKeyword(str1):
                Keywords.append(str1)
            if isIndifiers(str1):
               Identifiers.append(str1)
            l[j] = l[j].replace(str1,'')'''
            l[j] = l[j].replace(')','')
            Delimiter.append(')')
    
        if r'"' in l[j]:
            index1 = l[j].find('"')
            index2 = l[j].rfind('"')
            #print(index1,"and ",index2)
            #print(l[j][index1])
            l[j] = l[j].replace(l[j][index1],'')
            if r'"' in l[j]:
                l[j] = l[j].replace(l[j][index2],'')
            indes=l[j].find(',')
            if(indes== -1):
                strings1=l[j][:]
                Strings.append(strings1)
                #print(strings1)
                l[j] = ' '
            else:
                indexs = l[j].find(',') - 2
                indexs2 = l[j].find(',')
                strings = l[j][1:indexs]
                Strings.append(strings)
                l[j]=l[j][indexs2:] 

        if isLibrery(l[j]):
            Librery.append(l[j])
            l[j] = ''

        if l[j].isdigit():
            Constants.append(l[j])
        if isDelimiter(l[j]):
            Delimiter.append(l[j])
        if isOperator(l[j]):
            Operators.append(l[j])
        if isSeparators(l[j]):
            Separators.append(l[j])
        if isKeyword(l[j]):
            Keywords.append(l[j])
        if isIndifiers(l[j]):
            Identifiers.append(l[j])

        
print("......")
print("List of Libreries :- ",Librery)           
print("......")
print("List of Constants :- ",Constants)
print("......")
print("List of Delimiter :- ",Delimiter)
print("......")
print("List of Operators :- ",Operators)
print("......")
print("List of Separators :- ",Separators)
print("......")
print("List of Keywords :- ",Keywords)
print("......")
print("List of Identifiers :- ",Identifiers)
print("......")
seperater = ' '
print("List of Strings :- ",[seperater.join(Strings)])

