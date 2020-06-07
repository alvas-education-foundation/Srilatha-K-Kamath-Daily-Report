with open("demo.txt") as f:
    with open("demo1.txt", "w") as f1:
        for line in f:
            f1.write(line)
