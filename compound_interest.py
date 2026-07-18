principal = 0
rate = 0
time = 0
amount = 0

while principal <= 0:
    principal = float(input("Enter the principle: "))
    if(principal <= 0):
        print("Principle amount cannot be equal to or less than 0")


while rate <= 0:
    rate = float(input("Enter your rate of interest: "))
    if(rate <= 0):
        print("rate of intereset cannot be equal to or less than 0")

while time <= 0:
    time = int(input("Enter the time in years: "))
    if(time <= 0):
        print("Time cannot be equal to or less than 0")

print(principal)
print(rate)
print(time)

amount = principal * ((1 + rate/100) ** time)
print(f"Balance after {time} years is ${amount:.2f}")
