def fact(d):
    if d==1 or d==0:
        return 1
    else:
        return d*fact(d-1)
def sum_of_digits(a):
    sum=0
    while a>0:
        last_digit=a%10
        sum=sum+last_digit
        a=a//10
    return sum
print(sum_of_digits(fact(100)))