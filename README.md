# Advent of Code 2025

Solutions for [Advent of Code 2025](https://adventofcode.com/) in Python.

## 01
- edge case on starting from 0
- + and - handling for mod
- simple while can fix issue
- linear thinking for circular problems - count multiples crossed instead of simulating
- integer division for boundaries - `(n // 100) * 100` finds nearest multiples

## 02
- care max number of partition
- `for-else` - detects loop completion without break
- divisibility filters patterns early - `len % k == 0` before checking

## 03
- finding max value, greedy might work
- suffix constraint - when picking k items, leave room for remaining picks
- greedy works for lex-max - highest digit first always wins 