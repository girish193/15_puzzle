# 15_puzzle
15 puzzle problem solved with bruteforce Breadth First Search(BFS)

## Description
This code aims at solving 15 puzzle problem with BFS. All the nodes corresponding with different positions of the blank tile are explored until a goal is found.

## Dependencies
* python -version 3
* Numpy
* copy
* time

## Function Descriptions 
### Array to String: 
In this functiom array value is converted into string. Flatten() function is used to convert 2D array to 1 D array. String is generated by appending ‘|’ and concatenating array elements. 
### String to Array
In this function string value is converted into Array.Here string.split() function is used to extract array element value.Every element of the list is converted into integer and stored. The resultant array is then reshaped into 4X4 array. 
### Blank_Tile_swapping: 
In this function blank tile position is calculated by using np.where function. Depending on the blanktile position the possibility for top,left,bottom,right options is determined .The swap operations are performed and the new values are stored in a new array and later converted to a string and returned. 
### Swapping Comparision: 
In this function the values returned from blank_tile_swapping function are stored in a list. If the values are empty, they are removed. For each value stored in the search_value list, it is compared with the existing elements in the string database. If the element already exists the value is not added, otherwise it is added in breadth first manner (BFS)which in turn is accomplished by using the key of the last element incremented by 1 as the new key. This way the node numbers are added in BFS manner with their values. Following this the node_states dictionary is returned. 

### Main(): 
In this function the root node is called as initial_state. The node_states dictionary is updated with root node and key as node number, here it is 1. Following this the tree generation function is called to generate the tree elements until the goal state is reached. 


## Run Code
Open the file "4x4 puzzle with tracking.py" in an IDE (Spyder, VS Code etc) of your choice. All the test cases are given 
as input and solutions are found in the same python file. Further "nodePath_{*}.txt" files are generated which contains 
the solution strategy for a given initial and goal states.


 
