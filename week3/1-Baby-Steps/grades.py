students=["mitko","kati","niki","bobi"]
grades=[4.0,3.5,5.0,6.0]
def grades_that_pass(students,grades,limit):
    passed=[]
    start=0
    while start<len(grades):
        if grades[start]>=limit:
            passed+=[students[start]]
        start+=1
    return passed

result=grades_that_pass(students,grades,5.0)
print(result)
