#! /usr/bin/env python
''' Show that for N people, when N = 23 or greater it is more likely than not
    that two out of the N people have the same birthday.  Assume that birthdays
    are uniformly randomly distributed throughout the year and that we have a
    random sample of people.  This example is adapted from David J. Hand's
    "The Improbability Principle" (2014), page 89.
'''

def main():

    '''
    P is the probability that any two out of the N people have the same
    birthday as each other (does not matter which two, any pair amongst
    the N people is acceptable).

    It is easier to calculate Q = 1 - P, where Q is the probability
    that NO two of the people have the same birthday.  To calculate Q,
    consider the case N = 3.  Q is the probability that the third
    person does not have the same birthday as either the first or
    second person (hence multiplying these two terms):

        Q = 364/365 * 363/365 = 0.9918

    So for N = 3, the chance of any pair having the same B-day
    is 1 - Q = P = 0.0082 = 0.82%, a very small chance.

    As N increases, Q starts to drop, until finally P > 50%.  The
    general formula for Q as a function of N is a product of N-1 terms:

        Q(N) = 364/365 * ... * (366 - N)/365

    or more compactly using factorials:

        Q(N) = 365! / [ (365-N)! * 365**N ]
    '''

    N = 1   # start with a single person
    Q = 1.  # for N = 1, 100% chance no one else w/same B-day
    P = 0.  # for N = 1,   0% chance anyone else w/same B-day

    # keep increasing N in a loop until desired probability P reached
    while P < 0.50:

        # multiply on next factor in the product series for Q(N)
        Q *= (366. - N) / 365.
        P = 1. - Q

        print("By N = %2i, P = %.1f%%" % (N, 100*P))
        N += 1      # increment N for next loop

    print()

    '''
    Alternately, use the analytic expression for Q(N).
    Note the purposeful use in math.factorial() of all ints, not floats!
    '''
    from math import factorial as fac
    def Q(N):
        return fac(365) / ( fac(365-N) * 365**N )

    N = 1
    P = 0.
    while P < 0.50:

        P = 1. - Q(N)
        print("For N = %2i, P = %.1f%%" % (N, 100*P))
        N += 1


if (__name__ == '__main__'):
    main()
