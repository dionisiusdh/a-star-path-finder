import queue
from graph import *
from node import *


# Baca nama graf yang mau dibaca
#   graphName = input("Masukkan nama graf input: ")
graphName = "MapITB"
print()


# Baca nama graf yang mau dibaca
#   graphName = input("Masukkan nama graf input: ")
graphName = "MapITB"
print()


# Baca input simpul awal dan akhir
#   start = input("Masukkan simpul awal: ")
start = "Scoop and Skoops"
#   end = input("Masukkan simpul tujuan: ")
end = "Galaksi Bima Sakti"


# Buat graf dari nama graf input
g = makeGraphFromTxt(graphName, end)
# g.printGraph()


# Cari node start dan end
# for node in g.nodes:
#   if (node.name == start):
#     startNode = node
#   elif (node.name == end):
#     endNode = node
startNode = g.findNode(start)
endNode = g.findNode(end)


# Make priority queue to store nodes
q = queue.PriorityQueue()

# Deklarasikan dictionary kosong untuk rekam jejak parent dan rekam jejak total
# jarak kumulatif yang paling singkat untuk ke node tertentu
jalur = {}
kumulatifMeter = {}

# Inisiasi dengan none, karena parent dari starting node tidak ada, dan 0.0
# untuk jarak kumulatif, karena jarak dari start ke start adalah 0
jalur[start] = None
kumulatifMeter[start] = 0.0

# Set starting node
q.put((0, start))

# Inisiasikan currNodeName dengan nilai acak agar bisa masuk ke loop
currNodeName = -999


# jalankan loop asalkan belum sampai tujuan atau masih ada elemen prioqueue
while (q.qsize() > 0 and currNodeName != end):
  (currPrio, currNodeName) = q.get()

  for nextNodeName in g.findNode(currNodeName).neighbors:
    addedMeter = kumulatifMeter[currNodeName] + g.findNode(currNodeName).neighbors[nextNodeName]

    # menambahkan kumulatifMeter baru apabila belum ada dictionary key : nextNodeName
    if (not(nextNodeName in kumulatifMeter)):
      # menambahkan kumulatifMeter baru
      kumulatifMeter[nextNodeName] = addedMeter

      # prioritas untuk nextNodeName dikalkulasi dengan menambahkan addedMeter dan nilai 
      # heuristik nextNodeName
      nextPrio = addedMeter + g.findNode(nextNodeName).heuristik
      
      # memasukan prio dan nama node ke dalam prioqueue
      q.put((nextPrio, nextNodeName))

      # menambahkan riwayat jalur
      jalur[nextNodeName] = currNodeName

    # menambahkan kumulatifMeter baru apabila kumulatifMeter yang sebelumnya
    # ternyata tidak optimal
    if (addedMeter < kumulatifMeter[nextNodeName]):
      # menambahkan kumulatifMeter baru
      kumulatifMeter[nextNodeName] = addedMeter

      # prioritas untuk nextNodeName dikalkulasi dengan menambahkan addedMeter dan nilai 
      # heuristik nextNodeName
      nextPrio = addedMeter + g.findNode(nextNodeName).heuristik
      
      # memasukan prio dan nama node ke dalam prioqueue
      q.put((nextPrio, nextNodeName))

      # menambahkan riwayat jalur
      jalur[nextNodeName] = currNodeName


# skema pencetakan hasil
if (currNodeName == end):
  # mencetak jarak terpendek antar node awal dan tujuan
  print(f"Jarak terpendek dari {start} ke {end}: {kumulatifMeter[end]}\n")

  # list untuk nanti dibalikan
  reverseDirection = []

  # iterasi mulai dari element parent ending node
  iterPrint = jalur[end]

  # selagi belum none (iterprint merupakan elemen parent dari starting node)
  while (iterPrint != None):
    # append ke list kemudian iterasikan berikutnya
    reverseDirection.append(iterPrint)
    iterPrint = jalur[iterPrint]

  # print array dengan orientasi reverse agar dari node awal-tujuan
  for nodeName in reversed(reverseDirection):
    print(nodeName, end=" → ")

  # node tujuan
  print(end, end="\n\n")

# apabila tidak ditemukan jalur
else:
  # cetak tidak ada jalur
  print(f"Tidak ada jalur yang menghubungi {start} dan {end}\n")




# CORETAN HAMPIRRR
'''
# Set current node
currNode = startNode


# Get initial neighbors of starting node
for nodeName in currNode.neighbors:
  # simpan nama node
  node = g.findNode(nodeName)

  # cari g(n) yang ditambah ke f(n)
  addedCost = currNode.neighbors[nodeName]

  # tambahkan tuple f(n) dan node ke queue
  q.put((node.heuristik + addedCost, node))
  
print("\nROUND TWO\n")
# Loop from start node selagi queue tidak kosong dan belum sampai node tujuan
while (q.qsize() > 0 and currNode.name != endNode.name):
  # cari next node dan prioritas yang akan di traverse
  (nextPriority, nextNode) = q.get()

  # catat cost kumulatif untuk next node
  nextNode.cost += (nextPriority - nextNode.heuristik)

  # simpan parent pada array of parent
  nextNode.parents.extend(currNode.parents)
  nextNode.parents.append(currNode)

  print(f"\nPARENTS untuk {nextNode.name.upper()}:")
  for i in nextNode.parents: print(i.name)

  # ubah node yang akan diproses menjadi nextNode
  currNode = nextNode

  print(f"COST SO FAR: {currNode.cost}")
  print(f"NEIGHBORS of {currNode.name.upper()}:")

  # looping semua neighbor dari node yang akan diproses
  for nodeName in currNode.neighbors:
    # simpan nama node tetangga
    node = g.findNode(nodeName)
    
    # cari g(n) yang akan ditambah ke f(n)
    addedCost = currNode.cost + currNode.neighbors[nodeName]

    

    # tambahkan f(n) dan node ke queue
    q.put((node.heuristik + addedCost, node))
  
  print()


i = len(endNode.parents) - 1 - endNode.parents[::-1].index(startNode)

print()

while (i < len(endNode.parents)): 
  print(endNode.parents[i].name, end=" - ")
  i += 1

print(end + "\n")

print(f"Jarak terpendek dari {start} ke {end}: {endNode.cost}\n")
'''

# GANTI CARA CETAK, MASIH ADA EDGE CASE GAGAL
'''
# pencetakan hasil
# init list kosong untuk membalikan urutan arah dengan aturan LIFO
reverseDirection = []

# mulai dari node terakhir
currIterNode = endNode.parents.pop()

# selagi belum sampai ke start
while (len(endNode.parents) > 0):
  # tambahkan node tersebut ke list
  reverseDirection.append(currIterNode.name)
  
  # keluar dari loop jika sudah sampai start node
  if (currIterNode == startNode):
    break

  # ganti current iterator node
  currIterNode = endNode.parents.pop()
  

# cetak selagi masih ada elemen list
while (len(reverseDirection) > 0):
  # apabila tersisa masih lebih dari 1 elemen
  if (len(reverseDirection) > 1):
    # cetak dengan akhiran ' - '
    print(reverseDirection.pop(), end=" - ")
  else: # kondisi lain
    print(reverseDirection.pop() + "\n")

print(f"Jarak terpendek dari {start} ke {end}: {endNode.cost}\n")'''

# MENGGUNAKAN ITERATOR NODE 
'''
# pencetakan hasil
if (currNode.name != endNode.name):
  print(f"Tidak ada jalur yang menghubungi {start} dan {end}\n")
else:
  # init list kosong untuk membalikan urutan arah dengan aturan LIFO
  reverseDirection = []
  
  # mulai dari node terakhir
  currIterNode = endNode

  # selagi belum sampai ke start
  while (currIterNode != None):
    # tambahkan node tersebut ke list
    reverseDirection.append(currIterNode.name)
    
    # mundur ke parent dari node kini
    currIterNode = currIterNode.parent

  # cetak selagi masih ada elemen list
  while (len(reverseDirection) > 0):
    # apabila tersisa masih lebih dari 1 elemen
    if (len(reverseDirection) > 1):
      # cetak dengan akhiran ' - '
      print(reverseDirection.pop(), end=" - ")
    else: # kondisi lain
      print(reverseDirection.pop())

  print(f"Jarak terpendek dari {start} ke {end}: {endNode.cost}\n")'''