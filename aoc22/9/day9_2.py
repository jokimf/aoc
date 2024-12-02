class Knot:
    def __init__(self) -> None:
        self.row = 0
        self.col = 0
        self.visited = set()

    def __repr__(self) -> str:
        return f'({self.row},{self.col})'

    def walk(self, direction):
        if direction == 'U':
            self.col -=1
        elif direction == 'D':
            self.col +=1  
        elif direction == 'R':
            self.row +=1
        elif direction == 'L':
            self.row -=1

    def keep_up(self, other):
        if self.row + 2 == other.row and self.col + 1 == other.col:
            self.row = other.row - 1
            self.col = other.col
        elif self.row - 2 == other.row and self.col + 1 == other.col:
            self.row = other.row +1
            self.col = other.col
        elif self.row + 2 == other.row and self.col - 1 == other.col:
            self.row = other.row - 1
            self.col = other.col
        elif self.row -2 == other.row and self.col - 1 == other.col:
            self.row = other.row +1
            self.col = other.col
        elif self.row + 1 == other.row and self.col + 2 == other.col:
            self.row = other.row
            self.col = other.col -1
        elif self.row - 1 == other.row and self.col + 2 == other.col:
            self.row = other.row
            self.col = other.col -1
        elif self.row + 1 == other.row and self.col - 2 == other.col:
            self.row = other.row
            self.col = other.col +1
        elif self.row -1 == other.row and self.col - 2 == other.col:
            self.row = other.row
            self.col = other.col +1

        elif self.row - 2 == other.row and self.col -2 == other.col:
            self.row = other.row + 1
            self.col = other.col + 1
        elif self.row -2 == other.row and self.col +2 == other.col:
            self.row = other.row +1
            self.col = other.col -1
        elif self.row + 2 == other.row and self.col -2 == other.col:
            self.row = other.row -1
            self.col = other.col +1
        elif self.row + 2 == other.row and self.col + 2 == other.col:
            self.row = other.row -1
            self.col = other.col -1

        elif self.row + 2 == other.row: # head is to the right
            self.row +=1
        elif self.row -2 == other.row: # head is to the left
            self.row -=1
        elif self.col + 2 == other.col:
            self.col +=1
        elif self.col -2 == other.col:
            self.col -=1
        self.visited.add((self.row,self.col))
        

with open('data.txt') as data:
    TOTAL_KNOTS = 10
    knots = [Knot() for x in range(TOTAL_KNOTS)] # create list of Knots
    for row in data:
        direction, amount = row.strip('\n').split(' ')
        for step in range(0, int(amount)):
            knots[0].walk(direction) # Head walks
            for i in range(1,TOTAL_KNOTS): 
                knots[i].keep_up(knots[i-1]) # Others follow
    print(len(knots[-1].visited)) # Print amount of visited for last node
        