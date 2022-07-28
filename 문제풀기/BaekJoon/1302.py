N = int(input())

books = {}

for _ in range(N):
    book = input()
    if book in books:
        books[book] += 1
    else:
        books[book] = 1

rank_1 = max(books.values())

book_rank = []

for k, v in books.items():
    if v == rank_1:
        book_rank.append(k)

print(sorted(book_rank, reverse = False)[0])
