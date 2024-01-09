def hocBuilder(h,i=1,card=0):
    if h==1:
        return 8
    if h==0:
        return 0
    if h==i:
        return card+8
    else:
        return hocBuilder(h,i+1,card+5)
print(hocBuilder(3))
