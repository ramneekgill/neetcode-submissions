class Singleton:
    _new_instance = None
    val = None
    # In python consider this method as the 'getInstance'
    def __new__(cls):
        if not cls._new_instance:
            cls._new_instance = super(Singleton,cls).__new__(cls)
        return cls._new_instance


    def getValue(self) -> str:
        return self.val

    def setValue(self, value: str):
        self.val = value

test = Singleton()
print(test.getValue())
test.setValue('something')
print(test.getValue())