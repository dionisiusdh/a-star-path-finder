import queue
from graph import *
from node import *
from visualizer import *

"""
FUNCTIONS
"""
def welcomeMessage():
  print("=========================")
  print("=     A* Pathfinder     =")
  print("=========================")

def getGraphInput():
  # Baca nama graf yang mau dibaca
  graphName = input("Masukkan nama graf input (tanpa ekstensi file): ")
  print()

  g = showGraphNode(graphName)

  # Baca input simpul awal dan akhir
  start = input("Masukkan nama simpul awal: ")

  while (start not in g.getAllNodeName()):
    print("Nama simpul tidak ditemukan!")
    start = input("Masukkan nama simpul awal: ")

  end = input("Masukkan nama simpul tujuan: ")
  
  while (end not in g.getAllNodeName()):
    print("Nama simpul tidak ditemukan!")
    end = input("Masukkan nama simpul tujuan: ")

  print()
  return graphName, start, end

"""
MAIN PROGRAM
"""
welcomeMessage()
exit = False

while (not exit):
  graphName, start, end = getGraphInput()

  # Buat graf dari nama graf input
  g = makeGraphFromTxt(graphName, end)

  # Cari node start dan end
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
          addedMeter = kumulatifMeter[currNodeName] + g.findNode(
              currNodeName).neighbors[nextNodeName]

          # menambahkan kumulatifMeter baru apabila belum ada dictionary key : nextNodeName
          if (not (nextNodeName in kumulatifMeter)):
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
      print(f"Jarak terpendek dari {start} ke {end}: {kumulatifMeter[end]} meter \n")
      print("Lintasan:")

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

      # Visualisasi graph
      full_path = list(reversed(reverseDirection))
      full_path.append(end)
      
      visualize(g, full_path, kumulatifMeter[end])

  # apabila tidak ditemukan jalur
  else:
      # cetak tidak ada jalur
      print(f"Tidak ada jalur yang menghubungi {start} dan {end}\n")

  # exit
  exitChoice = input("Apakah anda ingin membaca file lain? (Y/N) : ")

  if (exitChoice == "N" or exitChoice == "n"):
    exit = True

print("Terima kasih!")