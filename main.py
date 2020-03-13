import time
import turtle
import sys
t = turtle
ti = time.asctime()

print("How much do you want it?")
a = int(sys.stdin.readline())
print("Witch color? RED")
b = float(sys.stdin.readline())
print("Witch color? GREEN")
c = float(sys.stdin.readline())
print("Witch color? BLUE")
d = float(sys.stdin.readline())

t.color(b, c, d)

t.title("Creator of polygons")


def lato():
	for x in range(0,8):
		if x % 2 == 0:
			t.begin_fill()		

		else:
			t.end_fill()

	
		for x in range(0,4):
			t.forward(10)
			t.right(90)
		t.forward(10)


for x in range(0,a):
	lato()
	t.left(360 / a)

t.end_fill()

f = open("disegno_info.txt", "w+")
f.write("""
/###########################################/
Your number is %s
-------------------------------------------
The created date is %s
/###########################################/""" % (a, ti))
f.close()
