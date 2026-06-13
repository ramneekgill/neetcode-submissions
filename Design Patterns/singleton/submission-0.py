class Singleton:
    new_instance = None
    # In python consider this method as the 'getInstance'
    def __new__(cls):
        if not cls.new_instance:
            cls.new_instance = super(Singleton,cls).__new__(cls)
        return cls.new_instance


    def getValue(self) -> str:
        return self.val

    def setValue(self, value: str):
        self.val = value
