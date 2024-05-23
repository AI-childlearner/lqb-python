x=input()
y=input()
move=[1,-1,2,-2,3,-3]#所有行动方式
aset={x}#记录所有更新情况，防止重复
def bfs():
    Q=[[x,0]]
    while Q:
        old=Q.pop(0)
        for i in move:
            a=list(old[0])#变成列表方便操作
            b=old[1]#显示步数
            c=a.index("*")#记录*所在下标
            d=c+i#记录要与*交换位置的数的下标
            if 0<=d<len(x):#保证交换位置合理
                a[c]=a[d]#对应下标元素交换位置
                a[d]="*"
                e="".join(a)#将a变回字符串
                b=b+1#行动一次步数加一
                if e==y:#当变换为目标序列时就可以输出
                    print(b)
                    return
                if e not in aset:#如果此时变换的序列之前没出现
                    aset.add(e)
                    Q.append([e,b])#将新变换后的序列和更新后的步数入栈，重新进行序列变换
bfs()