def last_names_by_age(dic, min_age, max_age):
    dic0 = {}
    keys = list(dic.keys())
    last_names = []
    ages = []

    for i in range(len(keys)):
        last_name = keys[i].split()
        last_names.append(last_name[len(last_name) - 1])
        ages.append(dic.get(keys[i]))

    for i in range(len(ages)):
        s = ""
        if min_age <= ages[i] <= max_age:
            for j in range(len(keys)):
                if dic.get(keys[j]) == ages[i]:
                    s += last_names[j] + " and "
            s = s.removesuffix(" and ")
            dic0.update({ages[i]: s})
    return dic0
         

      
    