#!/usr/bin/python3
"""
This script defines isWineer() function that resolve the Prime Game problem
"""


def isPrime(n):
    """Return list of prime numbers between 1 and n inclusive
    """
    prime = []
    seg_sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if (seg_sieve[p]):
            prime.append(p)
            for i in range(p, n + 1, p):
                seg_sieve[i] = False
    return prime


def isWinner(x, nums):
    """
    Determines winner of Prime Game
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for i in range(x):
        prime = isPrime(nums[i])
        if len(prime) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
