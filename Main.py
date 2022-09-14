class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class Queue:
  def __init__(self):
    self.head = None
    self.last = None

  def enqueue(self, data) -> None:
    # Write your code here
    if self.last==None:
      self.last=Node(data)
      self.last.next=None
      self.last.data=data
      self.head=self.last
    else:
      t=Node(data)
      self.last.next=t
      t.data=data
      t.next=None
      self.last=t
  def dequeue(self) -> None:
    # Write your code here
    t=self.head
    if self.head==None:
      return None
    self.head = t.next
    if(self.head == None):
      self.last = None
  def status(self) -> None:
    # Write your code here
    t=self.head
    if self.head==None and self.last==None:
      print("None")
    while(t!=None):
      print(t.data,end="")
      print("=>",end="")
      t=t.next
      if t==None:
        print("None")




# Do not change the following code
queue = Queue()
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = input_data.split(',')
for i in range(len(operations)):
  if operations[i] == "enqueue":
    queue.enqueue(int(data[i]))
  elif operations[i] == "dequeue":
    queue.dequeue()
queue.status()
