class NextIdMixin:
    id = -1  # not necessary only to avoid warning

    @classmethod
    def get_next_id(cls):
        return cls.id

    @classmethod
    def increment_id(cls):
        cls.id += 1
