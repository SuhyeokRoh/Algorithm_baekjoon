wordlist = [
    "Never gonna give you up",
    "Never gonna let you down",
    "Never gonna run around and desert you",
    "Never gonna make you cry",
    "Never gonna say goodbye",
    "Never gonna tell a lie and hurt you",
    "Never gonna stop"
]
rst = 0
for _ in range(int(input())):
    word = input()
    if word in wordlist:
        pass
    else:
        rst = 1
        break
        
if rst == 0:
    print("No")
else:
    print("Yes")