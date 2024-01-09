def hash():
    a= ["ST1E89B8A32","FR5J39A4S94","JF4AO4KF44","KEPMN4589JF","WOA458JHF","KAPR487DE","JFLE8343F","FJ03JV43R","SE43FB4BG"]
    h = [0]*9
    integer = "0123456789"
    count=0
    sum=0
    l = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    v = "AEIOU"
    for i in range(0,9):
        for j in range(0,len(a[i])):
            if a[i][j] in integer:
                sum = sum + int(a[i][j])
            if a[i][j] not in v and a[i][j] not in integer:
                count+=1

        temp = ((count*24)+sum)%9
        for k in range(0,9):
            if h[temp]==0:
                h[temp] = a[i]
                break
            else:
                temp+=1
                if temp>8:
                    temp=0
                if temp<=8:
                    if h[temp]==0:
                        h[temp] = a[i]
                        break
                    else:
                        temp+=1
                        if temp>8:
                            temp=0
        count=0
        sum=0
    print(h)

hash()
