class ReservationException(Exception):
    def __init__(self, message="Reservation Not Found."):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message