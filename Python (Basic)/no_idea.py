count_n, count_m = input().split()
input_integers = input().split()
like_group = set(input().split())
dislike_group = set(input().split())
happiness_score = 0

for n in input_integers:
    if n in like_group:
        happiness_score += 1
    elif n in dislike_group:
        happiness_score -= 1
print(happiness_score)
