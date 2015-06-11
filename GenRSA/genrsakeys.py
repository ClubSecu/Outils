#!/usr/bin/python

"""
    Author : Nomekrax
    Creation : 11/06/2015
    Last modification : 11/06/2015
    Informations : Python 2.7.3
"""

from math import sqrt
import os, sys

""" Function to calculate phi of two numbers """
def phi(a, b):
    return ((a-1)*(b-1))

""" Function to search pdcg of two numbers """
def pgcd(a, b):
    if (b==0) :
        return (a)
    else :
        r = a%b
        return pgcd(b, r)


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g,y,x = egcd(b%a,a)
        return (g, x-(b//a)*y, y)

""" Opposite of modulo function """
def modinv(a, m):
    g,x,y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x%m

""" Function to check if value of e is correct
        Check if 1 < e < phi(n)
        Check if pgcd(e, phi(n)) = 1
"""
def verif_e(e, phi_n):
    if ( 1 > e ) and ( e > phi_n ):
        raise Exception('incorrect value for e')
        sys.exit() 
    if ( pgcd(e, phi_n) != 1):
        raise Exception('incorrect value for e')
        sys.exit() 

""" Variables """
""" p and q need to be private """
p = 31
q = 37
""" e and n are public """
e = 7

""" Get value of n """
n = p * q
""" Get phi(n) """
phi_n = phi(p, q)
""" Verifying if e value is correct """
verif_e(e, phi_n)
""" Get d """
d = modinv(e, phi_n)

""" Show all values """
print "p: ", p
print "q: ", q
print "e: ", e
print "phi_n: ", phi_n
print "n: ", n
print "d: ", d
