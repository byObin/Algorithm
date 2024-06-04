n = int(input())
num_cards = set(map(int, input().split()))

m = int(input())
have_cards = list(map(int, input().split()))

result = [1 if card in num_cards else 0 for card in have_cards]

print(' '.join(map(str, result)))