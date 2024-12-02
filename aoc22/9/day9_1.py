class Knot:
    def __init__(self) -> None:
        self.row = 0
        self.col = 0
        self.visited = set()

    def walk(self, direction):
        if direction == 'U':
            self.col -=1
        elif direction == 'D':
            self.col +=1  
        elif direction == 'R':
            self.row +=1
        elif direction == 'L':
            self.row -=1
        else:
            raise ValueError('why')

    def keep_up(self, other):
        if self.row + 2 == other.row and self.col + 1 == other.col:
            self.row+=1
            self.col+=1
        elif self.row - 2 == other.row and self.col + 1 == other.col:
            self.row-=1
            self.col+=1
        elif self.row + 2 == other.row and self.col - 1 == other.col:
            self.row+=1
            self.col-=1
        elif self.row -2 == other.row and self.col - 1 == other.col:
            self.row-=1
            self.col-=1
        elif self.row + 1 == other.row and self.col + 2 == other.col:
            self.row+=1
            self.col+=1
        elif self.row - 1 == other.row and self.col + 2 == other.col:
            self.row-=1
            self.col+=1
        elif self.row + 1 == other.row and self.col - 2 == other.col:
            self.row+=1
            self.col-=1
        elif self.row -1 == other.row and self.col - 2 == other.col:
            self.row-=1
            self.col-=1
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
    head = Knot()
    tail = Knot()
    for row in data:
        direction, amount = row.strip('\n').split(' ')
        for step in range(0,int(amount)):
            head.walk(direction)
            tail.keep_up(head)
    print(len(tail.visited))
        
            