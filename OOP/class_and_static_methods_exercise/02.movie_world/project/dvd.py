import calendar


class DVD:
    def __init__(self, name: str, dvd_id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = dvd_id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, dvd_id: int, name: str, date: str, age_restriction: int):
        date_info = date.split(".")
        creation_year = int(date_info[2])
        creation_month = calendar.month_name[int(date_info[1])]
        return cls(name, dvd_id, creation_year, creation_month, age_restriction)

    def __repr__(self):
        return (f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction "
                f"{self.age_restriction}. Status: {'rented' if self.is_rented else 'not rented'}")