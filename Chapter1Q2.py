# Write code to reverse a C-Style string

string = "String!\0"

end = string[:-1]
reverse = end[::-1]
final = reverse + "\0"
print(final)