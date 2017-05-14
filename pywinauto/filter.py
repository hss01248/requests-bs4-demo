
with open('F:\\url.txt', 'r') as f:
    list1 = f.readlines()


def remain720p(args):
    return args.find('720P') > 0


list2 = filter(remain720p, list1)

with open('F:\\url2.txt', 'w') as f2:
    for str2 in list2:
        f2.writelines(str2)