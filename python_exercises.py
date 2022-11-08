#Cube Number Test... Print out all cubed numbers up to the total value 1000. Meaning that if the cubed number is over 1000 break the loop.
for num in range(11):
    answer = num**3
    print(num, answer)


#Get first prime numbers up to 100
for num in range(1, 100):
    count = 0
    for i in range(2, (num//2 + 1)):
        if(num % i == 0):
            count = count + 1
            break
    if(count == 0 and num != 1):
        print("%d" %num, end = ' ')


#Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors
age_query = input("What is your age?")
age_query = int(age_query)

if age_query > 18:
    if age_query < 65:
        print("Adults")
    else:
        print("Seniors")
else:
    print("Kids")