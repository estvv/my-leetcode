# abcaab -> 3

def exercise(string: str):
    save = {}
    counter = 0
    answer = 0

    for i in range(len(string)):
        # print(save.keys())
        if not string[i] in save.keys():
            # print("Yes: ", save)
            save[string[i]] = 1
            counter += 1
        else:
            # print("Nop: ", save)
            if counter >= answer:
                answer = counter
            counter = 0
            save = {}
        # print(counter)

    return answer

# print(exercise("abcaab"))
print(exercise("aaaaaaaaabaaacccc"))
# print(exercise("abcaab"))
