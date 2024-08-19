def calculate_love_score(name_1, name_2):
    name = name_1.lower().replace(" ", "") + name_2.lower().replace(" ", "")
    check_1 = "true"
    check_2 = "love"
    first_num = 0
    second_num = 0

    for letter in check_1:
        if letter in name:
            num = name.count(letter)
            first_num += num

    for letter in check_2:
        if letter in name:
            num = name.count(letter)
            second_num += num

    score = str(first_num) + str(second_num)
    print(int(score))

calculate_love_score("Kanye West", "Kim Kardashian")