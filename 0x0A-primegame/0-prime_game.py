#!/usr/bin/python3
"""0. Prime Game - Maria and Ben are playing a game"""


def isWinner(x, nums):
    """Determines the winner of the game.

    Args:
        x (int): Number of rounds.
        nums (list): List of integers representing the upper bounds for each round.

    Returns:
        str: Name of the winner ("Ben", "Maria") or None if there's no winner.

    Raises:
        ValueError: If x is non-positive or nums is None.
        ValueError: If the length of nums is not equal to x.
    """
    if x <= 0:
        raise ValueError("Number of rounds (x) should be positive.")
    if nums is None:
        raise ValueError("List of upper bounds (nums) cannot be None.")
    if x != len(nums):
        raise ValueError("Number of rounds (x) should match the length of nums.")

    ben = 0
    maria = 0

    primes = sieve_of_eratosthenes(max(nums))

    for i in nums:
        if sum(primes[:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1

    if ben > maria:
        return "Ben"
    elif maria > ben:
        return "Maria"
    else:
        return None


def sieve_of_eratosthenes(n):
    """Generates a list of prime numbers up to n using the Sieve of Eratosthenes algorithm."""
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    return primes

