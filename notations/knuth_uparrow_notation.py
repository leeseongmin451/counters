from __future__ import annotations

import math
from copy import deepcopy
from typing import *


def get_coeff_power(base: Union[int, float], power=1) -> Tuple[Union[int, float], int]:
    if base == 0:
        return 0, 0

    log_n = math.log10(abs(base)) * power
    res_power = math.floor(log_n)
    res_coeff = 10 ** (log_n - res_power)

    return res_coeff, res_power


class KnuthUpArrowNotation:
    """
    A numerical notation for extremely large numbers.
    It is based on Knuth's up-arrow notation.

    Calculatable like normal type of values.
    Also has other type of calculations only available in this class.
    In this game, it uses symbol '^' instead of up-arrow.

    `KnuthUpArrowNotation(KUAN)`'s instances has 4 properties: `coeff(icient), power, level and layer`.
    And the value of this number is `coeff * 10 ^ power`, basically.
    It's similar to scientific notations without mentioning level and layer.

    The most important thing is that `power` itself can also be a `KUAN` instance recursively.
    And the `layer` value represents how many recursion has occurred from itself.
    For example, if power is not `KUAN`, then `layer` value is 1, meaning 'first layer'.
    But if power IS `KUAN` and its layer is 3, then `layer` value becomes 4.

    If `layer` is 10 or higher, the entire notation collapses into next `level`.
    """

    def __init__(self, coeff: Union[int, float] = 1, power: Union[int, KnuthUpArrowNotation] = 0, level=1, layer=1):
        """
        Initializing method
        """

        self.coeff = coeff
        self.power = power
        self.level = level
        self.layer = layer

        # Fix coeff, level and layer value depending on power if necessary
        if isinstance(power, KnuthUpArrowNotation):
            if self.level < power.level:
                self.level = power.level
            if self.level == power.level:
                self.layer = power.layer + 1

            # Coeff value has no meaning if level is 2 or higher
            # Because numbers at this level is so large that multiplication has no effect to them
            if power.level > 1:
                self.coeff = 1

        self.normalize()

    def normalize(self):
        self.normalize_layer()
        self.normalize_coeff()
        self.normalize_power()
        self.normalize_layer()

    def normalize_coeff(self):
        if self.coeff == 0:
            self.power = 0
            self.level = 1
            self.layer = 1
            return

        if self.level > 1 or self.layer > 2:
            self.coeff = 1

        if not (1 <= abs(self.coeff) < 10):
            new_coeff, new_power = get_coeff_power(self.coeff)
            self.coeff = new_coeff
            self.power += new_power

    def normalize_power(self):
        if self.level == 1:
            if self.layer == 1 and self.power >= 10:
                self.power = KnuthUpArrowNotation(*get_coeff_power(self.power))
                self.layer += 1
            elif self.layer == 2 and self.power.power == 0:
                self.power = round(self.power.coeff)
                self.layer -= 1
        else:
            if not isinstance(self.power, KnuthUpArrowNotation):
                self.power = KnuthUpArrowNotation(*get_coeff_power(self.power))

    def normalize_layer(self):
        if isinstance(self.power, KnuthUpArrowNotation):
            self.layer = self.power.layer + 1

        if self.layer >= 10:
            self.level += 1
            self.layer = 2
            self.power = KnuthUpArrowNotation(self.layer / 10, 1)

    def value(self) -> float:
        if self.level > 1 or self.layer > 2:
            return math.inf

        if self.layer == 2 and self.power.value() >= 308:
            return math.inf

        return float(self.coeff * (10 ** self.power))

    def unite(self, other: KnuthUpArrowNotation):
        self.coeff = other.coeff
        self.power = other.power
        self.layer = other.layer
        self.level = other.level

    def __str__(self) -> str:
        base_str = "10" + "^" * self.level
        if self.layer == 1:
            return str(int(self.value()))

        if self.layer == 2:
            if self.level == 1:
                return "{0:.2f} x ".format(self.coeff) + base_str + "{}".format(self.power)
            else:
                return base_str + "{}".format(self.power)

        if self.layer == 3:
            return base_str + "({})".format(self.power)

        return base_str + "{}".format(self.power)

    def __abs__(self) -> KnuthUpArrowNotation:
        copied = deepcopy(self)
        copied.coeff = abs(copied.coeff)
        return copied

    def __neg__(self) -> KnuthUpArrowNotation:
        copied = deepcopy(self)
        copied.coeff = -copied.coeff
        return copied

    def __add__(self, other: Union[int, float, KnuthUpArrowNotation]) -> KnuthUpArrowNotation:
        if not isinstance(other, KnuthUpArrowNotation):
            oKUAN = KnuthUpArrowNotation(*get_coeff_power(other))
        else:
            oKUAN = deepcopy(other)

        scopy = deepcopy(self)

        # TODO: 차이가 큰 수를 계산할 경우 OverflowError가 발생

        # If number's level or layer is too high, practical operations are useless.
        # So just return one of params without changing its value.

        if scopy.level > oKUAN.level:
            return scopy
        elif scopy.level < oKUAN.level:
            scopy.unite(oKUAN)
            return scopy

        if scopy.level > 1:
            if scopy.power > oKUAN.power:
                return scopy
            elif scopy.power < oKUAN.power:
                scopy.unite(oKUAN)
                return scopy

        if scopy.layer > 2 and oKUAN.layer > 2:
            if scopy.layer > oKUAN.layer:
                return scopy
            elif scopy.layer < oKUAN.layer:
                scopy.unite(oKUAN)
                return scopy
            else:
                if scopy.power > oKUAN.power:
                    return scopy
                elif scopy.power < oKUAN.power:
                    scopy.unite(oKUAN)
                    return scopy

        elif scopy.layer > 2 >= oKUAN.layer:
            return scopy

        elif scopy.layer <= 2 < oKUAN.layer:
            scopy.unite(oKUAN)
            return scopy

        # If both number
        # level: 1
        # layer < 3
        # Then adding operation gets meaningful.

        if scopy.layer == 2 and oKUAN.layer == 2:
            power_diff = int(scopy.power.value() - oKUAN.power.value())

            if power_diff >= 0:
                scopy.coeff += oKUAN.coeff / (10 ** power_diff)

            else:
                oKUAN.coeff += scopy.coeff * (10 ** power_diff)
                scopy.unite(oKUAN)

        elif scopy.layer == 2 and oKUAN.layer == 1:
            power_diff = int(scopy.power.value() - oKUAN.power)

            scopy.coeff += oKUAN.coeff / (10 ** power_diff)

        elif scopy.layer == 1 and oKUAN.layer == 2:
            power_diff = int(scopy.power - oKUAN.power.value())

            oKUAN.coeff += scopy.coeff * (10 ** power_diff)
            scopy.unite(oKUAN)

        else:
            power_diff = int(scopy.power - oKUAN.power)

            if power_diff >= 0:
                scopy.coeff += oKUAN.coeff / (10 ** power_diff)

            else:
                oKUAN.coeff += scopy.coeff * (10 ** power_diff)
                scopy.unite(oKUAN)

        scopy.normalize()
        return scopy

    def __sub__(self, other: Union[int, float, KnuthUpArrowNotation]) -> KnuthUpArrowNotation:
        if not isinstance(other, KnuthUpArrowNotation):
            oKUAN = KnuthUpArrowNotation(*get_coeff_power(other))
        else:
            oKUAN = deepcopy(other)

        scopy = deepcopy(self)

        # If number's level or layer is too high, practical operations are useless.
        # So just return one of params without changing its value.

        if scopy.level > oKUAN.level:
            return scopy
        elif scopy.level < oKUAN.level:
            scopy.unite(oKUAN)
            return -scopy

        if scopy.level > 1:
            if scopy.power > oKUAN.power:
                return scopy
            elif scopy.power < oKUAN.power:
                scopy.unite(oKUAN)
                return -scopy

        if scopy.layer > 2 and oKUAN.layer > 2:
            if scopy.layer > oKUAN.layer:
                return scopy
            elif scopy.layer < oKUAN.layer:
                scopy.unite(oKUAN)
                return -scopy
            else:
                if scopy.power > oKUAN.power:
                    return scopy
                elif scopy.power < oKUAN.power:
                    scopy.unite(oKUAN)
                    return -scopy

        elif scopy.layer > 2 >= oKUAN.layer:
            return scopy

        elif scopy.layer <= 2 < oKUAN.layer:
            scopy.unite(oKUAN)
            return -scopy

        # If both number
        # level: 1
        # layer < 3
        # Then adding operation gets meaningful.

        if scopy.layer == 2 and oKUAN.layer == 2:
            power_diff = int(scopy.power.value() - oKUAN.power.value())

            if power_diff >= 0:
                scopy.coeff -= oKUAN.coeff / (10 ** power_diff)

            else:
                oKUAN.coeff -= scopy.coeff * (10 ** power_diff)
                scopy.unite(-oKUAN)

        elif scopy.layer == 2 and oKUAN.layer == 1:
            power_diff = int(scopy.power.value() - oKUAN.power)

            scopy.coeff -= oKUAN.coeff / (10 ** power_diff)

        elif scopy.layer == 1 and oKUAN.layer == 2:
            power_diff = int(scopy.power - oKUAN.power.value())

            oKUAN.coeff -= scopy.coeff * (10 ** power_diff)
            scopy.unite(-oKUAN)

        else:
            power_diff = int(scopy.power - oKUAN.power)

            if power_diff >= 0:
                scopy.coeff -= oKUAN.coeff / (10 ** power_diff)

            else:
                oKUAN.coeff -= scopy.coeff * (10 ** power_diff)
                scopy.unite(-oKUAN)

        scopy.normalize()
        return scopy

    def __mul__(self, other: Union[int, float, KnuthUpArrowNotation]) -> KnuthUpArrowNotation:
        if not isinstance(other, KnuthUpArrowNotation):
            oKUAN = KnuthUpArrowNotation(*get_coeff_power(other))
        else:
            oKUAN = deepcopy(other)

        scopy = deepcopy(self)

        scopy.coeff *= oKUAN.coeff
        if oKUAN.layer == 1:
            scopy.power += oKUAN.power
        else:
            scopy.power = oKUAN.power + scopy.power

        scopy.normalize()
        return scopy

    def __truediv__(self, other: Union[int, float, KnuthUpArrowNotation]) -> KnuthUpArrowNotation:
        if not isinstance(other, KnuthUpArrowNotation):
            oKUAN = KnuthUpArrowNotation(*get_coeff_power(other))
        else:
            oKUAN = deepcopy(other)

        scopy = deepcopy(self)

        scopy.coeff /= oKUAN.coeff
        scopy.power -= oKUAN.power

        scopy.normalize()
        return scopy

    def __pow__(self, other: Union[int, float, KnuthUpArrowNotation]) -> KnuthUpArrowNotation:
        if not isinstance(other, KnuthUpArrowNotation):
            oKUAN = KnuthUpArrowNotation(*get_coeff_power(other))
        else:
            oKUAN = deepcopy(other)

        scopy = deepcopy(self)

        # TODO: 계산 결과가 맞지 않음

        scopy.power = scopy.power * oKUAN

        if scopy.coeff != 1:
            if oKUAN.layer == 1:
                c, p = get_coeff_power(scopy.coeff, int(oKUAN.value()))
                scopy.coeff = c
                scopy.power = scopy.power + p
            else:
                oKUAN.coeff *= math.log10(scopy.coeff)
                scopy.power = scopy.power + oKUAN

        scopy.normalize()
        return scopy

    def __radd__(self, other: Union[int, float, KnuthUpArrowNotation]) -> KnuthUpArrowNotation:
        return self + other

    def __rsub__(self, other: Union[int, float, KnuthUpArrowNotation]) -> KnuthUpArrowNotation:
        return -(self - other)

    def __rmul__(self, other: Union[int, float, KnuthUpArrowNotation]) -> KnuthUpArrowNotation:
        return self * other

    def __rtruediv__(self, other: Union[int, float, KnuthUpArrowNotation]) -> KnuthUpArrowNotation:
        pass

    def __rpow__(self, other: Union[int, float, KnuthUpArrowNotation]) -> KnuthUpArrowNotation:
        pass

    def __iadd__(self, other: Union[int, float, KnuthUpArrowNotation]) -> KnuthUpArrowNotation:
        self.unite(self + other)
        return self

    def __isub__(self, other: Union[int, float, KnuthUpArrowNotation]) -> KnuthUpArrowNotation:
        self.unite(self - other)
        return self

    def __imul__(self, other: Union[int, float, KnuthUpArrowNotation]) -> KnuthUpArrowNotation:
        self.unite(self * other)
        return self

    def __idiv__(self, other: Union[int, float, KnuthUpArrowNotation]) -> KnuthUpArrowNotation:
        self.unite(self / other)
        return self

    def __ipow__(self, other: Union[int, float, KnuthUpArrowNotation]) -> KnuthUpArrowNotation:
        self.unite(self ** other)
        return self

    def __eq__(self, other: Union[int, float, KnuthUpArrowNotation]) -> bool:
        if not isinstance(other, KnuthUpArrowNotation):
            oKUAN = KnuthUpArrowNotation(*get_coeff_power(other))
        else:
            oKUAN = other

        if self.level != oKUAN.level:
            return False
        if self.layer != oKUAN.layer:
            return False

        if self.level > 1 or self.layer > 2:
            return self.power == oKUAN.power

        return self.coeff == oKUAN.coeff and self.power == oKUAN.power

    def __ne__(self, other: Union[int, float, KnuthUpArrowNotation]) -> bool:
        return not self == other

    def __gt__(self, other: Union[int, float, KnuthUpArrowNotation]) -> bool:
        if not isinstance(other, KnuthUpArrowNotation):
            oKUAN = KnuthUpArrowNotation(*get_coeff_power(other))
        else:
            oKUAN = other

        if self.level > oKUAN.level:
            return True
        if self.layer > oKUAN.layer:
            return True

        if self.level > 1 or self.layer > 2:
            return self.power > oKUAN.power

        if self.power > oKUAN.power:
            return True

        return self.coeff > other.coeff

    def __lt__(self, other: Union[int, float, KnuthUpArrowNotation]) -> bool:
        return not (self > other or self == other)

    def __ge__(self, other: Union[int, float, KnuthUpArrowNotation]) -> bool:
        return self > other or self == other

    def __le__(self, other: Union[int, float, KnuthUpArrowNotation]) -> bool:
        return not self > other

"""
a = KnuthUpArrowNotation(5)

for i in range(1, 101):
    print(f"5 ^ {i} = {a ** i}")
"""