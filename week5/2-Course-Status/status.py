def gen_names():
    names=[]    
    n=int(input("Please enter number of students: "))
    count=0
    while count<n:
        names+=[str(input("Please enter student name: "))]
        count+=1
    status=['finalized','not-finalized']
    return names,status


def gen_persons(names,status):
    #Generating people list of dictionaries
    i=0
    j=0
    persons=[]
    statut={}
    while i<len(names):
        j=0        
        while j<=len(status)-1:
            if i >len(names)-1:
                break
            else:                
                statut['name']=names[i]
                statut['status']=status[j]
                persons+=[statut]
                statut={}
                j+=1
                i+=1
    return persons


def fin(persons):
    finish={'finalized':[],'not-finalized':[]}
    for i in persons:
        finish[i['status']]+=[i['name']]
    return finish


def main():
    if __name__=='__main__':
        main()
        
names,status=gen_names()        
print("\nGenerated names are {}\n".format(names))
print("Generated statuses are {}\n".format(status))
print(fin(gen_persons(names,status)))
