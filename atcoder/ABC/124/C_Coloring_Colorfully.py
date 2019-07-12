def main():
    S = input()

    odd_tile_dict = {"0": 0, "1": 0}
    even_tile_dict = {"0": 0, "1": 0}
    for s in S[1::2]:
        odd_tile_dict[s] += 1

    for s in S[::2]:
        even_tile_dict[s] += 1

    res = min(odd_tile_dict["0"] + even_tile_dict["1"], odd_tile_dict["1"] + even_tile_dict["0"])
    print(res)


if __name__ == '__main__':
    main()