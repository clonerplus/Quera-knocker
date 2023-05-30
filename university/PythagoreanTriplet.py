# Python3 program to find the Pythagorean
# Triplet with a given sum

# Function to calculate the
# Pythagorean triplet in O(n)


def PythagoreanTriplet(n):
    flag = 0

    # Iterate a from 1 to N-1.
    for a in range(1, n, 1):

        # Calculate value of b
        b = (n * n - 2 * n * a) // (2 * n - 2 * a)

        # The value of c = n - a - b
        c = n - a - b

        if (a * a + b * b == c * c
                and b > 0 and c > 0):
            print(a, b, c)
            flag = 1
            break

    if flag == 0:
        print("Impossible")

    return


# Driver code
if __name__ == '__main__':
    N = int(input())

    # Function call
    PythagoreanTriplet(N)

# This code is contributed by Bhupendra_Singh

