from requests import *
from json import *
def check_planets():
    name = ''
    d = 0
    url = 'https://swapi.dev/api/planets/'
    for i in range(1, 6):
        responce = get(f'{url}/{i}').json()
        if int(responce.get("diameter"))>d:
            d=int(responce.get("diameter"))
            name = responce.get("name")
    return name, d

def check_starhips():
    j=0
    name = ''
    d = 0
    url = 'https://swapi.dev/api/starships/'
    d_list=[]
    for i in range(1, 100):
        responce = get(f'{url}/{i}').json()
        if len(responce)>1:
            j+=1
            if responce.get("max_atmosphering_speed")!='n/a':
                d_list.append({responce.get("name"):responce.get("max_atmosphering_speed")})
                if int(responce.get("max_atmosphering_speed"))>d:
                    d=int(responce.get("max_atmosphering_speed"))
                    name = responce.get("name")
        if  j==5: break
    return name,d
