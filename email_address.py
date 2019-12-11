def is_correct1(str):
    str1 = str.split("@")[0]
    str2 = str.split("@")[1]

    if str == str1 + "@" + str2:
        return True


def is_correct2(str):
    str2 = str.split("@")[1]

    if "." in str2:
        return True

