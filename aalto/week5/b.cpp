#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <list>
#include <queue>

using Llong = int64_t;

template<typename T>
std::ostream &operator<<(std::ostream &os, const std::vector<T> &vec) {
    os << "[";
    if (!vec.empty()) {
        os << vec[0];
    }

    for (std::size_t i = 1; i < vec.size(); i++) {
        os << ", " << vec[i];
    }

    os << "]";
    return os;
}

struct Flight {
        Llong city;
        Llong length;

    public:
        Flight(Llong city, Llong length) : city(city), length(length) {}
};

class Compare {
    public:
        bool operator()(Flight e1, Flight e2) {
            if (e1.length == e2.length) {
                return e1.city < e2.city;
            } else {
                return (e1.length > e2.length);
            }
        }
};

int main() {
    // read number of values
    Llong numCities, numConnections;
    std::cin >> numCities;
    std::cin >> numConnections;

    std::vector<std::vector<Flight>> connections(numCities, std::vector<Flight>());

    for (int i = 0; i < numConnections; i++) {
        int source, dest, length;
        std::cin >> source >> dest >> length;

        // why starting the counting by 1?!
        source--;
        dest--;

        connections[source].push_back(Flight(dest, length));
    }

    std::vector<Llong> dist(numCities, std::numeric_limits<Llong>::max());
    std::vector<bool> processed(numCities, false);

    std::priority_queue<Flight, std::vector<Flight>, Compare> reachableNodes;
    dist[0] = 0;

    reachableNodes.push(Flight(0, 0));

    Llong reachedCount = 0;

    while (reachedCount < numCities) {
        auto u = reachableNodes.top().city;
        reachableNodes.pop();

        if (processed[u]) {
            continue;
        }

        // Mark the picked vertex as processed
        processed[u] = true;
        reachedCount += 1;

        // Update dist value of the adjacent vertices of the picked vertex.
        for (const auto &c: connections[u]) {
            if (!processed[c.city]) {
                auto d = dist[u] + c.length;
                if (d < dist[c.city]) {
                    dist[c.city] = d;
                    reachableNodes.push(Flight(c.city, d));
                }
            }
        }
    }

    for (auto d : dist) {
        std::cout << d << " ";
    }
    std::cout << std::endl;
}

