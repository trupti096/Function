age=int(input("enter_a_age="))
def eligible_for_vote(age):
    if age<18:
        print("not eligible")
    elif age>18:
        print("you are eligible")
eligible_for_vote(age)