class Microwave:
    def __init__(self, brand: str, power_range: str) -> None:
        self.brand = brand
        self.power_range = power_range
        self.turned_on: bool = False

    def turn_on(self) -> None:
        if self.turned_on:
            print(f'the {self.brand} microwave is already turned on')

        else:
            self.turned_on = True
            print(f'the {self.brand} is turned on')

    def turn_off(self) -> None:
        if self.turned_on:
            self.turned_on = False

            print(f'The {self.brand} is turned off')

        else:
            print(f'The {self.brand} microwave is turning off')

    def run(self, seconds: int) -> None:
        if self.turned_on:
            print(f'The {self.brand} is running for {seconds}s')

        else:
            print("A wheezing sound... turn on the microwave fisrt")

huawei = Microwave(brand='huawei', power_range= 'D')

huawei.turn_on()
huawei.turn_on()
huawei.run(35)
