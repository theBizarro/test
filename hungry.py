hungry = input("Tell if you are hungry : ")

if hungry == "yes":
    print("eat samosa")
    print("eat pizza")
    print("eat burger")
    thirsty = input("Are you thirsty also : ")
    if thirsty == "yes":
        print("drink soda")
    else:
        print("eat and go outside")

else:
    exercise = input("Have you exercised yet :")
    if exercise == "yes":
        print("you can go home and rest")
    else:
        print("go and exercise outside")