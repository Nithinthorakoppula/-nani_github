# nani={1:"names",2:"nan",12:"true"}
# # nani["nan"]="nin"
# print(nani)
# print(nani.items())
# nani.pop(2)
# print(nani)

# for i,y in nani.items():
#     print(i,y)


# tuple
# t1=(1,3,5)
# t2=(2,4,6)
# new=[]
# for i,j in zip(t1,t2):
#     new.append(i+j)
# print(new)


# name="nithin"
# password="123"
# user_name=input("enter the user name:")
# passwords=input("enter the password:")
# s='''
#     1.credit
#     2.debit
#     3.mini statement
#     4.exit
# '''
# amount=1000
# if name==user_name and passwords==password:
#     while True:
#         print(s)
#         option=int(input("enter the option:"))
#         if option==1:
#             credit_amount=float(input("enter the amount:"))
#             print("amount after credit",amount+credit_amount)
#         elif option==2:
#             debit_amount=float(input("enter the amount:"))
#             print("amount after debit:",amount-debit_amount)
#         elif option==3:
#             print("amount",amount)
#         elif option==4:
#            break

# else:
#     print("incorrect")

