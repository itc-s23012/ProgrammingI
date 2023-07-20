names = ("a", "b", "c")
sep = "_"
sep.join(names)


def concat_words(*args, separator="."):
    return separator.join(args)


print(concat_words("a", "b", "c", "d", separator="_"))
print(concat_words("4_choume", "Minatoku", "Tokyo", "Japan", separator=" "))

names = ("a", "b", "c")
joined_names = "_".join(names)


def concat_words(*args, separator="."):
    return separator.join(args)


print(concat_words("a", "b", "c", "d", separator="_"))
print(concat_words("宜野湾市", "字宇地泊", "コーポA"))

names = ("a", "b", "c")
joined_names = "_".join(names)


def concat_words(*args, separator="/"):
    return separator.join(args)


print(concat_words("home", "vagrant", "ProgrammingI", "CHAPTER04"))
print(concat_words("宜野湾市", "字宇地泊", "コーポA"))
