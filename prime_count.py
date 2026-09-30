#!/usr/bin/env python3
"""Count primes less than or equal to a limit using a sieve."""

import argparse
from math import isqrt


def count_primes(limit: int) -> int:
    """Return the number of primes <= limit using the Sieve of Eratosthenes.

    Uses O(limit log log limit) time and O(limit) memory.
    """
    if limit < 2:
        return 0

    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"

    for prime in range(2, isqrt(limit) + 1):
        if sieve[prime]:
            # Smaller multiples have already been marked by smaller primes.
            start = prime * prime
            count = (limit - start) // prime + 1
            sieve[start : limit + 1 : prime] = b"\x00" * count

    return sum(sieve)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("limit", type=int, help="inclusive upper bound")
    args = parser.parse_args()
    print(count_primes(args.limit))


if __name__ == "__main__":
    main()
