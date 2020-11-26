class Members :
    # Class variable
    _mem_number = 0
    # Constructor
    def __init__(self, mem_name) :
        Members._mem_number = Members._mem_number +1
        self._mem_name = mem_name
    # GET
    def getMemNumber(self) :
        return self._mem_number
    def getMemName(self) :
        return self._mem_name
    # SET
    def setMemName(self, mem_name) :
        self._mem_name = mem_name
    # ToString
    def ToString(self) :
        return "Member with id " + str(self.getMemNumber()) + " is called " + self.getMemName()