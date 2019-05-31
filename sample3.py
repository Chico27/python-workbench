# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！


def addABC(x):
    L = []
    L.append("A")
    L.append(x)
    L.append("B")
    L.append(x)
    L.append("C")
    return "".join(L)


k,s,t = input().split(" ")

outPutABC = "ABC"

for i in range(int(k)-1):
    nextOutPutABC = addABC(outPutABC)
    outPutABC = nextOutPutABC

print(outPutABC[int(s)-1:int(t)])

