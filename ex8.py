formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
# works well
print formatter % (
"I",
" had",
"this",
" string"
)
# the following is wrong without commas
print formatter % ( 
"I"
" had"
"this"
" string"
)

