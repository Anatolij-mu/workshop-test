from address import Address
from mailing import Mailing


to_address = Address("123456", "Москва", "Ленина", "10", "25")
from_address = Address("654321", "Санкт-Петербург", "Пушкина", "5", "30")


mailing = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=500.50,
    track="RA123456789RU"
)


print(mailing.get_shipping_info())
