def beginningwitha():
    a=open("story.txt","r")
    x=a.readlines()
    c=0
    for d in x:
        if d[0] in ["a","A"]:
            c+=1
    print("The number of lines are:",c)
    a.close()
#beginningwitha()

def endingwithe():
    a=open("story.txt","r")
    x=a.readlines()
    c=0
    for d in x:
        x=d.strip()
        if x[-1] in ["e","E"]:
            c+=1
    print("The number of lines are:",c)
    a.close()
#endingwithe()

def beginingending():
    a=open("story.txt","r")
    x=a.readlines()
    c=0
    for d in x:
        if d[0] in ["a","A","e","E","i","I","o","O","u","U"] and d[-3] in [".",","]:
            c+=1
    print("The number of lines are:",c)
    a.close()
#beginingending()

def lineprinting():
    a=open("story.txt","r")
    x=a.readlines()
    for b in range (len(x)):
        print("The line number is:",b+1,"the line is:",x[b],"The lenght of the line is:",len(x[b])-1)
    a.close()
#lineprinting()
    
def turningintoanotherfile():
    a=open("story.txt","r")
    b=open("text_file.txt","a+")
    x=a.readlines()
    for d in x:
        c=d[0].upper()+d[1:]
        b.write(c)
    a.close()
    b.close()
#turningintoanotherfile()

def wordsmorethan9letters():
    a=open("story.txt","r")
    x=a.read()
    c=0
    for d in x.split():
        if len(d)>=9:
            c+=1
    print("The number of words are:",c)
    a.close()
#wordsmorethan9letters()

def occurnacesofin():
    a=open("story.txt","r")
    x=a.read()
    c=0
    for d in x.split():
        if d in ["IN","in"]:
            c+=1
    print("The number of words are:",c)
    a.close()
#occurnacesofin()


 
    