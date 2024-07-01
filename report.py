def report(path, word_count, dict):
    print(f"===== Begin report of {path} =====")
    print(f"{word_count} words found in the document.")

    characters = []
    keys = dict.keys()

    for key in keys:
        if key.isalpha():
            temp = {"char": key, "num": dict[key]}
            characters.append(temp)

    characters.sort(reverse=True, key=sort_on)
    
    for x in characters:
        print(f"The '{x['char']}' character was found {x['num']} times.")

    print("===== End Report =====")

def sort_on(dict):
    return dict["num"]
