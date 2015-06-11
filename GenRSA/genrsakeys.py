#!/usr/bin/python
from math import sqrt
import os, sys

def phi(a, b):
    return ((a-1)*(b-1))

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

def modinv(a, m):
    g,x,y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x%m

def verif_e(e, phi_n):
    if ( 1 > e ) and ( e > phi_n ):
        raise Exception('incorrect value for e')
        sys.exit() 
    if ( pgcd(e, phi_n) != 1):
        raise Exception('incorrect value for e')
        sys.exit() 

p = 31
q = 37
e = 7

n = p * q

phi_n = phi(p, q)

verif_e(e, phi_n)
d = modinv(e, phi_n)

print "p: ", p
print "q: ", q
print "e: ", e
print "phi_n: ", phi_n
print "n: ", n
print "d: ", d

