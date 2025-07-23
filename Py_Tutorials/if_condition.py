n=int(input("Enter a number: "))
print(n)
if n%2==0:
    print(f"{n} is an even number")
else:
    print(f"{n} is an odd number")
# Using a ternary operator
message="Number is even" if n%2==0 else "Number is odd"
print(message)
# Using negate operator
if not n%2==0:
    print(f"{n} is an odd number")
else:
    print(f"{n} is an even number")
#using and
if n > 10 and n % 2 == 0:
    print(f"{n} is greater than 10 and even")
else:
    print(f"{n} is less than 10 and even")
#examples
indian = ["samasa","suresh","karthik"]
chinese = ["egg role","chow mein","spring roll"]
italian = ["pizza","pasta","lasagna"]

dish = input("Enter a dish: ")

if dish in indian:
    print(f"{dish} is an Indian dish")
elif dish in italian:
    print(f"{dish} is an Italian dish")
elif dish in chinese:
    print(f"{dish} is a Chinese dish")
else:
    print(f"I don't know about {dish}")




