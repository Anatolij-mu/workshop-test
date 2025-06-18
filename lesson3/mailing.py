from address import Address


class Mailing:

    def __init__(self, to_address: Address, from_address: Address,
                 cost: float, track: str):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

    def get_shipping_info(self) -> str:

        from_addr = (f"{self.from_address.index}, {self.from_address.city}, "
                     f"{self.from_address.street}, {self.from_address.house} -"
                     f"{self.from_address.apartment}")

        to_addr = (f"{self.to_address.index}, {self.to_address.city}, "
                   f"{self.to_address.street}, {self.to_address.house} - "
                   f"{self.to_address.apartment}")

        return (f"Отправление {self.track} из {from_addr} в {to_addr}. "
                f"Стоимость {int(self.cost)} рублей.")
