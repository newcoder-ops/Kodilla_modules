# A recursive function that
# check a str[s..e] is
# palindrome or not.
def is_PalRec(st, s, e) :
	
	# If there is only one character
	if (s == e):
		return True

	# If first and last
	# characters do not match
	if (st[s] != st[e]) :
		return False

	# If there are more than
	# two characters, check if
	# middle substring is also
	# palindrome or not.
	if (s < e + 1) :
		return is_PalRec(st, s + 1, e - 1);

	return True

def is_Palindrome(st) :
	n = len(st)
	
	if (n == 0) :
		return True
	
	return is_PalRec(st, 0, n - 1);

st = "geeg"
if (is_Palindrome(st)) :
	print ("Yes")
else :
	print ("No")