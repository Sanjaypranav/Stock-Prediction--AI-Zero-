from dateutil.parser import parse

def date_parser(value):

    a = value.split(" ")[0]
    value = value.split(" ")[1].split("-")[0]
    a = a + " " + value
    # print(type(a))
    return parse(a)

# print(date_parser("2022-07-01 12:00:00-04:00"))