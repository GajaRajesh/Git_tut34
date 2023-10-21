def paln(pal):
    if(pal.lower()==pal.lower()[::-1]):
        print(pal, "is a palindrom ")
    else:
        print(pal, "is not a palindrom")
pal=input("enter a String: ")
paln(pal)