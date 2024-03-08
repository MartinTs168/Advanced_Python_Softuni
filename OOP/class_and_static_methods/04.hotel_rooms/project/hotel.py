from project.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars: int):
        return cls(f"{stars} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        try:
            room = next(filter(lambda x: x.number == room_number, self.rooms))

        except StopIteration:
            return

        result = room.take_room(people)

        if not result:
            self.guests += people

    def free_room(self, room_number):
        try:
            room = next(filter(lambda x: x.number == room_number, self.rooms))

        except StopIteration:
            return

        room_guests = room.guests
        result = room.free_room()

        if not result:
            self.guests -= room_guests

    def status(self):
        return (f"Hotel {self.name} has {self.guests} total guests\n"
                f"Free rooms: {', '.join(str(r.number) for r in self.rooms if not r.is_taken)}\n"
                f"Taken rooms: {', '.join(str(r.number) for r in self.rooms if r.is_taken)}")

