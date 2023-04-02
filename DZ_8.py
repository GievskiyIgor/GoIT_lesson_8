from datetime import datetime, timedelta, date
from collections import defaultdict
from pprint import pprint

users = [{"name":"Igor","birthday":"2,4,1982"},
         {"name":"Alena","birthday":"4,4,1993"},
         {"name":"Gennadiy","birthday":"30,12,1960"},
         {"name":"Valentina","birthday":"10,6,1956"},
         {"name":"Alecya","birthday":"25,5,1973"}]

def get_birthday_per_weer (users):
    birthday = defaultdict(list)
    today = datetime.now().date()

    next_week_start = get_next_week_start(today)
    
    start_period = next_week_start - timedelta(2)
    end_period = next_week_start + timedelta(4)

    happy_users = [user for user in users if start_period <= prepare_birthday(user["birthday"]) <= end_period]

    for user in happy_users:
        current_bd: date = prepare_birthday(user["birthday"])
        if current_bd.weekday() in [5,6]:
            birthday["Monday"].append(user["name"])
        else:
           birthday[current_bd.strftime("%A")].append(user["name"])    

    return   birthday      

def get_next_week_start(week_day: datetime):
    diff_days = 7 - week_day.weekday()
    return week_day + timedelta(days=diff_days)

def prepare_birthday(birthday_str: str):
    bd = (datetime.strptime(birthday_str,"%d,%m,%Y"))
    return bd.replace(year=datetime.now().year).date()


if __name__ == "__main__":
        
    result = get_birthday_per_weer (users)
    pprint(result)