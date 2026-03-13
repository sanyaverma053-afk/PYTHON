
str1="WelcomeToTheConsole "
print(str1.isalnum())
print(str1.isalpha())
print(str1.islower())
print(str1.isprintable())

str1="  "
print(str1.isspace())

str1="world health organization"
print(str1.istitle())


a="HELLO"
print(a.isupper())

str1="Python is a Interpreted Language"
print(str1.startswith("Python"))
print(str1.swapcase())
print(str1.title())

str1="hello"
print(str1.capitalize())

str2="welcome to the console"
print(str2.center(50))

a="Harry is  Harry without his name Harry"
print(a.count("Harry"))

str1="welcome to the console"
print(str1.endswith("console"))


str1="welcome to the console !!!"
print(str1.endswith ("to",4,10))
