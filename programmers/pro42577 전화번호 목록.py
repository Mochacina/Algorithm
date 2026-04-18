def solution(phone_book):
    sort_book = sorted(phone_book)
    for i in range(len(sort_book)-1):
        arg = sort_book[i]
        next = sort_book[i+1]
        if len(arg) < len(next):
            if arg == next[:len(arg)]:
                return False
    return True

print(solution(["123","456","789"]))

# def solution(phoneBook):
#     phoneBook = sorted(phoneBook)

#     for p1, p2 in zip(phoneBook, phoneBook[1:]):
#         if p2.startswith(p1):
#             return False
#     return True