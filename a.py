import maskpass
pw = maskpass.askpass(prompt="Password:", mask="*")
print(pw)