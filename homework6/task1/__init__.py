def instances_counter(cls):
    class NewClass(cls):
        counter = 0

        def __init__(self):
            super().__init__()
            NewClass.counter += 1

        @classmethod
        def get_created_instances(cls):
            return cls.counter

        @classmethod
        def reset_instances_counter(cls):
            counter_value, cls.counter = cls.counter, 0
            return counter_value

    return NewClass
