def gugudan(*dans):
    for dan in dans:
        for i in range(1, 10):
            print(f"{dan}*{i}={dan*i}")
        print()
gugudan(2,3,7)