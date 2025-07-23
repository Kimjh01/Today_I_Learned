def count_frequencies(arr):
    """
    배열 원소들의 빈도를 해시맵(dict)으로 세는 함수
    """
    freq = {}
    for x in arr:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1
    return freq

# 예시
if __name__ == "__main__":
    arr = [3, 1, 2, 3, 2, 1, 3]
    freq = count_frequencies(arr)  # {3: 3, 1: 2, 2: 2}
    for k in sorted(freq):
        print(k, freq[k])