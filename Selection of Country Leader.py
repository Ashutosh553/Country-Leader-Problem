



t = int(input())
tc = 0
while t > 0:
    name_number = int(input())
    name_dict = {}
    for _ in range(name_number):
        name = input()
        name_dict[name] = list(dict.fromkeys(list(name.replace(" ",""))))
        name = ""
    leader_list = []
    for a in list(name_dict):
        if all(len(name_dict[a]) >= len(name_dict[i]) for i in (list(name_dict))):
            leader_list.append(a)
    if len(leader_list) > 1:
        for x in leader_list:
            if all( x <= y for y in leader_list):
                leader = x
                break
    else:
        leader = leader_list[0]
    tc += 1
    print(f"Case #{tc}: {leader}")
    t -= 1