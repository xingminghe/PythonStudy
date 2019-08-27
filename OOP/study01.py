citys = {
    "wuhan":"china",\
    "washington":"american",\
    "shanghai":"china"
}
def describe_city(city_name):
    if city_name in citys.keys():
        print(city_name,"in",citys[city_name])
    else:
        print(city_name,"is not in")
    return None
active = True
while active:
    city = input("enter a city or quit")
    if city == 'quit':
        active = False
    else:
        describe_city(city)