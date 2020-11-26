class Snakes :
    # Class variable
    _snake_number = 0
    # Constructor
    def __init__(self, snake_name, snake_type, member = None) :
        Snakes._snake_number = Snakes._snake_number + 1
        self._snake_name = snake_name
        self._snake_type = snake_type
        self._member = member
    # GET
    def getSnakeNumber(self) :
        return self._snake_number
    def getSnakeName(self) :
        return self._snake_name
    def getSnakeType(self) :
        return self._snake_type
    def getMember(self) :
        return self._member
    # SET
    def setSnakeName(self, snake_name) :
        self._snake_name = snake_name
    def setSnakeType(self, snake_type) :
        self._snake_type = snake_type
    def setMember(self, member) :
        self._member = member
    # ToString
    def ToString(self) :
        return self.getSnakeName() + " has the id: " + str(self.getSnakeNumber()) + " and is a " + self.getSnakeType() + ". It's owner is: " + str(self.getMember())