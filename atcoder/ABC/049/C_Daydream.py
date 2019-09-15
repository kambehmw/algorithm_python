import time

S = input()[::-1]
keywords = ["dream", "dreamer", "erase", "eraser"]
keywords = [x[::-1] for x in keywords]
# start_time = time.time()
start = 0
while True:
    flag = False
    end = None
    for key in keywords:
        key_len = len(key)
        end = start + key_len
        if S[start:end] == key:
            flag = True
            break

    start = end

    if not flag:
        print("NO")
        exit()

    if flag and start == len(S):
        print("YES")
        exit()


