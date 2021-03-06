from collections import defaultdict


def solution(numbers):
    numbers = map(str, numbers)
    numbers = sorted(numbers, key=lambda x: ((x*4)[:4]), reverse=True) 
    return str(int(''.join(numbers)))


if __name__ == "__main__":
    print(solution([6, 10, 2]))
    print(solution([3, 30, 34, 5, 9]))
    print(solution([12, 121]))
    print(solution([121, 12]))
    print(solution([40, 404]))
