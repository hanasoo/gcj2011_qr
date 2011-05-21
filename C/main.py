#!/usr/bin/env python
# -*- coding: utf-8 -*-

IN_FILE = 'C-small-attempt1.in'
IN_FILE = 'sample.txt'
OUT_FILE = 'result.txt'

#combinations method from python 2.6
def combinations(iterable, r):
	pool = tuple(iterable)
	n = len(pool)
	if r > n:
		return
	indices = range(r)
	yield tuple(pool[i] for i in indices)
	while True:
		for i in reversed(range(r)):
			if indices[i] != i + n - r:
				break
		else:
			return
		indices[i] += 1
		for j in range(i+1, r):
			indices[j] = indices[j-1] + 1
		yield tuple(pool[i] for i in indices)

def separate(iterable):
	src = tuple(iterable)
	n = len(src)
	indices = set(range(n))
	for i in range(n - 1, n / 2, -1):
		for right in combinations(indices, i):
			left = indices - set(right)
			yield [src[v] for v in right],[src[v] for v in left]

def xor_sum(list):
	val = 0
	for i in list:
		val = val ^ i
	return val

f = open(IN_FILE, 'r')
src = f.read().split('\n')
f.close()

case_num = int(src.pop(0))
case_count = 0
result = ''

for case_count in range(case_num):
	print('############ start #################')
	c_num = int(src.pop(0))
	piles = [int(c) for c in src.pop(0).strip().split(' ')]
	piles.sort()
	piles.reverse()
	print piles
	for p in separate(piles):
		print "try: %s bsum=%d sum=%d,%d" % (p, xor_sum(p[0]), sum(p[0]), sum(p[1]))
		if xor_sum(p[0]) == xor_sum(p[1]):
			print "hit: %s bsum=%d sum=%d,%d" % (p, xor_sum(p[0]), sum(p[0]), sum(p[1]))
			#result += 'Case #%d: %d\n' % (case_count + 1, sum(p[0]))
			#break
	else:
		result += 'Case #%d: NO\n' % (case_count + 1)
	print('############ end #################')

f = open(OUT_FILE, 'w')
f.write(result)
f.close()


