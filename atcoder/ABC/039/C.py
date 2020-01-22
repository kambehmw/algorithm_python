S = input()
keyboard = ["Do", "Re", "Mi", "Fa", "So", "La", "Si"]
patterns = ["WBWBWWBWBWBW", "WBWWBWBWBWWB", "WWBWBWBWWBWB", "WBWBWBWWBWBW", "WBWBWWBWBWWB", "WBWWBWBWWBWB", "WWBWBWWBWBWB"]
for i, p in enumerate(patterns):
    if p == S[:12]:
        print(keyboard[i])
        exit()
