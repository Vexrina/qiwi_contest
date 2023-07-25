import argparse
import take_datas
from datetime import datetime # реформатирование времени

# константы на 
IN_FORMAT = '%Y-%m-%d' # входящий формат времени
OUT_FORMAT = '%d/%m/%Y' # подходящий формат времени для апишки ЦБ


def currency_rates(code:str, date_string:str)->None:
    date = datetime.strptime(date_string, IN_FORMAT)
    formatted = date.strftime(OUT_FORMAT)
    today = datetime.now().date()
    try:
        if today<date.date():
            raise ValueError('Введена дата из будущего')
        valute = take_datas.take_valute(formatted, code)
        print(take_datas.create_output(valute,code))
    except ValueError as exc:
        print(f'Ошибка запроса: {exc}')

    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Получение информации о курсе валюты.")
    parser.add_argument("--code", type=str, help="Код валюты в формате ISO 4217", required=True)
    parser.add_argument("--date", type=str, help="Дата в формате YYYY-MM-DD", required=True)

    args = parser.parse_args()

    currency_rates(args.code, args.date)