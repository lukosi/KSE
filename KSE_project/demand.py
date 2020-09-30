class Demand:

    def __init__(self):
        self.date_dict = {}
        self.temp_dict_hours = {}

    def open_demnad(self, path):

        with open(path, mode="rt", encoding="utf-8") as demand_file:
            for i, hour_line in enumerate(demand_file):
                if i != 0 and hour_line != "\n":
                    year, month, day, hour, demand = hour_line.replace("\n", "").split("\t")
                    date = f'{year}-{month}-{day}'
                    new_demand._add_demand(date, int(hour), float(demand))

    def _add_demand(self, date, hour, value):

        if date not in self.date_dict:
            self.temp_dict_hours.clear()
        self.temp_dict_hours[hour] = value
        self.date_dict[date] = self.temp_dict_hours


new_demand = Demand()
new_demand.open_demnad("demand/demand.txt")
print(new_demand.date_dict['2020-01-01'][3])
