is_Male = False
is_Tall = False

if is_Male:
    print("You are a male")
else:
    print("You are not a male")


if is_Male or is_Tall:
    print("You are either male or tall or both")
else:
    print("You are neither male or tall")


if is_Male and is_Tall:
    print("You are a tall male")
else:
    print("You are either not male or not tall or both")


if is_Male and is_Tall:
    print("You are a tall male")
elif is_Male and not(is_Tall):
    print("You are a short male")
elif not(is_Male) and is_Tall:
    print("You are a not a male but tall")
else:
    print("You are not a male and not tall")