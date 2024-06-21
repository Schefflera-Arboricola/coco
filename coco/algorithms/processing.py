__all__ = ["tempering", "melting", "mix"]


def tempering(C):
    tp = C.get_tempering_point()
    type = C.classify()
    print("tempering...")
    t = _cooling_formula(C.temp, C.amount, tp, type)
    print(f"tempering done in {t} seconds")


def melting(C):
    mp = C.get_melting_point()
    type = C.classify()
    print("melting...")
    t = _melting_formula(C.temp, C.amount, mp, type)
    print(f"melting done in {t} seconds")


def _cooling_formula(temp, amount, tp, type):
    # todo
    return 0


def _melting_formula(temp, amount, mp, type):
    # todo
    return 0


def mix(C1, C2):
    if vars(C1) == vars(C2):
        C3 = C1
        C3.amount = C1.amount + C2.amount
        return C3
    else:
        raise ValueError("Cannot mix different types of chocolate")
