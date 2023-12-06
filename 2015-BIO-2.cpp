#include <bits/stdc++.h>
using namespace std;
// Battleships
// 2023-12-06 Marking (1 right, 0 wrong, * bug):
// 1110001000001110 12/27
// Took 00h41m34s for pt a

// EBI: Still a bug here?

// web search means used web to help

const int BOARD_SIZE = 10;
const int BOARD_SIZE_SQUARED = 100;
const int NUM_SHIPS = 10;
const int SHIP_SIZES[] = {4,3,3,2,2,2,1,1,1,1};
// const int NUM_SHIPS = 1;
// const int SHIP_SIZES[] = {2};

class Board {
    private:
        bitset<BOARD_SIZE_SQUARED> board;
        bool get(int x, int y) {
            if(x < 0 || x >= BOARD_SIZE) return false; // out-of-bounds
            if(y < 0 || y >= BOARD_SIZE) return false; // out-of-bounds
            return this->board[y*BOARD_SIZE+x];
        }
        void set(int x, int y, bool isShip) {
            this->board[y*BOARD_SIZE+x] = isShip;
        }
        bool canPlaceShip(int x, int y, int shipSize, bool horizontal) { // else vertical
            if(horizontal && x+shipSize <= BOARD_SIZE) {
                // horizontal; in bounds of board horizontally
                if (this->get(x-1, y)) return false;
                if (this->get(x+shipSize, y)) return false;
                for(int checkX = x-1; checkX <= x+shipSize; checkX++) {
                    if (this->get(checkX, y-1)) return false;
                    if (this->get(checkX, y+1)) return false;
                }
            } else if(y+shipSize <= BOARD_SIZE) {
                // vertical; in bounds of board horizontally
                if (this->get(x, y-1)) return false;
                if (this->get(x, y+shipSize)) return false;
                for(int checkY = y-1; checkY <= y+shipSize; checkY++) {
                    if (this->get(x-1, checkY)) return false;
                    if (this->get(x+1, checkY)) return false;
                }
            } else {
                // out of bounds of board
                return false;
            }
            // No adjacent ships
            return true;
        }
    public:
        /**
         * Return whether the ship has been placed legally, not placing it if illegal.
        */
        bool shipPlaced(int x, int y, int shipSize, bool horizontal) {
            if(this->canPlaceShip(x, y, shipSize, horizontal)) {
                if(horizontal) {
                    for(int placeX = x; placeX < x+shipSize; placeX++) {
                        this->set(placeX, y, true);
                    }
                } else {
                    for(int placeY = y; placeY < y+shipSize; placeY++) {
                        this->set(x, placeY, true);
                    }
                }
                return true;
            } else {
                return false;
            }
        }

        Board() { // web search
            for(int i = 0; i < BOARD_SIZE_SQUARED; i++) {
                this->board[i] = false;
            }
            this->set(3, 0, true);
        }

        // DEBUG
        void print() {
            cout << "\n";
            for(int y = BOARD_SIZE; y >= 0; y--) {
                for(int x = 0; x < BOARD_SIZE; x++) {
                    if(get(x, y)) {
                        cout << "#";
                    } else {
                        cout << "-";
                    }
                }
                cout << "\n";
            }
            cout << "\n";
        }
};

int main() {
    // Vars
    int a;
    int c;
    int m;
    int r = 0;
    Board board; // web search
    
    // Input
    cin >> a >> c >> m;

    // Main program
    int i = 0; // of ships with sizes [4,3,3,2,2,2,1,1,1,1] = 10 ships
    while(i < NUM_SHIPS) {
        // 1.
        r = (a * r + c) % m; 
        // 2.
        int x = r % 10;
        int y = (r / 10) % 10;
        // 3.
        r = (a * r + c) % m;
        bool horizontal = (r % 2 == 0);
        board.print();
        // 4.
        if(board.shipPlaced(x, y, SHIP_SIZES[i], horizontal)) {
            // 5.
            cout << x << " " << y << " " << (horizontal ? "H" : "V") << "\n";
            i++; // Next ship
        }
        // board.print();
    }

    return 0;
}