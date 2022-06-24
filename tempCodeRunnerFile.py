def reverse(string):
    string = [string[i] for i in range(len(string)-1, -1, -1)]
    return string

print (reverse("Natty"))