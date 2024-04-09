def find_max_length_cable(lan, n):
    start, end = 1, max(lan)

    while start <= end:
        mid = (start + end) // 2
        total_len = sum(i // mid for i in lan)

        if total_len >= n:
            start = mid + 1
        else:
            end = mid - 1

    return end

k, n = map(int, input().split())
lan = [int(input()) for _ in range(k)]

max_length = find_max_length_cable(lan, n)
print(max_length)