class GlobalValue:
    _instance = None
    value = 0

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(GlobalValue, cls).__new__(cls)
        return cls._instance
