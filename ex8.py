formatter = "%r %r %r %r"

print formatter % (1,2,3,4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (
    "I had this thing",
    "That you could type right",
    "But it didn't work",
    "So I said goodnight")

