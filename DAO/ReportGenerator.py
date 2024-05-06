from DatabaseContext import DatabaseContext

class ReportGenerator:
    def __init__(self, db_name):
        self.db_context = DatabaseContext(db_name)

    def generate_reservation_report(self):
        query = "SELECT * FROM Reservation"
        reservations = self.db_context.runQuery(query)
        return reservations

    def generate_vehicle_report(self):
        query = "SELECT * FROM Vehicle"
        vehicles = self.db_context.runQuery(query)
        return vehicles