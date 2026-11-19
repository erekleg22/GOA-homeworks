#შექმენით პროგრამა while ციკლით რომელიც მომხარებელს შეეკითხება pin კოდს (4 ციფრიანი კოდი) იქამდე სანამ არ შემოიყვანს სწორად, საბოლოოდ დაუბეჭდეთ რომ გაიარა ავტორიზაცია და გამოუტანეთ თუ რამდენი ცდა დასჭირდა


corret_pin = "1234"
attempts = 0
user_pin = ""

while user_pin != corret_pin:
    user_pin = input("enter pin code: ")
    attempts += 1

    if user_pin != corret_pin:
        print("wrong try again: ")

print("successfull, you needed", attempts, "attempt")