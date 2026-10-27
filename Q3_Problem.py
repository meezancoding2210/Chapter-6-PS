p1 = "make a lot of money"
p2 = "buy now"
p3 = "subscribe to this"
p4 = "click this"

a = input("Enter your comment: ")

if((p1 in a) or (p2 in a) or (p3 in a ) or (p4 in a)):
    print("This is a spam")
else:
    print("This is not a spam")