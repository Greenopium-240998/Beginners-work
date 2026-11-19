while True:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    height = int(input("Enter your height (cm): "))
    weight = int(input("Enter your weight (kg): "))
    bmi = weight / height / height * 10000

    if age < 20:
        print(f"Hi {name}, please follow the children BMI chart")
    else:
        if age < 65:
            low, high = 18.5, 25
        else:
            low, high = 23, 30

        if bmi < low:
            msg = "You need to increase your intake"
        elif bmi < high:
            msg = "You are healthy"
        else:
            msg = "Pay attention to your diet"
        print(f"Hi {name}, your BMI is {bmi:.1f}. {msg}")

    again = input("Try again? (y for yes): ")
    if again.lower() != "y":
        break
