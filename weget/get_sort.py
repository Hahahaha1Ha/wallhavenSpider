import re


def asksort():
    outcheck = True
    stack = ['000', '000', 'relevance']
    dict1 = {
        "0": "relevance",
        "1": "relevance",
        "2": "random",
        "3": "data_added",
        "4": "views",
        "5": "favorites",
        "6": "toplist",
        "7": "hot"
    }
    while outcheck:
        asktext = str(
            input(
                "选择筛选条件 1 -> 进入选择<一般><动漫><真人>|2 -> 进入选择<全年龄><带有一点点的不安全要素>|3 -> 进入选择<关联性|随机|添加时间|查看人数|更多喜欢|排行前十|热门>|4 -> 退出\n"
            ))
        if asktext[0] == '1':
            categoies = str(
                input(
                    "使用1->勾选|0->不勾选|3->退出此筛选条件///第一位对应<一般>,第二位对应<动漫>,第三位对应<真人> \n"
                ))
            re1 = re.compile(r'[0-1]{1,3}')
            if '3' in categoies:
                continue
            else:
                try:
                    output = re1.match(categoies)
                    get = output.group()
                except AttributeError:
                    print("三位都需输入0-3的数字")
                    continue
                else:
                    if len(get) < 2:
                        get = get[:len(get)] + '00'
                        print(get)
                    elif len(get) == 2:
                        get = get[:len(get)] + '0'
                    stack1 = list(stack[0])
                    for i in range(0, 3):
                        if stack[0][i] != get[i]:
                            stack1[i] = get[i]
                    stack[0] = ''.join(stack1)
            print(stack)
        if asktext[0] == '2':
            categoies = str(
                input(
                    "使用1->勾选|0->不勾选|3->退出此筛选条件///第一位对应<全年龄>,第二位对应<略微不安全要素> \n")
            )
            re1 = re.compile(r'[0-1]{1,2}')
            if '3' in categoies:
                continue
            else:
                try:
                    output = re1.match(categoies)
                    get = output.group()
                except AttributeError:
                    print("两位都需输入0-3的数字")
                    continue
                else:
                    if len(get) < 2:
                        get = get[:len(get)] + '00'
                        print(get)
                    elif len(get) == 2:
                        get = get[:len(get)] + '0'
                    stack1 = list(stack[1])
                    for i in range(0, 3):
                        if stack[1][i] != get[i]:
                            stack1[i] = get[i]
                    stack[1] = ''.join(stack1)
            print(stack)
        if asktext[0] == '3':
            categoies = str(
                input(
                    "1 -> 关联性 2 -> 随机 3 -> 最近添加 4 -> 查看人数 5 -> 更多喜欢 6 -> 排名前十 7 -> 热门 \n"
                ))
            get = re.search(r'[1-7]', categoies).group()
            stack[2] = dict1[get]
            print(stack)
        if asktext[0] == '4':
            print("最后的筛选条件为 \n", stack)
            exitget = str(input("确定要退出筛选吗 1 -> 退出 2 -> 重新选择 \n"))
            if "1" in exitget:
                outcheck = False
            elif "2" in exitget:
                continue

    return stack
