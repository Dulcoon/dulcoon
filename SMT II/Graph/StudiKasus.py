import os

class Node:
    def __init__(self, nama, noIdentitas, programStudi, daftarTeman):
        self.nama = nama
        self.noIdentitas = noIdentitas
        self.programStudi = programStudi
        self.daftarTeman = daftarTeman

class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ":",self.adj_list[vertex])

    def add_vertex(self, vertex):
        new_node = Node(vertex)
        if vertex not in self.adj_list.keys():
            self.adj_list[new_node] = []
            return True
        return False
    
    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2) 
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].remove(v2) 
            self.adj_list[v2].remove(v1)
            return True
        return False
    
    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            for other_vertex in self.adj_list.keys():
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False

if __name__=="__main__":     
    my_graph = Graph()
    while True:
        print("="*40)
        print("Graph App")
        print("1. Show My Graph")
        print("2. Add Vertex")
        print("3. Add Edge")
        print("4. Remove Edge")
        print("5. Remove Vertex")
        menu = input("Insert Menu :")
        if menu == "1":
            print("My Graph : ")
            my_graph.print_graph()
            input("Press [ENTER] to Continue...")
            os.system("cls")
        elif menu == "2":
            vtx = input("Input Your New Vertex :")
            if my_graph.add_vertex(vtx):
                print("Adding Vertex Successfull!")
                input("Press [ENTER] to Continue...")
                os.system("cls")
            else:
                print("Adding Vertex Failed,")
                print("Your Vertex Already Exist In The List")
                input("Press [ENTER] to Continue...")
            os.system("cls")
        elif menu == "3":
            v1 = input("Insert Your First Vertex :")
            v2 = input("Insert Your Second Vertex :")
            if my_graph.add_edge(v1, v2):
                print("Add Edge Succesfull")
                input("Press [ENTER] to Continue...")
                os.system("cls")
            else:
                print("Add Edge Failed, Maybe Your v1 or V2 Not In Adj List Yet")
                input("Press [ENTER] to Continue...")
                os.system("cls")
        elif menu == "4":
            v1 = input("Insert Your First Vertex :")
            v2 = input("Insert Your Second Vertex :")
            if my_graph.remove_edge(v1, v2):
                print("Remove Edge Succesfull")
                input("Press [ENTER] to Continue...")
                os.system("cls")
            else:
                print("Remove Edge Failed, Maybe Your v1 or V2 Not In Adj List Yet")
                input("Press [ENTER] to Continue...")
                os.system("cls")
        elif menu == "5":
            vtx = input("Insert Your Vertex That You Want to Delete :")
            if my_graph.remove_vertex(vtx):
                print("Remove Vertex Succesfull")
                input("Press [ENTER] to Continue...")
                os.system("cls")
            else:
                print("Remove Vertex Failed, Maybe Your Vertex Not In Adj List Yet")
                input("Press [ENTER] to Continue...")
                os.system("cls")
        else:
            print("Input Incorrect!")
            input("Press [ENTER] to Continue...")
            os.system("cls")