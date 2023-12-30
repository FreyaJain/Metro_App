from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt
import streamlit as st
import heapq

class Graph_M:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_vertex(self, vertex):
        self.graph[vertex]

    def add_edge(self, src, dest, weight):
        self.graph[src].append((dest, weight))
        self.graph[dest].append((src, weight))

    def containsVertex(self, vertex):
        return vertex in self.graph

    def hasPath(self, src, dest, processed):
        processed[src] = True
        if src == dest:
            return True
        for neighbor, _ in self.graph[src]:
            if not processed[neighbor] and self.hasPath(neighbor, dest, processed):
                return True
        return False

    def dijkstra(self, src, dest, is_time):
        pq = [(0, src)]
        distances = {vertex: float('infinity') for vertex in self.graph}
        distances[src] = 0

        while pq:
            current_distance, current_vertex = heapq.heappop(pq)

            if current_vertex == dest:
                return distances[current_vertex]

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.graph[current_vertex]:
                if is_time:
                    new_distance = current_distance + weight / 60  # convert minutes to hours
                else:
                    new_distance = current_distance + weight

                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(pq, (new_distance, neighbor))

        return float('infinity')

    def get_Interchanges(self, path):
        result = []
        for i in range(len(path) - 1):
            src, dest = path[i], path[i + 1]
            if src[-1] != dest[-1]:
                result.append(src)
        result.append(path[-1])  # add the last station
        return result

    def Get_Minimum_Distance(self, src, dest):
        pq = [(0, src, [])]
        distances = {vertex: float('infinity') for vertex in self.graph}
        distances[src] = 0

        while pq:
            current_distance, current_vertex, path = heapq.heappop(pq)

            if current_vertex == dest:
                return path + [current_vertex]

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.graph[current_vertex]:
                new_distance = current_distance + weight

                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(pq, (new_distance, neighbor, path + [current_vertex]))

        return []

    def Get_Minimum_Time(self, src, dest):
        pq = [(0, src, [])]
        distances = {vertex: float('infinity') for vertex in self.graph}
        distances[src] = 0

        while pq:
            current_time, current_vertex, path = heapq.heappop(pq)

            if current_vertex == dest:
                return path + [current_vertex]

            if current_time > distances[current_vertex]:
                continue

            for neighbor, weight in self.graph[current_vertex]:
                new_time = current_time + weight / 60  # convert minutes to hours

                if new_time < distances[neighbor]:
                    distances[neighbor] = new_time
                    heapq.heappush(pq, (new_time, neighbor, path + [current_vertex]))

        return []
    
    def display_stations(self):
        st.write("Metro Stations:")
        for vertex in self.graph:
            st.text(vertex)
            
    def display_map(self):
        st.write("Metro Map:")
        # Create a directed graph
        G = nx.DiGraph()
        for vertex, neighbors in self.graph.items():
            for neighbor, _ in neighbors:
                G.add_edge(vertex, neighbor)
        # Draw the graph using matplotlib
        fig, ax = plt.subplots()
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=False, node_size=500, font_size=6, font_color='black', font_weight='bold',
        node_color='skyblue', edge_color='gray', linewidths=2, arrowsize=10) 
        nx.draw_networkx_labels(G, pos,font_size=6, font_color='black', font_weight='bold')
        # Display the plot in Streamlit
        st.pyplot(fig, clear_figure=True)

    
    def create_metro_map(self):
        self.add_vertex("Noida Sector 62~B")
        self.add_vertex("Botanical Garden~B")
        self.add_vertex("Yamuna Bank~B")
        self.add_vertex("Rajiv Chowk~BY")
        self.add_vertex("Vaishali~B")
        self.add_vertex("Moti Nagar~B")
        self.add_vertex("Janak Puri West~BO")
        self.add_vertex("Dwarka Sector 21~B")
        self.add_vertex("Huda City Center~Y")
        self.add_vertex("Saket~Y")
        self.add_vertex("Vishwavidyalaya~Y")
        self.add_vertex("Chandni Chowk~Y")
        self.add_vertex("New Delhi~YO")
        self.add_vertex("AIIMS~Y")
        self.add_vertex("Shivaji Stadium~O")
        self.add_vertex("DDS Campus~O")
        self.add_vertex("IGI Airport~O")
        self.add_vertex("Rajouri Garden~BP")
        self.add_vertex("Netaji Subhash Place~PR")
        self.add_vertex("Punjabi Bagh West~P")

        self.add_edge("Noida Sector 62~B", "Botanical Garden~B", 8)
        self.add_edge("Botanical Garden~B", "Yamuna Bank~B", 10)
        self.add_edge("Yamuna Bank~B", "Vaishali~B", 8)
        self.add_edge("Yamuna Bank~B", "Rajiv Chowk~BY", 6)
        self.add_edge("Rajiv Chowk~BY", "Moti Nagar~B", 9)
        self.add_edge("Moti Nagar~B", "Janak Puri West~BO", 7)
        self.add_edge("Janak Puri West~BO", "Dwarka Sector 21~B", 6)
        self.add_edge("Huda City Center~Y", "Saket~Y", 15)
        self.add_edge("Saket~Y", "AIIMS~Y", 6)
        self.add_edge("AIIMS~Y", "Rajiv Chowk~BY", 7)
        self.add_edge("Rajiv Chowk~BY", "New Delhi~YO", 1)
        self.add_edge("New Delhi~YO", "Chandni Chowk~Y", 2)
        self.add_edge("Chandni Chowk~Y", "Vishwavidyalaya~Y", 5)
        self.add_edge("New Delhi~YO", "Shivaji Stadium~O", 2)
        self.add_edge("Shivaji Stadium~O", "DDS Campus~O", 7)
        self.add_edge("DDS Campus~O", "IGI Airport~O", 8)
        self.add_edge("Moti Nagar~B", "Rajouri Garden~BP", 2)
        self.add_edge("Punjabi Bagh West~P", "Rajouri Garden~BP", 2)
        self.add_edge("Punjabi Bagh West~P", "Netaji Subhash Place~PR", 3)


