import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from graph_m import Graph_M

def main():
    st.title("Metro App")
    g = Graph_M()
    g.create_metro_map()

    st.sidebar.header("Actions")
    selected_action = st.sidebar.selectbox(
        "Choose an action",
        ["List All Stations", "Show Metro Map", "Get Shortest Distance", "Get Shortest Time"]
    )

    if selected_action == "List All Stations":
        st.header("List of All Stations")
        g.display_stations()

    elif selected_action == "Show Metro Map":
        st.header("Metro Map")
        g.display_map()

    elif selected_action == "Get Shortest Distance":
        st.header("Get Shortest Distance")
        st.subheader("Choose Source and Destination Stations")
        source_station = st.selectbox("Source Station", list(g.graph.keys()))
        destination_station = st.selectbox("Destination Station", list(g.graph.keys()))

        if st.button("Calculate Shortest Distance"):
            shortest_distance = g.dijkstra(source_station, destination_station, False)
            st.success(f"Shortest Distance from {source_station} to {destination_station}: {shortest_distance} KM")

    elif selected_action == "Get Shortest Time":
        st.header("Get Shortest Time")
        st.subheader("Choose Source and Destination Stations")
        source_station_time = st.selectbox("Source Station", list(g.graph.keys()))
        destination_station_time = st.selectbox("Destination Station", list(g.graph.keys()))

        if st.button("Calculate Shortest Time"):
            shortest_time = g.dijkstra(source_station_time, destination_station_time, True) / 60
            st.success(f"Shortest Time from {source_station_time} to {destination_station_time}: {shortest_time} Minutes")

if __name__ == "__main__":
    main()
