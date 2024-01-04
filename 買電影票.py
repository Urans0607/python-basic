age = int(input("請輸入年齡:"))
student = input("你是不是學生(Y/N):").lower()
money = 0

if age >= 5  and student =="y":
    money = 100
elif age >= 5 and student == "n":
    if 5<= age <= 18:
        money = 120
    else:
        money = 150
    
# if age <5 or student == 'y' :
#     if age<=5:
#         ticket_price = 0
#     else:
#          ticket_price = 100
# else:
#     if age >= 5 and age <= 18:
#         ticket_price = 120
#     else:
#         ticket_price = 150

    
# if age < 5:
#     ticket_price = 0
# elif age >= 5 and age <= 18:
#     if student == "y":
#         ticket_price = 100
#     else:
#         ticket_price = 120
# else:
#     ticket_price = 150

print("您的年齡為:", age)
print("您是否為學生:", student)
print("門票價格為:", money, "元")