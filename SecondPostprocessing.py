#!/usr/bin/python
# -*- coding: utf-8 -*-
def SecondPostprocessing(word):
    try:

      if word=='া':
        str = '।'
      elif word == "ত" and word == "ভ":
          return 0
      else:
          return word

    except:
        1