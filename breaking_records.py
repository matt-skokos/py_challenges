def breaking_records(scores):
    max_min = [0, 0]
    max_score = 0
    min_score = 0
    for idx, num in enumerate(scores):
        if idx == 0:
            max_score = scores[idx]
            min_score = scores[idx]
            print(max_score)
            print(min_score)
        elif idx == (len(scores) - 1):
            if scores[idx] > max_score:
                max_score = scores[idx]
                max_min[0] += 1
            elif scores[idx] < min_score:
                min_score = scores[idx]
                max_min[1] += 1
        elif scores[idx] > max_score:
            max_score = scores[idx]
            max_min[0] += 1
        elif scores[idx] < min_score:
            min_score = scores[idx]
            max_min[1] += 1
    return max_min

    # takes in a list, returns a list of 0's or 1's
    # 0 or 1 depends on whether she breaks her record
    # 12 is first > 24 is second ( 1 )


# if index is zero set min and max scores
# compare this first index with the next and return 1 if


# scores1 = [1, 2, 3, 4]
scores1 = [10, 5, 20, 20, 4, 5, 2, 25, 1]

print(breaking_records(scores1))
