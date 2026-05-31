import math

num1 = int(input("Num1: "))
num2 = int(input("Num2: "))
# Find GCD
gcd_result = math.gcd(num1, num2)

# Find LCM
lcm_result = math.lcm(num1, num2)

print(f"The GCD of {num1} and {num2} is: {gcd_result}")  
print(f"The LCM of {num1} and {num2} is: {lcm_result}") 
