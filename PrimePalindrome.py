import math


def primePalindrome(N: int) -> int:
    if digitCount(N) == 1:
        return N
    else:
        while True:
            nextPal = findNextPalindrome(N)
            if isPrime(nextPal):
                pass
            backDig = curr_temp % 10
            # print (curr, curr_temp, frontDig, backDig)
            # input()
            if frontDig != backDig:
                flag = 1
                break
            curr_temp = curr_temp % (10 ** (frontPtr))
            frontPtr -= 2
            # print (curr_temp)
            curr_temp = curr_temp // (10)
            # print (curr_temp)
        if flag == 0:
            # print(curr)
            # input()
            return curr
        else:
            curr += 1


def main():
    print(primePalindrome(9989900))


if __name__ == "__main__":
    main()
