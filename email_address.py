def is_correct(str):
    str1 = str.split("@")[0]
    str2 = str.split("@")[1]
    if str == str1 + "@" + str2:
        return True

