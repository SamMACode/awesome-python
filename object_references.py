# charles and lewis refer to the same object
charles = {'name': 'Charles L. Dodgson', 'born': 1832}
lewis = charles
print(f"lewis = charles: {lewis is charles}")
lewis['balance'] = 950
# id(charles): 140257173710720, id(lewis): 140257173710720, charles: {'balance': 950}
print(f"id(charles): {id(charles)}, id(lewis): {id(lewis)}, charles['balance']: {charles['balance']}")
alex = {'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 950}
# is operator is used to compare id(object), == only compare field value
print(f"charles is alex: {charles is alex}, charles equals charles: {charles == alex}")


