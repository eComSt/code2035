
def time_day(hour):
    if hour>12 and hour<=16:
        print("День")
    elif hour>16 and hour<=23:
        print("Вечер")
    elif hour>3 and hour<=12:
        print("Утро")
    elif (hour>23 and hour<=24) or hour<=3:
        print("Ночь")
    else:
        print("Мы на какой планете?")
