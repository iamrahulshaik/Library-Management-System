# This code is a simple library management system that allows students to borrow books.
class Books:
    def __init__(self, book_name, book_id):
        self.book_name = book_name
        self.book_id = book_id

    def __str__(self):
        return self.book_name

    @classmethod
    def generate_obj(cls, book_info):
        book_name, book_id = book_info.split("-")
        return cls(book_name.strip(), int(book_id))


class Students:
    def __init__(self, student_name):
        self.student_name = student_name
        self.borrowed_books = []

    def get_student_name(self):
        return self.student_name

    def borrow(self, book):
        if book in self.borrowed_books:
            print(f"{self.student_name} has already borrowed '{book}'.")
        else:
            self.borrowed_books.append(book)

    def show_books(self):
        return self.borrowed_books


class Library:
    def show_all_books(self, student, number):
        book_data = student.show_books()
        if book_data:
            book_list = " , ".join(str(book) for book in book_data)
            print(f"Student {number}: {student.get_student_name()} borrows: {book_list}")
        else:
            print(f"Student {number}: {student.get_student_name()} has not borrowed any books.")


# Create book store as a dictionary
store = ["python-1", "data science-2", "sql-3", "html-4", "java-5",
         "c++-6", "javascript-7", "c#-8", "php-9", "ruby-10"]

dict_of_books = {}
for b in store:
    book_obj = Books.generate_obj(b)
    dict_of_books[book_obj.book_id] = book_obj

# Display available books
print("\nAvailable Books:")
for book in dict_of_books.values():
    print(f"{book.book_id}: {book}")

students_list = []
student_count = 1  # Initialize count

while True:
    name = input(f"\nEnter the name of student {student_count} (or 0/stop to finish): ").strip()
    if name.lower() in ["0", "stop"]:
        break

    student = Students(name)

    while True:
        book_id_input = input(f"Enter book ID for {name} to borrow (or 0/stop to finish): ").strip()
        if book_id_input.lower() in ['0', 'stop']:
            break
        if not book_id_input.isdigit() or int(book_id_input) not in dict_of_books:
            print("Invalid book ID. Try again.")
            continue

        student.borrow(dict_of_books[int(book_id_input)])

    students_list.append(student)
    student_count += 1  # Increment for next student

# Show borrowed books for each student with numbering
lib = Library()
print("\n📚 Borrowed Books Summary:")
for index, stu in enumerate(students_list, start=1):
    lib.show_all_books(stu, index)



