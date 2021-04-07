def find_all_hobbyists(hobby, hobbies):
    # so find peoples name who has the 'hobby'
    res = []
    for key, val in hobbies.items():
        if hobby in val:
            res.append(key)
    return res



if __name__ == "__main__":
    hobbies = {
        "Steve": ['Fashion', 'Piano', 'Reading'],
        "Patty": ['Drama', 'Magic', 'Pets'],
        "Chad": ['Puzzles', 'Pets', 'Yoga']
    }

    print(find_all_hobbyists('Pets', hobbies));