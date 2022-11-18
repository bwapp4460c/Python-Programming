

def fact(num):
  
    factorial = 0
    
    if num <=1 :
        factorial = 1
        
    else:
      factorial = num * factorial(n-1)
      
    return fact



num = int(input())
print(fact(num))
