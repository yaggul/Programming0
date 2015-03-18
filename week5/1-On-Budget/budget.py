def on_budget(books,budget):
    shBag={"books_on_budget":0,"loan":0}
    books=sorted(books)
    overbudget=0
    loan=0
    ind=0
    while ind<len(books):
        if books[ind]<=budget:
            budget-=books[ind]
            shBag['books_on_budget']+=1
            ind+=1
        else:
            overbudget+=books[ind]
            ind+=1
    if overbudget>budget:
        shBag['loan']=overbudget-budget
    else:
        pass
    return shBag


def main():
    if __name__=="__main__":
        main()
