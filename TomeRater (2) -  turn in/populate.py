from TomeRater import *

Tome_Rater = TomeRater()

#Create some books:
book1 = Tome_Rater.create_book("Society of Mind", 12345678, 1.5)
novel1 = Tome_Rater.create_novel("Alice In Wonderland", "Lewis Carroll", 12345, 1.99)
novel1.set_isbn(9781536831139)
nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452, 8)
nonfiction2 = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938, 9.95)
novel2 = Tome_Rater.create_novel("The Diamond Age", "Neal Stephenson", 10101010, 14)
novel3 = Tome_Rater.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000, 18.99)
novel4 = Tome_Rater.create_novel("This Book Has A Duplicate ISBN", "Bogus Fakery", 10001000, 22.00)
novel5 = Tome_Rater.create_novel("The Never Read Book - The Price of Being Too Expensive", "Greedy McMoneybags", 987654321, 100)

#Create users:
Tome_Rater.add_user("Alan Turing", "alan@turing.com")
Tome_Rater.add_user("David Marr", "david@computation.org")
#intentionally bogus email address for checking function
Tome_Rater.add_user("David Marr", "davidcomputation.org")
#intentionally bogus email address for checking function
Tome_Rater.add_user("David Marr", "david@computation.ude")

#Add a user with three books already read:
#Correctly prints "Invalid Rating" three times because each book passed in list has no rating provided to pass along to add_book_to_user method
Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", user_books=[book1, novel1, nonfiction1, novel4])
#copied line above to line below to test adding user twice
Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", user_books=[book1, novel1, nonfiction1])

#Add books to a user one by one, with ratings:
Tome_Rater.add_book_to_user(book1, "alan@turing.com", 1)
Tome_Rater.add_book_to_user(novel1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction2, "alan@turing.com", 4)
Tome_Rater.add_book_to_user(novel3, "alan@turing.com", 1)

Tome_Rater.add_book_to_user(novel2, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "marvin@mit.edu", 2)

Tome_Rater.add_book_to_user(novel3, "david@computation.org", 4)


#Uncomment these to test your functions:
print('\nCATALOG')
Tome_Rater.print_catalog()
print('\nUSERS')
Tome_Rater.print_users()

print()

print("Most positive user:")
print(Tome_Rater.most_positive_user())
print()
print("Highest rated book:")
print(Tome_Rater.highest_rated_book())
print()
print("Most read book:")
print(Tome_Rater.get_most_read_book())
print()
print("List of 9 most read books: (truncated if requested list is larger than catalog")
for book in Tome_Rater.get_n_most_read_books(9):
	print('{title} has been read {count} times'.format(title = book[0], count = book[1]))
print()
print("List of 2 most prolific readers: (truncated if requested list is larger than user base)")
top_two = Tome_Rater.get_n_most_prolific_readers(2)
for user in top_two:
	print('{user} has read {book_count} books'.format(user = user, book_count = top_two[user]))
print()
print("List of 2 most expensive books: (truncated if requested list is larger than catalog")
pricey_two = Tome_Rater.get_n_most_expensive_books(2)
for k,v in pricey_two.items():
	print('{title} costs ${price}'.format(title = k, price = v))
print()
print('"Worth" of users')
print('Total spend for {email} is {total_spend}'.format(email = 'alan@turing.com', total_spend = Tome_Rater.get_worth_of_user('alan@turing.com')))
print('Total spend for {email} is {total_spend}'.format(email = 'marvin@mit.edu', total_spend = Tome_Rater.get_worth_of_user('marvin@mit.edu')))
print('Total spend for {email} is {total_spend}'.format(email = 'david@computation.org', total_spend = Tome_Rater.get_worth_of_user('david@computation.org')))
print()
print('End of first Tome_Rater tests')
print()


###################################################

Tome_Rater2 = TomeRater()

#Create some books:
book1 = Tome_Rater2.create_book("Society of Mind", 12345678)
novel1 = Tome_Rater2.create_novel("Alice In Wonderland", "Lewis Carroll", 12345)

#Create users:
Tome_Rater2.add_user("Alan Turing", "alan@turing.com")
Tome_Rater2.add_user("David Marr", "david@computation.org")

#Add books to a user one by one, with ratings:
Tome_Rater2.add_book_to_user(book1, "alan@turing.com", 1)
Tome_Rater2.add_book_to_user(novel1, "alan@turing.com", 3)
Tome_Rater2.add_book_to_user(nonfiction1, "alan@turing.com", 3)
Tome_Rater2.add_book_to_user(nonfiction2, "alan@turing.com", 4)
Tome_Rater2.add_book_to_user(novel3, "alan@turing.com", 1)

#Test calling add_book_to_user() when user doesn't exist
Tome_Rater2.add_book_to_user(novel2, "marvin@mit.edu", 2)
Tome_Rater2.add_book_to_user(novel3, "marvin@mit.edu", 2)

Tome_Rater2.add_book_to_user(novel3, "david@computation.org", 4)


#Uncomment these to test your functions:
print('\nCATALOG')
Tome_Rater2.print_catalog()
print('\nUSERS')
Tome_Rater2.print_users()

print()

print("Most positive user:")
print(Tome_Rater2.most_positive_user())
print()
print("Highest rated book:")
print(Tome_Rater2.highest_rated_book())
print()
print("Most read book:")
print(Tome_Rater2.get_most_read_book())
print()
print("List of 3 most read books: (truncated if requested list is larger than catalog)")
for book in Tome_Rater2.get_n_most_read_books(3):
	print('{title} has been read {count} times'.format(title = book[0], count = book[1]))
print()
print("List of 8 most prolific readers: (truncated if requested list is larger than user base)")
top_three = Tome_Rater2.get_n_most_prolific_readers(8)
for user in top_three:
	print('{user} has read {book_count} books'.format(user = user, book_count = top_three[user]))
print()
print("List of 10 most expensive books: (truncated if requested list is larger than catalog")
pricey_ten = Tome_Rater2.get_n_most_expensive_books(10)
for k,v in pricey_ten.items():
	print('{title} costs ${price}'.format(title = k, price = v))
print()
