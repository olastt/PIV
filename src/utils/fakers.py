import datetime
from random import choice, randint
from string import ascii_letters, digits

from faker import Faker
from faker.providers import company

from settings import base_settings

fake_locales = base_settings.faker_locales

fake = Faker(fake_locales)
fake.add_provider(company)


def random_number(start: int = 100, end: int = 1000) -> int:
    return randint(start, end)


def random_string(start: int = 9, end: int = 15) -> str:
    return ''.join(choice(ascii_letters + digits) for _ in range(randint(start, end)))


def random_list_of_strings(start: int = 2, end: int = 7) -> list[str]:
    return [random_string() for _ in range(randint(start, end))]


def random_fio():
    return fake.name()

def random_fio_one():
    return fake.name().split(" ")[0]


def random_ip_title():
    return 'ИП ' + ' '.join(fake.name().split()[:2])


def random_email():
    return fake.email()


def random_email_list():
    emails = [random_email() for _ in range(randint(1, 2))]
    return emails


def random_phone_number():
    region_code = randint(900, 985)
    number1 = randint(100, 999)
    number2 = randint(10, 99)
    number3 = randint(10, 99)
    phone_number = f'+7 ({region_code}) {number1}-{number2}-{number3}'
    return phone_number


def random_phone_number_list():
    phones = [random_phone_number() for _ in range(randint(1, 2))]
    return phones


def random_company():
    return fake.company()


def inn_ctrl_summ(nums, type):
    """
    Подсчет контрольной суммы
    """
    inn_ctrl_type = {
        'n2_12': [7, 2, 4, 10, 3, 5, 9, 4, 6, 8],
        'n1_12': [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8],
        'n1_10': [2, 4, 10, 3, 5, 9, 4, 6, 8],
    }
    n = 0
    l = inn_ctrl_type[type]
    for i in range(0, len(l)):
        n += nums[i] * l[i]
    return n % 11 % 10


def random_inn(inn_len=12):
    """
    Генерация ИНН (10 или 12 значный)
    На входе указывается длина номера - 10 или 12.
    Если ничего не указано, будет выбрана случайная длина.
    """
    if not inn_len:
        inn_len = list((10, 12))[randint(0, 1)]
    if inn_len not in (10, 12):
        return None
    nums = [
        randint(1, 9) if x == 0
        else randint(0, 9)
        for x in range(0, 9 if inn_len == 10 else 10)
    ]
    if inn_len == 12:
        n2 = inn_ctrl_summ(nums, 'n2_12')
        nums.append(n2)
        n1 = inn_ctrl_summ(nums, 'n1_12')
        nums.append(n1)
    elif inn_len == 10:
        n1 = inn_ctrl_summ(nums, 'n1_10')
        nums.append(n1)
    return ''.join([str(x) for x in nums])


def random_ogrn():
    # Выбор признака отнесения государственного регистрационного номера записи
    type_code = choice([2, 4, 6, 7, 8, 9])
    # Год внесения записи
    year = randint(10, 22)
    # Код субъекта Российской Федерации
    region_code = randint(1, 99)
    # Номер записи в государственном реестре
    record_number = randint(1000000, 9999999)
    ogrn = f'{type_code}{year:02d}{region_code:02d}{record_number:07d}'
    control_sum = str((int(ogrn[:12]) % 11))[-1]
    return f'{ogrn}{control_sum}'


def random_ogrnip():
    type_code = 3
    year = randint(10, 22)
    region_code = randint(1, 99)
    record_number = randint(100000000, 999999999)
    ogrn = f'{type_code}{year:02d}{region_code:02d}{record_number:09d}'
    control_sum = str((int(ogrn[:14]) % 13))[-1]
    return f'{ogrn}{control_sum}'


def random_kpp():
    inn = random_inn()
    return inn[:4] + '01001'


def random_full_address():
    full_address = 'Россия, ' + ', '.join(fake.address().split(', ')[:-1])
    return full_address


def random_address():
    address = ', '.join(fake.address().split(', ')[-3:-1])
    return address


def random_country():
    return fake.country()


def random_countries_list():
    k = randint(1, 3)
    return [fake.country() for _ in range(k)]


def random_region():
    return fake.region()


def random_regions_list():
    k = randint(1, 3)
    return [fake.region() for _ in range(k)]


def random_city():
    return fake.city()

def random_street():
    return fake.street_title()


def random_domain(protocol=True):
    domain = fake.domain_name()
    if protocol:
        domain = 'https://' + domain
    return domain


def random_domain_list(protocol=True):
    domains = [random_domain(protocol=protocol) for _ in range(randint(1, 2))]
    return domains


def random_text(max_length=500):
    text = fake.text(max_nb_chars=max_length)
    return text

def get_test_password():
    return base_settings.user_password



def random_datetime_z():
    now = datetime.datetime.now()
    formatted_date = now.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    return formatted_date

