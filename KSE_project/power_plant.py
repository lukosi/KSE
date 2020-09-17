import custom_exceptions as ex


class PowerPlant:

    id_plant = 0
    plants = {}
    plants_name = {}
    plants_type = ["wk", "wk_new"]

    def __init__(self, name, plant_type, p_min, p_max, year_start, year_end):
        self.name = name
        self.plant_type = plant_type
        self.p_min = p_min
        self.p_max = p_max
        self.year_start = year_start
        self.year_end = year_end
        self.bands = {}

        # Exceptions handling
        if not 0 < self.p_min < self.p_max < 2000:
            raise ex.PowerNotInRange
        if not 1950 < self.year_start < self.year_end < 2100:
            raise ex.YearNotInRange
        if self.plant_type not in PowerPlant.plants_type:
            raise ex.PlantTypeNotInTypes

        self.add_plant()
        self.create_bands()

    def __str__(self):
        return self.name

    def add_plant(self):
        PowerPlant.plants[PowerPlant.id_plant] = self
        PowerPlant.plants_name[PowerPlant.id_plant] = self.name
        PowerPlant.id_plant += 1

    def create_bands(self):
        n_bands = 10
        self.bands[1] = self.p_min
        for i in range(2, n_bands + 1):
            self.bands[i] = self.p_min + ((self.p_max - self.p_min) / n_bands) * i


plant1 = PowerPlant("KOZ 1", "wk_new", 100, 500, 2010, 2040)
plant2 = PowerPlant("KOZ 2", "wk", 50, 200, 1990, 2025)

# drafts

# print(getattr(plant1, "plant_type"))  # The other way to access attributes (variables) it to use the getattr() and setattr() functions.
# print(plant1)
# print(PowerPlant.plants[1].name)
# print(PowerPlant.plants_name[0])
print(plant1.bands[2])





