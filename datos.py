heuristica = {
    "Arad": 366, "Bucharest": 0, "Craiova": 160, "Dobreta": 242, "Eforie": 161, "Fagaras": 176, 
    "Giurgiu": 77, "Hirsova": 151,"Iasi": 226, "Lugoj": 244, "Mehadia": 241, "Neamt": 234, 
    "Oradea": 380, "Pitesti": 101, "Rimnicu Vilcea": 193, "Sibiu": 253, "Timisoara": 329,
    "Urziceni": 80, "Vaslui": 199, "Zerind": 374
}

conexiones = {
    "Arad": {"Zerind": 75, "Sibiu": 140, "Timisoara": 118},
    "Bucharest": {"Pitesti": 101, "Fagaras": 211, "Giurgiu": 90, "Urziceni": 85},
    "Craiova": {"Dobreta": 120, "Rimnicu Vilcea": 146, "Pitesti": 138},
    "Dobreta": {"Mehadia": 75, "Craiova": 120},
    "Eforie": {"Hirsova": 86},
    "Fagaras": {"Sibiu": 99, "Bucharest": 211},
    "Giurgiu": {"Bucharest": 90},
    "Hirsova": {"Urziceni": 98, "Eforie": 86},
    "Iasi": {"Neamt": 87, "Vaslui": 92},
    "Lugoj": {"Timisoara": 111, "Mehadia": 75}, 
    "Mehadia": {"Lugoj": 70, "Dobreta": 75},
    "Neamt": {"Iasi": 87}, 
    "Oradea": {"Zerind": 71, "Sibiu": 151},
    "Pitesti": {"Rimnicu Vilcea": 97, "Craiova": 138, "Bucharest": 101},
    "Rimnicu Vilcea": {"Sibiu": 80, "Craiova": 148, "Pitesti": 97},
    "Sibiu": {"Arad": 140, "Fagaras": 99, "Rimnicu Vilcea": 80},
    "Timisoara": {"Arad": 118, "Lugoj": 111},
    "Urziceni": {"Bucharest": 85, "Vaslui": 142, "Hirsova": 98},
    "Vaslui": {"Iasi": 92, "Urziceni": 142},
    "Zerind": {"Oradea": 71, "Arad": 75}
}