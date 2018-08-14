class User(object):
	def __init__(self, name, email):
		self.name = name
		self.email = email
		self.books = {}
	
	def __repr__(self):
		return "User {name}, email: {email}, books read: {book_count}".format(name = self.name, email = self.email, book_count = len(self.books))
	
	def __eq__(self, other_user):
		if (self.name == other_user.name) and (self.email == other_user.email):
			return True
		else:
			return False
	
	def get_email(self):
		return self.email
	
	def get_books(self):
		return self.books
		
	def change_email(self, address):
		old_email = self.email
		self.email = address
		print("{name}'s email address has been changed from {old_email} to {new_email}.".format(name = self.name, old_email = old_email, new_email = self.email))
	
	def read_book(self, book, rating = None):
		self.books[book] = rating
	
	def get_average_rating(self):
		rating_sum = 0
		rating_count = 0
		for v in self.books.values():
			if v:
				rating_sum += v
				rating_count += 1
		try:
			average = rating_sum / rating_count
		except ZeroDivisionError:
			average = 0
		return average

class Book(object):
	def __init__(self, title, isbn, price = 0.0):
		self.title = title
		self.isbn = isbn
		self.price = price
		self.ratings = []
		
	def __repr__(self):
		#I didn't like that for a generic book object there wasn't a custom __repr__.
		return self.title
	
	def __eq__(self, other_book):
		if (self.title == other_book.title) and (self.isbn == other_book.isbn):
			return True
		else:
			return False
	
	def __hash__(self):
		return hash((self.title, self.isbn))
	
	def get_title(self):
		return self.title
	
	def get_isbn(self):
		return self.isbn
	
	def set_isbn(self, new_isbn):
		old_isbn = self.isbn
		self.isbn = new_isbn
		print("{title}'s ISBN has been changed from {old_isbn} to {new_isbn}.".format(title = self.title, old_isbn = old_isbn, new_isbn = self.isbn))
	
	def get_price(self):
		return self.price
	
	def set_price(self, price):
		self.price = price
	
	def add_rating(self, rating):
		if (type(rating) == int) and (rating >= 0) and (rating <= 4):
			self.ratings.append(rating)
		else:
			print("Invalid Rating")
	
	def get_average_rating(self):
		rating_sum = 0
		for rating in self.ratings:
			rating_sum += rating
		try:
			average = rating_sum / len(self.ratings)
		except ZeroDivisionError:
			average = 0
		return average
	

class Fiction(Book):
	def __init__(self, title, author, isbn, price = 0.0):
		super().__init__(title, isbn, price)
		self.author = author
	
	def __repr__(self):
		return "{title} by {author}".format(title = self.title, author = self.author)
	
	def get_author(self):
		return self.author

class Non_Fiction(Book):
	def __init__(self, title, subject, level, isbn, price = 0.0):
		super().__init__(title, isbn, price)
		self.subject = subject
		self.level = level
	
	def __repr__(self):
		return "{title}, a {level} manual on {subject}".format(title = self.title, level = self.level, subject = self.subject)
	
	def get_subject(self):
		return self.subject
	
	def get_level(self):
		return self.level

class TomeRater():
	def __init__(self):
		self.users = {}
		self.books = {}
		#keeping track of the full catalog, regardless of readership
		self.full_catalog = []
	
	def __repr__(self):
		return 'TomeRater object with {users} users and {books} books.'.format(users = len(self.users), books = len(self.books))
	
	def __eq__(self, other_tr):
		equality = True
		for book in self.books:
			if book not in other_tr.books:
				equality = False
				break
		for other_book in other_tr.books:
			if other_book not in self.books:
				equality = False
				break
		for user in self.users:
			if user not in other_tr.users:
				equality = False
				break
		for other_user in other_tr.users:
			if other_user not in self.users:
				equality = False
				break
		return equality
	
	def add_book_to_catalog(self, book):
		if self.isbn_unique(book.get_isbn()):
			self.full_catalog.append(book)
			return True
		else:
			return False
	
	def isbn_unique(self, isbn):
		retval = True
		for book in self.full_catalog:
			if book.get_isbn() == isbn:
				retval = False
				print('The provided ISBN ({isbn}) is not unique.'.format(isbn = isbn))
				break
		return retval
	
	def create_book(self, title, isbn, price=0.0):
		book = Book(title, isbn, price)
		if self.add_book_to_catalog(book):
			return book
		else:
			print("invalid book")
			return None
	
	def create_novel(self, title, author, isbn, price=0.0):
		book = Fiction(title, author, isbn, price)
		if self.add_book_to_catalog(book):
			return book
		else:
			print("invalid novel")
			return None
	
	def create_non_fiction(self, title, subject, level, isbn, price=0.0):
		book = Non_Fiction(title, subject, level, isbn, price)
		if self.add_book_to_catalog(book):
			return book
		else:
			print("invalid non-fiction")
			return None
	
	def add_book_to_user(self, book, email, rating = None):
		if email in self.users.keys():
			self.users[email].read_book(book, rating)
			book.add_rating(rating)
			if book and book in self.books:
				self.books[book] += 1
			elif book and book not in self.books:
				self.books[book] = 1
			if book and book not in self.full_catalog:
				self.add_book_to_catalog(book)
		else:
			print('No user with email {email}!'.format(email = email))
	
	def get_n_most_expensive_books(self, n):
		book_price_dict = {}
		book_price_dict_sorted = {}
		counter = 0
		for book in self.full_catalog:
			if book: #disregard any Nones
				book_price_dict[book.get_title()] = book.get_price()
		for slot in sorted(book_price_dict.items(), key = lambda v: v[1], reverse = True):
			book_price_dict_sorted[slot[0]] = slot[1]
			counter += 1
			if counter >= n:
				break
		return book_price_dict_sorted
	
	def add_user(self, name, email, user_books = None):
		user = User(name, email)
		if email not in self.users:
			if email_address_check(email):
				self.users[email] = user
				if user_books: #ignore book lists that are None types
					for book in user_books:
						if book: #ignore books that are None types
							self.add_book_to_catalog(book)
							self.add_book_to_user(book, email)
			else:
				print('The email address provided ({email}) is not a valid email address.'.format(email = email))
		else:
			print('Email address {email} is already in use.'.format(email = email))
	
	def print_catalog(self):
		for book in self.full_catalog:
			print(book)
	
	def print_users(self):
		for user in self.users:
			print(user)
	
	def get_most_read_book(self):
		most_read = None
		high_read = 0
		for book in self.books:
			if self.books[book] > high_read:
				high_read = self.books[book]
				most_read = book
		return most_read
	
	def get_n_most_read_books(self, n):
		most_read_books = []
		counter = 0
		for book in sorted(self.books.items(), key=lambda v: v[1], reverse = True):
			most_read_books.append(book)
			counter += 1
			if counter >= n:
				break
		return most_read_books
	
	def get_n_most_prolific_readers(self, n):
		most_prolific_readers_dict = {}
		for user in self.users:
			most_prolific_readers_dict[user] = len(self.users[user].books)
		most_prolific_readers = sorted(most_prolific_readers_dict.items(), key = lambda v: v[1], reverse = True)
		most_prolific_readers_truncated = {}
		counter = 0
		for reader in most_prolific_readers:
			most_prolific_readers_truncated[reader[0]] = reader[1]
			counter += 1
			if counter >= n:
				break
		return most_prolific_readers_truncated
	
	def highest_rated_book(self):
		highest_rated_book = None
		highest_rating = 0
		for book in self.books:
			this_rating = book.get_average_rating()
			if this_rating > highest_rating:
				highest_rated_book = book
				highest_rating = this_rating
		return highest_rated_book
	
	def most_positive_user(self):
		most_positive_user = None
		most_positive = 0
		for user in self.users:
			this_positive = self.users[user].get_average_rating()
			if this_positive > most_positive:
				most_positive_user = self.users[user]
				most_positive = this_positive
		return most_positive_user
	
	def get_worth_of_user(self, user_email):
		user = self.get_user_by_email(user_email)
		total_spend = 0.0
		if user:
			for book in self.users[user_email].get_books():
				total_spend += book.get_price()
		return total_spend
	
	def get_user_by_email(self, email):
		retval = None
		for user in self.users:
			if self.users[user].get_email() == email:
				retval = self.users[user]
				break
		return retval

def email_address_check(email):
	if ('@' in email) and ((email[-4:].lower().strip() == '.com') or (email[-4:].lower().strip() == '.edu') or (email[-4:].lower().strip() == '.org')):
		return True
	else:
		return False

