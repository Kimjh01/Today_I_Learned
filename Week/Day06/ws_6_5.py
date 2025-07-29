def ordered_difference_sets(set1, set2):
    diff1 = set1 - set2
    diff2 = set2 - set1

    if not diff1:
        return (diff1, diff2)
    elif not diff2:
        return (diff2, diff1)
    elif len(diff1) >= len(diff2):
        result = (diff1, diff2)
    else:
        result = (diff2, diff1)

    return result

# 예시 실행
result = ordered_difference_sets({1, 2, 3, 4}, {3, 4, 5, 6})
print("결과:", result)  # 출력: ({1, 2}, {5, 6})

result = ordered_difference_sets({1, 2, 3, 4}, {1, 2, 3})
print("결과:", result)  # 출력: (set(), {4})
