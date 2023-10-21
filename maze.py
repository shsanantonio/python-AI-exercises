import sys

class Node():
  def __init__(self, state, parent, action):
    self.state = state
    self.parent = parent
    self.action = action

class StackFrontier(): # Generate objects in python
  def __init__(self):
    self.frontier = []

  def add(self, node):
    self.frontier.append(node)
  
  def contains_state(self, state):
    return any(node.state == state for node in self.frontier)
  
  def empty(self):
    return len(self.frontier) == 0

  def remove(self):
    if self.empty():
      raise Exception("empty frontier")
    
    else:
      node = self.frontier[-1] # gets the last item from the list
      self.frontier = self.frontier[:-1] #removes the last item from the list
      return node

class QueueFrontier(StackFrontier): # inherits StackFrontier meaning it's going to do all the same things that the stack frontier did, only that theres gonna be a slight difference on the methods 

  def remove(self):
    if self.empty():
      raise Exception("empty frontier")
    else:
      node = self.frontier[0] # gets th e first item from the list
      self.frontier = self.frontier[1:]
      return node

class Maze():

  def __init__(self, filename):

    # Read file and set height and width of maze
    with open(filename) as f: # with statement is used in exception handling to make the code cleaner and much more readable. It simplifies the management of common resources like file streams.
      contents = f.read()

    # Validate start and goal
    if contents.count("A") != 1:
      raise Exception("maze must have exactly one start point")
    if contents.count("B") != 1:
      raise Exception("maze must have exactly one goal")

    # Determine height and width of maze
    contents = contents.splitlines()
    self.height = len(contents)
    self.width = max(len(line) for line in contents)

    # Keep tracks of walls
    self.walls = []
    for i in range(self.height):
      row = []
      for j in range(self.width):
        try:
          if contents[i][j] == "A":
            self.start = (i, j)
            row.append(False)
          elif contents[i][j] == "B":
            self.goal = (i, j)
            row.append(False)
          elif contents[i][j] == " ":
            row.append(False)
          else:
            row.append(True)
        except IndexError:
          row.append(False)
      self.walls.append(row)

    self.solution = None
  
  def print(self):
    solution = self.solution[1] if self.solution is not None else None
    print()
    for i, row in enumerate(self.walls):
      for j, col in enumerate(row):
        if col:
          print("▇", end="")
        elif (i, j) == self.start:
          print("A", end="")
        elif(i, j) == self.goal:
          print("B", end="")
        else:
          print(" ", end="")
      print()
    print()






