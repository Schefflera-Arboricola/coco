__all__ = [
    "Chocolate",
]


class Chocolate:
    def __init__(self, amount, temp, cocoa_solids, cocoa_butter, milk_solids, sugar):
        if temp is None:
            temp = "room temp"
        else:
            self.temp = temp
        if amount is None:
            self.amount = 0
        else:
            self.amount = amount

        self.type = self.classify(cocoa_solids, cocoa_butter, milk_solids, sugar)
        self.melting_point = self.get_melting_point(amount, self.type)
        self.tempering_point = self.get_tempering_point(self.type)

    def classify(cocoa_solids, cocoa_butter, milk_solids, sugar):
        threshold = 0.01
        if cocoa_solids > threshold and milk_solids <= threshold:
            return "dark"
        elif cocoa_solids > threshold and milk_solids > threshold:
            return "milk"
        elif cocoa_solids <= threshold and milk_solids > threshold:
            return "white"
        else:
            raise ValueError("Invalid chocolate type")

    def get_melting_point(amount, type):
        if amount == 0:
            return None
        elif type == "dark":
            return 31
        elif type == "milk":
            return 30
        elif type == "white":
            return 29
        else:
            raise ValueError("Invalid chocolate type")

    def get_tempering_point(type):
        if type == "dark":
            return 88
        elif type == "milk":
            return 86
        elif type == "white":
            return 84
        else:
            raise ValueError("Invalid chocolate type")
