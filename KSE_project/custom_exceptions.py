class PowerNotInRange(Exception):

    def __init__(self, message="Error was raised while initializing class because condition 0 < power_min < power_max < 2500 was not met"):
        self.message = message
        super().__init__(self.message)


class YearNotInRange(Exception):

    def __init__(self, message="Error was raised while initializing class because condition 1950 < year_start < year__end < 2100 was not met"):
        self.message = message
        super().__init__(self.message)


class EfficiencyNotInRange(Exception):

    def __init__(self, message="Error was raised while initializing class because condition 0 < efficiency < 1 was not met"):
        self.message = message
        super().__init__(self.message)


class PlantTypeNotInTypes(Exception):

    def __init__(self, message="Error was raised while initializing class because plant type was not defined type for plant in program"):
        self.message = message
        super().__init__(self.message)
