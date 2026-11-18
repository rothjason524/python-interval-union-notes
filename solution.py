def merge(intervals):
    result = []
    for start, end in sorted(intervals):
        if start > end:
            raise ValueError('reversed interval')
        if result and start <= result[-1][1]:
            result[-1][1] = max(result[-1][1], end)
        else:
            result.append([start, end])
    return result

def solve(value):
    return merge(value)
