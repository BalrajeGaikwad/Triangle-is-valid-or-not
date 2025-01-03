#g) Write a program to check whether a triangle is valid or not, when the three angles of the triangle are entered through the keyboard. 
# A triangle is valid if the sum of all the three angles is equal to 180 degrees.

a=int(input("First Angle :"))
b=int(input("First Angle :"))
c=int(input("First Angle :"))

if(a+b+c == 180):
    print("Triangle is valid and sum is 180")
else:
    print("not valid")
