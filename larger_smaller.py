first = int(input("Enter thr first number:"))
second = int(input("Enter the second number:"))
if first>second:
	larger = first
	smaller = second
else:
	larger = second
	smaller = first
print("Larger Number=",larger)
print("Smaller Number=",smaller)