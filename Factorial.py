

def fact(num):
  
    factorial = 0
    
    if num <=1 :
        factorial = 1
        
    else:
      factorial = num * fact(num-1)
      
    return factorial



num = int(input())
print(fact(num))
