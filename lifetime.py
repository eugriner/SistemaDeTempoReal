#!/usr/bin/python3
from __future__ import unicode_literals
# -*- coding: utf-8 -*-
import time
from time import gmtime, strftime

def main():
  print("Data de nascimento")
  # day = input('Dia: ')
  # month = input('Mes: ')
  # year = input('Ano: ')
  # hour = input('Hora: ')
  # minute = input('Minuto: ')
  # second = input('Segundo: ')
  day = 28
  month = 6
  year = 1989
  hour = 0
  minute = 0
  second = 0
  # t = (2009, 2, 17, 17h, 3m, 38s, 1, 48, 0)
  # Index Attribute Values
  # 0 tm_year (for example, 1993)
  # 1 tm_mon  range [1, 12]
  # 2 tm_mday range [1, 31]
  # 3 tm_hour range [0, 23]
  # 4 tm_min  range [0, 59]
  # 5 tm_sec  range [0, 61]; see (2) in strftime() description
  # 6 tm_wday range [0, 6], Monday is 0
  # 7 tm_yday range [1, 366]
  # 8 tm_isdst  0, 1 or -1; see below

  age = (year, month, day, hour, minute, second, 1, 52 , 0)
  now = gmtime()
  # print (strftime("%Y-%m-%d %H:%M:%S", now))
  # print (strftime("%Y-%m-%d %H:%M:%S", age))
  # print (time.mktime( now )/(60*60*24*30*12))
  # print (time.mktime( age ))

  secs = time.mktime( now ) - time.mktime( age )
  print ("Voce viveu exatamente: %d segundos" %  (secs))
  print ("Voce viveu aproximadamente: %f anos" %  (secs/(60*60*24*365)))
  # print "asctime(localtime(secs)): %s" % time.asctime(time.localtime(secs)


if __name__ == '__main__':
  main()