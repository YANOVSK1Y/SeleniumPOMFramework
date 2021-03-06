

class SingletonType(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

    def clear(cls):
        try:
            del SingletonType._instances[cls]
        except KeyError:
            pass
