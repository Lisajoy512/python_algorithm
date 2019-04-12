def plus_one(digits: [int]) -> [int]:
    if len(digits) == 0:
        return []
    last_n = int(digits[-1])
    if last_n < 9:
        digits[-1] = last_n + 1
        return digits
    else:
        if len(digits) == 1:
            digits.append(1)
            digits.append(0)
            return digits[1:]
        else:
            result = plus_one(digits[:len(digits) - 1])
            result.append(0)
            return result


if __name__ == "__main__":
    print(plus_one([9]))
