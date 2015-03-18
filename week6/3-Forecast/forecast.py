def forecast(days):
    cdays={"sunshine":0,"snow":0,"rain":0}
    dmax=0
    for i in days:
        cdays[i]+=1
    for key,value in cdays.items():
        if value==max(cdays.values()):
            dmax+=1            
    if dmax==3:
        return "Forecast for tommorow is {}".format(days[-1])
    elif dmax==2:
        for key,value in cdays.items():
            if value!=max(cdays.values()):
                return "Forecast for tommorow is {}".format(key)
    else:
        for key,value in cdays.items():
            if value==max(cdays.values()):
                return "Forecast for tommorow is {}".format(key)
            
            
def main():
    if __name__=="__main__":
        main()
