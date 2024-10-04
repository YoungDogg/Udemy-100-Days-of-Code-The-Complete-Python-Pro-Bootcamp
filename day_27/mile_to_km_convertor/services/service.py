# convert mile to km
class Service:
    def __init__(self, **kwargs):
        self.miles = kwargs.get('miles',0)
        self.kilometers = self.converter_ml2km(self.miles)

    @staticmethod
    def converter_ml2km(miles):
        return round(miles * 1.60934,2)

    def __str__(self):
        return f"{self.miles} miles is equal to {self.kilometers} kilometers"


if __name__ == "__main__":
    service = Service(miles=10)
    print(service)
