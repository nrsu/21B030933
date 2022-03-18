import json
from textwrap import indent

with open("C:\\Users\\Админ\\Desktop\\jsonsample\\Sample-data.json", "r") as json_file:
    json_ = json.load(json_file)
    
print("\n")    
print("Interface status")
print('==========================================================================')
print("DN                                          Description     Speed      MTU")          
print('----------------------------------------    --------------  ---------  ----')

imdata = json_["imdata"]
cnt = 0

for i in range(len(imdata)):
    for j in imdata[i]:
        for k in imdata[i][j]:
            speed= imdata[i][j][k]['speed']
            mtu = imdata[i][j][k]['mtu']
            print(F"topology/pod-1/node-201/sys/phys-[eth1/{cnt}]                  {speed}     {mtu}")
            cnt+=1
        