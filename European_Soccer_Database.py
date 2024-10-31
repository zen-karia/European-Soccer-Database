import csv
import matplotlib.pyplot as plt
import tkinter as tk
import os


def main():
        new_window = tk.Tk()
        new_window.title("Functions")
        new_window.geometry("400x400")
        tk.Label(new_window, text = "\n\t     Welcome to the European Soccer Game Data Analysis Program.\
                 \nWhat do you want to do?\n").pack()
        bnew = tk.Button(new_window, text = "Create a New File", command = New_File).pack()
        bread = tk.Button(new_window, text = "Read an Existing File", command = Read_File).pack()
        bapp = tk.Button(new_window, text = "Append in an Existing File", command = Append_File).pack()
        bsearch = tk.Button(new_window, text = "Search for a record in a File", command = Search_File).pack()
        bmod = tk.Button(new_window, text = "Modify a record in a File", command = Modify_File).pack()
        bgraph = tk.Button(new_window, text = "Plot graph for comparison", command = Graph_File).pack()
        bdel = tk.Button(new_window, text = "Delete a File", command = Delete_File).pack()
        bex = tk.Button(new_window, text = "EXIT", command=new_window.destroy).pack()
        new_window.mainloop()

def Content():
   new_window_1 = tk.Tk()
   new_window_1.title("New Record!")
   new_window_1.geometry("400x400")
   def save_text():
      with open("Soccer.csv", 'a', newline='') as fin:
         w = csv.writer(fin)
         t1 = tb1.get()
         t2 = tb2.get()
         t3 = tb3.get()
         t4 = tb4.get()
         w.writerow([t1, t2, t3, t4])
      b = tk.Label(new_window_1, text = "Contents Added! Do you want to enter more?").pack()
      b1 = tk.Button(new_window_1, text = "YES", command=input).pack()
      b2 = tk.Button(new_window_1, text = "NO", command = new_window_1.destroy).pack()
   def input():
      global tb1, tb2, tb3, tb4
      tk.Label(new_window_1, text = "Enter the country name of the team").pack()
      tb1 = tk.Entry(new_window_1)
      tb1.pack()
      tk.Label(new_window_1, text = "Enter the matches won by that team").pack()
      tb2 = tk.Entry(new_window_1)
      tb2.pack()
      tk.Label(new_window_1, text = "Enter player name").pack()
      tb3 = tk.Entry(new_window_1)
      tb3.pack()
      tk.Label(new_window_1, text = "Enter goals scored by that player").pack()
      tb4 = tk.Entry(new_window_1)
      tb4.pack()
      tk.Button(new_window_1, text = "Save to Soccer.csv", command = save_text).pack(pady = 10)
   input()     

def New_File():
   fin = open("Soccer.csv", 'w', newline='')
   w = csv.writer(fin)
   w.writerow(["Country Name", "Matches Won", "Player Name", "Goals Scored by the Player"])
   fin.close()
   Content()    

def Read_File():
   global data
   data = []
   def open_file():
      with open("Soccer.csv", 'r', newline = '') as fin:
         r = csv.reader(fin)
         for i in r:
            data.append(i)
   open_file()
   new_window_1 = tk.Tk()
   new_window_1.title("File Reader")
   text = tk.Text(new_window_1, width=70, height=50)
   text.pack()
   for i in data:
      text.insert("end", ",\t".join(i) + "\n")


def Append_File():
   Content()

def Search_File():
  def search():
   pname = search_entry.get()
   with open("Soccer.csv", 'r', newline='') as fin:
      r = csv.reader(fin)
      for i in r:
         if i[2].lower() == pname.lower():
            result_text.insert("end", "\t".join(i) + "\n")
            return
      result_text.insert("No such record found!\nPlease open the Functions window to continue.")

  new_window_1 = tk.Tk()
  new_window_1.title("Search Record")
  tk.Label(new_window_1, text="Enter player name whose record you wish to search:").pack()
  search_entry = tk.Entry(new_window_1)
  search_entry.pack()
  tk.Button(new_window_1, text="Search", command=search).pack()
  result_text = tk.Text(new_window_1, width=90, height=30)
  result_text.pack()

def Modify_File():
   def checkmodify():
      pname = modify_entry.get()
      playeristhere = False

      with open("Soccer.csv", 'r', newline='') as fin:
         data = list(csv.reader(fin))
         for row in data:
               if row[2].strip().lower() == pname.lower():
                  playeristhere = True
                  break

      if playeristhere:
         add_data()
      else:
         result_text.insert(tk.END, "No such record found!\nPlease open the Functions window to continue.\n")

   def modify():
      pname = modify_entry.get()
      modified = False
      newrows = []

      with open("Soccer.csv", 'r', newline='') as fin:
         data = list(csv.reader(fin))

      for row in data:
         if row[2].strip().lower() == pname.lower():
               row = [tb1.get(), tb2.get(), tb3.get(), tb4.get()]
               modified = True
         newrows.append(row)

      with open("Soccer.csv", 'w', newline='') as fout:
         w = csv.writer(fout)
         w.writerows(newrows)

      if modified:
         result_text.insert(tk.END, "Record updated.\nPlease open the Functions window to continue.\n")
      else:
         result_text.insert(tk.END, "No such record found!\nPlease open the Functions window to continue.\n")

   def add_data():
      tk.Label(new_window_1, text="Enter the country name of the team").pack()
      tb1.pack()
      tk.Label(new_window_1, text="Enter the matches won by that team").pack()
      tb2.pack()
      tk.Label(new_window_1, text="Enter player name").pack()
      tb3.pack()
      tk.Label(new_window_1, text="Enter goals scored by that player").pack()
      tb4.pack()
      tk.Button(new_window_1, text="Modify Record", command=modify).pack()
        
   new_window_1 = tk.Tk()
   new_window_1.title("Modify Record")

   tk.Label(new_window_1, text="Enter player name whose record you wish to modify:").pack()
   modify_entry = tk.Entry(new_window_1)
   modify_entry.pack()
   tk.Button(new_window_1, text="Next", command=checkmodify).pack()
   result_text = tk.Text(new_window_1, width=80, height=10)
   result_text.pack()

   tb1 = tk.Entry(new_window_1)
   tb2 = tk.Entry(new_window_1)
   tb3 = tk.Entry(new_window_1)
   tb4 = tk.Entry(new_window_1)

def Delete_File():
   def delete():
      os.remove("Soccer.csv")
   new_window_1 = tk.Tk()
   tk.Label(new_window_1, text = "Warning! You're going to delete the file. Do you want to go ahead?\n").pack()

   # lambda is used for multiple commands
   tk.Button(new_window_1, text = "YES", command=lambda: [delete(), new_window_1.destroy()]).pack()
   tk.Button(new_window_1, text = "NO", command = new_window_1.destroy).pack()

def Graph_File():
   data = []
   with open("Soccer.csv", 'r', newline = '') as fin:
      r = csv.reader(fin)
      for i in r:
         data.append(i)
   def t():
      x = []
      y = []
      for i in data:
         if i[0] == "Country Name":
            continue
         else:
            y.append(i[0])
            x.append(int(i[1]))
      plt.barh(y, x, label = "Goals Scored")
      plt.title("Team VS Goals")
      plt.ylabel("Countries")
      plt.xlabel("Goals Scored")
      plt.legend()
      for i,n in enumerate(x):
         plt.text(n, i, str(n))
      plt.show()
   
   def p():
      x = []
      y = []
      for i in data:
         if i[0] == "Country Name":
            continue
         else:
            y.append(i[2])
            x.append(int(i[3]))
      plt.barh(y, x, label = "Goals Scored")
      plt.title("Player VS Goals")
      plt.ylabel("Players")
      plt.xlabel("Goals Scored")
      plt.legend()
      for i,n in enumerate(x):
         plt.text(n, i, str(n))
      plt.show()

   new_window_1 = tk.Tk()
   new_window_1.geometry("400x400")
   tk.Label(new_window_1, text = "Select one of the following")
   g1 = tk.Button(new_window_1, text = "Plot graph between Team and Goals Scored by the Team", command=t).pack(pady = 20)
   p1 = tk.Button(new_window_1, text = "Plot graph between Player and Goals Scored by the Team", command=p).pack()

main()