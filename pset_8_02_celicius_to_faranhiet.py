temp = int(input("Enter temperature in celcious : "))
def farh(temp):                     # Function declaration
    return(temp *(9/5)) + 32
f = farh(temp)                      #Function call
print(f"Temprerature  of  {temp} in faranhiest is = {str(f)}")