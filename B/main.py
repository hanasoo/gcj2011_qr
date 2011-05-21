#!/usr/bin/env python
# -*- coding: utf-8 -*-

IN_FILE = 'B-large.in'
#IN_FILE = 'sample.txt'
OUT_FILE = IN_FILE.replace('.in', '.out')


class CombineRule():
	def __init__(self, str):
		self.s1 = str[0:2]
		self.s2 = str[1] + str[0]
		self.s3 = str[2]
		print 'combine_rule: %s or %s to %s' % (self.s1, self.s2, self.s3)
	
	def proc(self, src):
		target = src[len(src)-2:]
		#print '### target: %s' % target
		if target == self.s1 or target == self.s2:
			return src[:len(src)-2] + self.s3
		return src

class OpposeRule():
	def __init__(self, str):
		self.s1 = str[0]
		self.s2 = str[1]
		print 'oppose_rule: %s %s' % (self.s1, self.s2)
	
	def proc(self, src):
		if self.s1 in src and self.s2 in src:
			#pos1 = src.find(self.s1)
			#pos2 = src.find(self.s2)
			#pos1, pos2 = (pos1, pos2) if pos1 < pos2 else (pos2, pos1)
			#return src.replace(src[pos1:pos2+1], '')
			return ''
		else:
			return src

def spell(str):
	result = ''.join([s + ' ' for s in str]).strip()
	result = '['  + result.replace(' ', ', ') + ']'
	return result

f = open(IN_FILE, 'r')
src = f.read().split('\n')
f.close()

case_num = int(src.pop(0))
case_count = 0
result = ''

for case_count in range(case_num):
	print('############ start #################')
	line = src.pop(0).strip().split(' ')
	
	c_rules = []
	c_num = int(line.pop(0))
	for i in range(c_num):
		c_rules.append(CombineRule(line.pop(0)))
	
	o_rules = []
	o_num = int(line.pop(0))
	for i in range(o_num):
		o_rules.append(OpposeRule(line.pop(0)))
	
	m_num = int(line.pop(0))
	magic1 = line.pop(0)
	magic2 = magic1[0]
	print 'Magic_before: %s' % magic1
	for i in range(1, m_num):
		magic2 += magic1[i]
		for c in c_rules:
			magic2 = c.proc(magic2)
		for o in o_rules:
			magic2 = o.proc(magic2)
	print 'Magic_after : %s' % spell(magic2)
	
	result += 'Case #%d: %s\n' % (case_count + 1, spell(magic2))
	print('############ end #################')

f = open(OUT_FILE, 'w')
f.write(result)
f.close()


