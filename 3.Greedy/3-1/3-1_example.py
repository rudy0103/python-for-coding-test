#거스름돈 주기


n = int(input())

number_of_coin = 0

number_of_coin += n//500
# n = n - (500*(n//500))
n%= 500

number_of_coin += n//100
# n = n - (100*(n//100))
n%= 100

number_of_coin += n//50
# n = n - (50*(n//50))
n%= 50

number_of_coin += n//10
# n = n - (10*(n//10))
n%= 10


print(number_of_coin)


# # 책 답안
# n = 1260
# count = 0

# # 큰 단위의 화폐부터 차례대로 확인
# coin_types = [500,100,50,10]

# for coin in coin_types:
#     count += n // coin
#     n %= coin

# print(count)