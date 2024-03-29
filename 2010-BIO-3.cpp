// Juggl(ug)ing
// ~1hr10m so far

// EBI: Assignment of vector auto deep copies
// EBI: Checking through logic is important - think of all cases not just given case all the time

#include <bits/stdc++.h>
using namespace std;

// filledVolumes vectors always have distance as last item

vector<tuple<vector<int>,int>> getNextNodes(vector<int> filledVolumes, vector<int> maxVolumes, int numJugs, int distanceFromStart) {
    vector<tuple<vector<int>,int>> nextNodes;
    for(int firstJug = 0; firstJug < numJugs; firstJug++) {
        if(filledVolumes[firstJug] != 0) {
            // Empty
            vector<int> newFilledVolumes = filledVolumes;
            newFilledVolumes[firstJug] = 0;
            tuple<vector<int>, int> nextNode (newFilledVolumes, distanceFromStart+1);
            nextNodes.push_back(nextNode);
        }
        if(filledVolumes[firstJug] != maxVolumes[firstJug]) {
            // Fill up
            vector<int> newFilledVolumes = filledVolumes;
            newFilledVolumes[firstJug] = maxVolumes[firstJug];
            tuple<vector<int>, int> nextNode (newFilledVolumes, distanceFromStart+1);
            nextNodes.push_back(nextNode);
        }
        for(int secondJug = 0; secondJug < numJugs; secondJug++) {
            if(firstJug == secondJug) continue;
            if(filledVolumes[firstJug] == 0) continue; // Cannot "empty nothing"
            // first > second
            vector<int> newFilledVolumes = filledVolumes;
            if(filledVolumes[firstJug]+filledVolumes[secondJug] > maxVolumes[secondJug]) {
                newFilledVolumes[firstJug] = filledVolumes[firstJug] + filledVolumes[secondJug] - maxVolumes[secondJug];
                newFilledVolumes[secondJug] = maxVolumes[secondJug];
            } else {
                newFilledVolumes[firstJug] = 0;
                newFilledVolumes[secondJug] = filledVolumes[firstJug] + newFilledVolumes[secondJug];
            }
            tuple<vector<int>, int> nextNode (newFilledVolumes, distanceFromStart+1);
            nextNodes.push_back(nextNode);
        }
    }
    return nextNodes;
}

int main() {
    // TODO: Fix; allow inputs
    int numJugs;
    int targetVolume;
    vector<int> maxVolumes = {};

    cin >> numJugs >> targetVolume;
    int volume;
    while(cin >> volume) {
        maxVolumes.push_back(volume);
    }

    // BFS - node is filledVolumes
    queue<tuple<vector<int>,int>> q;

    vector<int> filledVolumes = {0, 0, 0};
    tuple<vector<int>,int> node (filledVolumes, 0); // Distance 0 from start
    q.push(node);

    // auto nextNodes = getNextNodes(filledVolumes, maxVolumes, numJugs, 0);

    // return 0;

    set<vector<int>> seen; // of filledVolumes

    while(!q.empty()) {
        tuple<vector<int>,int> node = q.front();
        filledVolumes = get<0>(node);

        // Check if ended
        for(vector<int>::iterator it = filledVolumes.begin(); it != filledVolumes.end(); it++) {
            int volume = *it;
            if(volume == targetVolume) {
                cout << get<1>(node) << "\n";
                return 0;
            }
        }

        q.pop();

        seen.insert(filledVolumes);
        // Calculate next nodes
        vector<tuple<vector<int>,int>> nextNodes = getNextNodes(filledVolumes, maxVolumes, numJugs, get<1>(node));

        for(vector<tuple<vector<int>,int>>::iterator it = nextNodes.begin(); it != nextNodes.end(); it++) {
            if(seen.count(get<0>(*it)) == 0) {
                q.push(*it);
            }
        }
    }

    cout << "IMPOSSIBLE";
    return 0;
    
    // vector<int> filledVolumes = {0, 0};
    // vector<int> maxVolumes = {3, 5};
    // vector<vector<int>> nextNodes = getNextNodes(filledVolumes, maxVolumes, 2);
    // cout << "len" << nextNodes.size();
    // for(auto i = nextNodes.begin(); i != nextNodes.end(); i++) {
    //     cout << "\n";
    //     for(auto j = i->begin(); j != i->end(); j++) {
    //         cout << *j << " ";
    //     }
    // }
    // return 0;
}