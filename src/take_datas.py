import httpx  # дергаем html с апишки
from char_codes import char_codes  # все коды валют:названия по формату ISO 4217

LINK = r'https://www.cbr.ru/scripts/XML_daily.asp?date_req='  # константа апишку ЦБ


def get_html_content(url: str) -> str:
    with httpx.Client() as client:
        try:
            response = client.get(url)
            response.raise_for_status()  # Проверяем наличие ошибок при запросе
            return response.text
        except httpx.HTTPStatusError as exc:
            print(f"Ошибка при запросе: {exc}")
        except httpx.RequestError as exc:
            print(f"Ошибка сети: {exc}")


def take_valute(date_req: str, code: str) -> str:
    url = LINK+str(date_req)  # создаем url для апишки
    html = get_html_content(url)  # дергаем апишку
    # разбиваем весь Html на список, чтобы найти нужную нам валюту
    html = html.split(r'</Valute>')
    for valute in html:  # проходимся по всем валютам
        if code in valute:  # если нашли нужную, то возвращаем
            return valute
    # на случай, если указали такую валюту,
    # для которой нет кода в ISO 4217 (гривны и литовский талон)
    # или для которой нет информации за день.

    raise ValueError('Для данной валюты нет информации на сайте ЦБ РФ.')

# создаем вывод


def create_output(valute: str, code: str) -> str:
    nominal_start = valute.find('<Nominal>')
    nominal_end = valute.find(r'</Nominal>')
    nominal = valute[nominal_start+len('<Nominal>'):nominal_end]
    value_start = valute.find('<Value>')  # находим значение
    value_end = valute.find(r'</Value>')
    # выдергиваем его из строки
    value = valute[value_start+len('<Value>'):value_end]
    value = value.replace(',', '.')
    # создаю строку как просят по ТЗ
    output = f'{code} ({char_codes[code]}): {float(value)/int(nominal)}'
    return output  # возвращаем
