from pprint import pprint
good_of_eldorado = [
    {
        "name":"3310",
        "brand":"Nokia",
        "price":1
    },
    {
        "name":"8800",
        "brand":"Nokia",
        "price":1_000_000,
    },
    {
        "name":"S21",
        "brand":"Samsung",
        "price":16_900
    },
    {
        "name":"Y61",
        "brand":"Huawei",
        "price":11_000
    },
    {
        "name":"Iphone 15",
        "brand":"Apple",
        "price":110_000
    },
    {
        "name":"Iphone 1",
        "brand":"Apple",
        "price":1_000
    },
    {
        "name":"Yoga tablet x1",
        "brand":"Lenovo",
        "price":55_000
    },
    {
        "name":"Honor 70",
        "brand":"Huawei",
        "price":70_000
    }
]
test_list = [2,4,3,5,7,4,1,6,8,0,3,3,2]
pprint(good_of_eldorado)
x = sorted(good_of_eldorado)
pprint(x)
