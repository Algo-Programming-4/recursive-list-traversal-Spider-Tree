#Dimitri Workman
#Sept-20-2024
#Recursive Traversal List

def recursiveTraversal(nest,totalV,totalR,totalA,deep,max):
    deep=1
    totalR+=1
    for item in nest:
        if type(item)==int:
            totalV+=item
            totalA+=1
            deep+=1
            max.append(deep)
        elif type(item)!=list:
           
            totalA+=1
            deep+=1
        
        else:
            totalA+=1
            deep+=1
            totalV,totalR,totalA,deep,max= recursiveTraversal(item,totalV,totalR,totalA,deep,max)
    return totalV,totalR,totalA,deep,max
        

"""This main function passes arguments to the other functions"""
def main():
    #example list
    max=0
    nested_list = [[[3, [4]], "3"], 7, [10, 3], [4, [5, [2, 8]]], 8] 
    val,Rec,Amo,dep,depth=recursiveTraversal(nested_list,0,0,0,0,[])
    print(depth)
    print("")
    newList=[]
    newList.append(val)
    newList.append(Rec)
    newList.append(Amo)
    
    for x in depth:
        if x>dep:
            dep=x
    newList.append(dep)

    print(newList)
#calls program
if __name__ =="__main__":
    main()