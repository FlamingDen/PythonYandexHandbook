class Broken:
    def __repr__(self):
        raise Exception


a = Broken()
func(a)
