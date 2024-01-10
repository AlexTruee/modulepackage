import emoji

from datetime import datetime
from colorama import Fore

from application.salary import calculate_salary as cs
from application.db.people import get_employees as ge

if __name__ == '__main__':

    today = datetime.today()
    print(Fore.MAGENTA + f"Сегодня {emoji.emojize(':calendar:')}: {today.strftime('%d-%m-%Y')}{emoji.emojize(':thumbs_up:')}")
    print(Fore.RED + f"Запускаем {emoji.emojize(':gear:')}")
    cs()
    print(Fore.CYAN + f"Запускаем {emoji.emojize(':mechanical_arm:')}")
    ge()

