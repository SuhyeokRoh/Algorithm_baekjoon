a = [1995, 1998, 1999, 2001, 2002, 2003, 2004, 2005, 2009, 2010 ,2011, 2012, 2014, 2015 ,2016, 2017, 2019]
b = [1996, 1997, 2000, 2007, 2008, 2013, 2018]
n = int(input())

if n in a:
    print('ITMO')
elif n in b:
    print('SPbSU')
else:
    print('PetrSU, ITMO')