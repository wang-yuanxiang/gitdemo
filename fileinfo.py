#麻将.py
a = input()
b = input()
c = a + b  #将两个字符串连起来
f = []
g = []
h = []
li = []
flag = False
for i in range(len(c)):              #遍历连接后的字符串
    if c[i] == 'm':                  #将“万”牌加入到列表中
        f.append(c[i - 1])
    if f.count('1') >= 3 and '2' in f and '3' in f and '4' in f and '5' in f and '6' in f and '7' in f and '8' in f and f.count('9')>=3:
        d = i
        flag = True
        break            #当各个数字的“万”牌都在列表内，且“一万”和“九万”至少为三张时，跳出循环
if f[-1] == '1' and f.count('9')>3 and flag == True:     
    s = int((d - 25)/2)
    li.append(s)        #如果此时最后摸到的牌是一万，而且“九万”多于三张时，最后一张“一万”即为胡牌所需的最后一张牌，求出的它的位置
elif f[-1] == '1' and f.count('9') == 3 and len(f) > 13 and flag == True:
    s = int((d - 25)/2)
    li.append(s)        #如果最后摸上来的是一万，而且九万是三张，且“万”牌多于13张，说明其他数字的“万”牌至少有一个数字不止一张，那么最后一万也是胡牌所需的最后一张牌，求出它的位置
elif f[-1] == '1' and f.count('9') == 3 and len(f) == 13 and d < len(c) and flag == True:
     for i in range(d + 1,len(c)):  #如果最后一张是一万，而且九万为三张，万牌总共有13张，此时，再摸到任何一张万牌即胡牌，因此需要遍历还没有摸上来的字符串
        if c[i] == 'm':
            s = int((i - 25)/2)
            li.append(s)   
            break                  #碰到任意一张万牌就胡牌，此时跳出循环，求出那张万牌的位置
elif f[-1] == '9' and f.count('1')>3 and flag == True :
    s = int((d - 25)/2)
    li.append(s)
elif f[-1] == '9' and f.count('1') == 3 and d < len(c) and len(f) == 13 and flag == True:
    for i in range(d + 1,len(c)):
        if c[i] == 'm':
            s = int((i - 25)/2)
            li.append(s)
            break
elif f[-1] == '9' and f.count('1') == 3 and len(f) > 13 and flag == True:
    s = int((d - 25)/2)
    li.append(s)
elif f[-1] != '1' and f[-1] != '9' and len(f) > 13 and flag == True:
    s = int((d - 25)/2)
    li.append(s)
elif f[-1] != '1' and f[-1] != '9' and len(f) == 13 and flag == True:
    for i in range(d + 1,len(c)):
        if c[i] == 'm':
            s = int((i - 25)/2)
            li.append(s)
            break                 #以上五种情况考虑的是最后摸上来的牌是九万的情况，此时考虑一万的数量，与之前的最后摸到的是一万的情况类似






flag = False                     #万牌的情况考虑结束，开始考虑“筒”牌的胡牌情况，方法与“万”牌类似
for i in range(len(c)):
    if c[i] == 'p':
        g.append(c[i - 1])
    if g.count('1') >= 3 and '2' in g and '3' in g and '4' in g and '5' in g and '6' in g and '7' in g and '8' in g and g.count('9')>=3:
        d = i
        flag = True
        break
if flag == True:
    if g[-1] == '1' and g.count('9')>3 :
        s = int((d - 25)/2)
        li.append(s)
    elif g[-1] == '1' and g.count('9') == 3 and len(g) > 13 :
        s = int((d - 25)/2)
        li.append(s)
    elif g[-1] == '1' and g.count('9') == 3 and len(g) == 13 and d < len(c) :
        for i in range(d + 1,len(c)):
            if c[i] == 'p':
                s = int((i - 25)/2)
                li.append(s)
                break
    elif g[-1] == '9' and g.count('1')>3 :
        s = int((d - 25)/2)
        li.append(s)
    elif g[-1] == '9' and g.count('1') == 3 and d < len(c) and len(g) == 13 :
        for i in range(d + 1,len(c)):
            if c[i] == 'p':
                s = int((i - 25)/2)
                li.append(s)
                break
    elif g[-1] == '9' and g.count('1') == 3 and len(g) > 13 :
        s = int((d - 25)/2)
        li.append(s)
    elif g[-1] != '1' and g[-1] != '9' and len(g) > 13:
        s = int((d - 25)/2)
        li.append(s)
    elif g[-1] != '1' and g[-1] != '9' and len(g) == 13 :
        for i in range(d + 1,len(c)):
            if c[i] == 'p':
                s = int((i - 25)/2)
                li.append(s)
                break       






flag = False                   #用相同方法考虑“条”牌的胡牌情况
for i in range(len(c)):
    if c[i] == 's':
        h.append(c[i - 1])
    if h.count('1') >= 3 and '2' in h and '3' in h and '4' in h and '5' in h and '6' in h and '7' in h and '8' in h and h.count('9')>=3:
        d = i
        flag = True
        break
if flag == True:
    if h[-1] == '1' and h.count('9')>3 :
        s = int((d - 25)/2)
        li.append(s)
    elif h[-1] == '1' and h.count('9') == 3 and len(h) > 13 :
        s = int((d - 25)/2)
        li.append(s)
    elif h[-1] == '1' and h.count('9') == 3 and len(h) == 13 and d < len(c) :
        for i in range(d + 1,len(c)):
            if c[i] == 's':
                s = int((i - 25)/2)
                li.append(s)
                break
    elif h[-1] == '9' and h.count('1')>3 :
        s = int((d - 25)/2)
        li.append(s)
    elif h[-1] == '9' and h.count('1') == 3 and d < len(c) and len(h) == 13 :
        for i in range(d + 1,len(c)):
            if c[i] == 's':
                s = int((i - 25)/2)
                li.append(s)
                break
    elif h[-1] == '9' and h.count('1') == 3 and len(h) > 13 :
        s = int((d - 25)/2)
        li.append(s)
    elif h[-1] != '1' and h[-1] != '9' and len(h) > 13:
        s = int((d - 25)/2)
        li.append(s)
    elif h[-1] != '1' and h[-1] != '9' and len(h) == 13 :
        for i in range(d + 1,len(c)):
            if c[i] == 's':
                s = int((i - 25)/2)
                li.append(s)
                break
if len(li) != 0:
    print(min(li))        #若能胡牌，输出最先能使胡牌的那张牌的位置
else:
    print('Stop Your Daydream!')
#test for github
#do not wanna change the code
#
#
#
#
#
#using this to stand for the change of the code