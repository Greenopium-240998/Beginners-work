#insert <std.io>
while True:	
    a=input("enter your name ")
    b=int(input("enter your age "))
    c=int(input("enter your height (in cms) "))
    d=int(input("enter your weight (in kgs)"))
    bmi=d/c/c*10000
    y=False
    z=False
    x=False
    if b>20 and b<65:
    	y=True
    elif b<20:
        z=True
    else:
    	x=True
    if y==True and bmi<18.5:
    	print("Hi " + str(a) + " your BMI is " + str(bmi) + " and You need to increase your intake\n. ")
    elif y==True and bmi<25:
    	print("Hi, " + str(a) + " your BMI is " + str(bmi) + " and You are quite healthy")
    elif y==True and bmi>25 and bmi<30:
    	print(bmi)
    	print("Hi, " + str(a) + " your BMI is " + str(bmi) + " and You need to pay attention to your diet")
    elif y==True and bmi>30:
    	print("your bmi is " + bmi)
    	print("Hi, " + str(a) + " your BMI is " + str(bmi) + " and You are obese")
    elif z==True:
    	print("Hi, " + str(a) + " Please follow the children BMI chart")
    elif x==True and bmi>23 and bmi<30:
    	print("Hi " + str(a) + " Your BMI is " + str(bmi) + "and you are healthy for your age")
    elif x==True and bmi<23:
    	print("Hi, "  + str(a) + " Your BMI is " + str(bmi) + " You are lacking in intake")
    elif x==True and bmi>30:
    	print("Hi, " + str(a) + "Your BMI is " + str(bmi) + " and you are obese ")
    again=input("Do you want to try again? Please type y for yes ")
    if again.lower()!="y"::
    	break
    	
	
