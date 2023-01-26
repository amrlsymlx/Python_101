
# function begin

def say_hi (name, age):
    print("Hello "+ name)
    print("This is my first Python function")
    print("Your age is: "+str(age)+" years old")

# function end

user_name = input("Enter your name:")
user_age = input("Enter your age:")

# call the function
say_hi(user_name, user_age) 

