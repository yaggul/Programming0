def travel_cost(travels):
    trv=0
    tickets=[]
    sline=[]
    ticket_c=0
    for i in travels:
        trv+=i
    if trv>=50:
        return "Най-добре карта за всички линии за {} лева".format(50)
    else:
        if sorted(travels)[-1]<23:
            return 'Най-добре е да се пътува само с билети за {} лева'.format(trv)
        else:
            for i in travels:
                if i>=23:
                    sline+=[i]
                else:
                    tickets+=[i]
                    for i in tickets:
                        ticket_c+=i
            print(sline)
            print(tickets)
            return "Най-добре с карта за {} и билети за {}, за общо {} лева".format(sline,tickets,len(sline)*23+ticket_c)
            
def main():
    if __name__=='__main__':
        main()
