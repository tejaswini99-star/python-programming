val = str(input("Enter a word : "));
val1 =str(val[::-1]);
print("\n Reversed String =",val);
if val == val1:
    print(val, "is palyndrome")
else:
    print(val, "not palyndrome")
