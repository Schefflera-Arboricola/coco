import math

__all__ = [
    "Chocolate",
]


class Chocolate:
    ambient_temp = 20 + 273.15  # in Kelvin
    specific_heat_capacity = (
        2300  # J/kg·K for chocolate (converted to J/kg·K from J/g·K)
    )
    heat_transfer_coefficient = 10  # W/m²·K, an assumed constant for simplicity
    power_input = 500  # W, an assumed constant for simplicity

    def __init__(
        self, amount=0, temp=ambient_temp, melting_point=318.15, tempering_point=304.15
    ):
        self.amount = amount  # mass in kg
        self.temp = temp  # in Kelvin
        self.melting_point = melting_point  # 45°C by default
        self.tempering_point = tempering_point  # 31°C by default

    def cooling_time(self):
        """Returns:
        cooling_time: Time in seconds (s) for chocolate to cool to tempering temperature
        """
        if self.melting_point is None or self.tempering_point is None:
            return None
        surface_area = self.amount ** (2 / 3)  # Simplified assumption for surface area
        cooling_time = (
            (self.amount * self.specific_heat_capacity)
            / (self.heat_transfer_coefficient * surface_area)
            * math.log(
                (self.temp - self.ambient_temp)
                / (self.tempering_point - self.ambient_temp)
            )
        )
        return cooling_time

    def melting_time(self):
        """Returns:
        melting_time: Time in seconds (s) to melt the chocolate
        """
        if self.melting_point is None:
            return None
        melting_time = (
            self.amount * self.specific_heat_capacity * (self.melting_point - self.temp)
        ) / self.power_input
        return melting_time

    def mix(self, other):
        if isinstance(other, Chocolate) and self.temp == other.temp:
            mixed_amount = self.amount + other.amount
            return Chocolate(mixed_amount, self.temp)
        else:
            raise ValueError("Both chocolates must be at the same temperature to mix.")
