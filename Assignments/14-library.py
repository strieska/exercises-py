f = open("14-library.txt")
lines = f.readlines()
total_count = 0
total_value = 0
books_to_order = []
for line in lines:
    book_id, count, value = line.split(" ")
    total_count += int(count)
    total_value += int(count) * float(value)
    if int(count) < 10:
        books_to_order.append(book_id)
print(total_count)
print(total_value)
print(books_to_order)