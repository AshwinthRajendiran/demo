#!/usr/bin/env python3
import sys

cur_word = None
cur_count = 0

for line in sys.stdin:
    try:
       word , count = line.strip().split("\t")
       count=int(count)
    except ValueError:
       continue

    if cur_word == word:
       cur_count+=count
    else:
       if cur_word:
          print(f"{cur_word}\t{cur_count}")
       cur_word = word
       cur_count = count
if cur_word:
    print(f"{cur_word}\t{cur_count}")