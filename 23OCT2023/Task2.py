def alpha(str1):
    count=0;
    for i in str1.lower():
        if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
            count+=1;
    print("number of consonents: ", count)
    print("number of consonents: ",(abs(len(str1)-count)))
str1=input("Enter a String: ")
alpha(str1)