def create_metro_map(g):
    g.add_vertex("Noida Sector 62~B")
    g.add_vertex("Botanical Garden~B")
    g.add_vertex("Yamuna Bank~B")
    g.add_vertex("Rajiv Chowk~BY")
    g.add_vertex("Vaishali~B")
    g.add_vertex("Moti Nagar~B")
    g.add_vertex("Janak Puri West~BO")
    g.add_vertex("Dwarka Sector 21~B")
    g.add_vertex("Huda City Center~Y")
    g.add_vertex("Saket~Y")
    g.add_vertex("Vishwavidyalaya~Y")
    g.add_vertex("Chandni Chowk~Y")
    g.add_vertex("New Delhi~YO")
    g.add_vertex("AIIMS~Y")
    g.add_vertex("Shivaji Stadium~O")
    g.add_vertex("DDS Campus~O")
    g.add_vertex("IGI Airport~O")
    g.add_vertex("Rajouri Garden~BP")
    g.add_vertex("Netaji Subhash Place~PR")
    g.add_vertex("Punjabi Bagh West~P")

    g.add_edge("Noida Sector 62~B", "Botanical Garden~B", 8)
    g.add_edge("Botanical Garden~B", "Yamuna Bank~B", 10)
    g.add_edge("Yamuna Bank~B", "Vaishali~B", 8)
    g.add_edge("Yamuna Bank~B", "Rajiv Chowk~BY", 6)
    g.add_edge("Rajiv Chowk~BY", "Moti Nagar~B", 9)
    g.add_edge("Moti Nagar~B", "Janak Puri West~BO", 7)
    g.add_edge("Janak Puri West~BO", "Dwarka Sector 21~B", 6)
    g.add_edge("Huda City Center~Y", "Saket~Y", 15)
    g.add_edge("Saket~Y", "AIIMS~Y", 6)
    g.add_edge("AIIMS~Y", "Rajiv Chowk~BY", 7)
    g.add_edge("Rajiv Chowk~BY", "New Delhi~YO", 1)
    g.add_edge("New Delhi~YO", "Chandni Chowk~Y", 2)
    g.add_edge("Chandni Chowk~Y", "Vishwavidyalaya~Y", 5)
    g.add_edge("New Delhi~YO", "Shivaji Stadium~O", 2)
    g.add_edge("Shivaji Stadium~O", "DDS Campus~O", 7)
    g.add_edge("DDS Campus~O", "IGI Airport~O", 8)
    g.add_edge("Moti Nagar~B", "Rajouri Garden~BP", 2)
    g.add_edge("Punjabi Bagh West~P", "Rajouri Garden~BP", 2)
    g.add_edge("Punjabi Bagh West~P", "Netaji Subhash Place~PR", 3)
