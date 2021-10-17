# line 5 uses the assign operator `=`, which is invalid in a condition,
# but is very close to `:=` or more commonly `==`, which are valid in this context

var = 2
if var = 1:
    print("hurray")
