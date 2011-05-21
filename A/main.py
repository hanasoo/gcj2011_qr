#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Button:
	def __init__(self, step_num, color, pos):
		self.color = color
		self.pos = int(pos)
		self.step_num = step_num
		
	def __str__(self):
		return "%s: %s: %s" % (self.step_num, self.color, self.pos)

class Hallway:
	def __init__(self, str_line):
		chars = str_line.strip().split(' ')
		self.button_num = int(chars.pop(0))
		self.buttons = []
		for i in range(self.button_num):
			self.buttons.append(Button(i, chars.pop(0), chars.pop(0)))
			
	def __str__(self):
		return str([str(b) for b in self.buttons])

class Bot:
	def __init__(self, color):
		self.color = color
		self.pos = 1
		self.tasks = []
	
	def look(self, hallway):
		self.tasks = []
		self.pos = 1
		for b in hallway.buttons:
			if b.color == self.color:
				self.tasks.append(b)
		print [str(t) for t in self.tasks]
	
	def action (self, step):
		str = '%s at %s, ' % (self.color, self.pos)
		if len(self.tasks) == 0:
			print '%s end' % str
			return False
		if self.pos != self.tasks[0].pos:
			self.pos += 1 if self.pos < self.tasks[0].pos else -1
			print '%s goes to %s looking %s' % (str, self.pos, self.tasks[0].pos)
			return False
		if step != self.tasks[0].step_num:
			print '%s waiting' % (str)
			return False
		else:
			print '%s push!!' % (str)
			self.tasks.pop(0)
			return True


lines = 0
f = open('A-large.in', 'r')
bo = Bot('O')
bb = Bot('B')
case_count = 0
result = ''

for line in f:
	if lines == 0:
		lines = int(line)
	else:
		case_count += 1
		print('############ start #################')
		h = Hallway(line)
		print h
		bo.look(h)
		bb.look(h)
		step = 0
		time = 0
		while(step < h.button_num):
			boflag = bo.action(step)
			bbflag = bb.action(step)
			if boflag or bbflag:
				step += 1
			time += 1
			
		result += 'Case #%d: %d\n' % (case_count, time)
		print('############ end #################')
		
f.close()

f = open('result.txt', 'w')
f.write(result)
f.close()

