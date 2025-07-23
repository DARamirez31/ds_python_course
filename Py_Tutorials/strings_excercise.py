#help(str)

#1
fruits = ['apple','banana','orange','grapes','mango','kiwi']
vegetables = ['carrot','potato','onion','tomato','cucumber','broccoli']
message=f"I eat {fruits[0]}, {fruits[1]}, and {fruits[2]} for breakfast, and {vegetables[0]}, {vegetables[1]}, and {vegetables[2]} for lunch."
print(message)
#2
Idea= "The Himalayas are one of the youngest mountain ranges on the planet."
print(Idea[0:13])  # The Himalayas
print(Idea[-30:-16])  # mountain range
print(f"{Idea[0:13]} {Idea[-14:]}")  # The Himalayas on the planet
#3
string= "There are 9 planets in the solar system"
# Correcting the sentence in one line
string = string.replace('9', '8')
print(string)

empty_string = "AI Engineer"
print(len(empty_string))

print(-9 % 2)

word = "Python"
print("PyT" in word)