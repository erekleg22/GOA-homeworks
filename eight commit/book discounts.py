#2) შექმენით 5 ცვლადი რომლებშიც შეინახავთ წიგნების თავდაპირველ ფასს, შემდეგ შექმენით ცვლადი რომელშიც შეინახავთ ფასდაკლების ოდენობას, შექმენით ახალი ფასის მქონე წიგნების ცვლადები, რომელთა მნიშვნელობა იქნება ძველ მნიშვნელობას გამოკლებული ახალი, საბოლოოდ კი დაბეჭდეთ ახალი წიგნების ფასები (გამოიყენეთ კარგი მიდგომები: რომ ცვლადის მნიშვნელობის მინიჭებისას შეგიძლიათ სხვა ცვლადის გამოყენება, კოდი ახსენით კომენტარების საშვალებით, ცვლადებს დაარქვით აღმწერი სახელები snake_case-ის სტილში)

#putting original prices
book_1 = 100
book_2 = 22
book_3 = 15
book_4 = 60
book_5 = 49

#putting the discount ammount
discount = 25

#putting the new book prices (including discounts)
book_1_new = book_1 - (book_1 * discount / 100)
book_2_new = book_2 - (book_2 * discount / 100)
book_3_new = book_3 - (book_3 * discount / 100)
book_4_new = book_4 - (book_4 * discount / 100)
book_5_new = book_5 - (book_5 * discount / 100)

#printing the new prices
print(book_1_new)
print(book_2_new)
print(book_3_new)
print(book_4_new)
print(book_5_new)