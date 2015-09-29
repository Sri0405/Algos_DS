

x = int(raw_input())
y = int(raw_input())

while (y!=0):
	carry = x&y
	x =x^y
	y = carry<<1

print x