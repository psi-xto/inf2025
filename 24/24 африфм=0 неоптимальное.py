m = 0
a = (
    open("../24_17641.txt")
    .readline()
    .replace("++", "!")
    .replace("*+", "!")
    .replace("+*", "!")
    .replace("**", "!")
)
for i in "123456789":
    a = a.replace(i, "1")
for c in a.split("!"):
    if len(c) > m:
        for i in range(len(c) - 1):
            if c[i] not in "+*" and c[i : i + 2] not in ("00", "01"):
                substring = c[i]
                for j in range(i + 1, len(c)):
                    substring += c[j]
                    if substring[-1] not in "+*" and eval(substring) == 0:
                        m = max(m, len(substring))
print(m)
