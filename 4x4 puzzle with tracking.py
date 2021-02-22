#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import copy 
import time

def puzzle_solution(initial_state, goal_state, test_case):
    
    start = time.time()

    def Array_to_String(current_node): 
        
        """
        
        Takes an Array representation and returns a String representation (colum major order).
        
        Parameters
        ----------
        current_node : 4 X 4 numpy array.
        
        Returns
        -------
        string : string representation of the given 4 X 4 array in column major order.
        
        """
        
        string = ""
        flattened_node= current_node.flatten(order = 'F') # for column major 
        for i in range(len(flattened_node)): 
            string += str(flattened_node[i]) + " "
        return string

    def String_to_Array(string): 
        
        """
        
        Takes a String representation and returns an Array representation (colum major order).
        
        Parameters
        ----------
        string : string representation of a node state.
        
        Returns
        -------
        array : Array representation of the given node state.
        
        """
            
        new_list = string.split(" ")[:-1]
        for i in range(len(new_list)):
            new_list[i]=int(new_list[i])
        array = np.array(new_list).reshape(4,4, order = 'F') # this will be a 4X4 array in column major
        return array 

    def blank_tile_swapping(current_node): 
        
        """
        
        For a given node state, it first finds the position of the blank tile. Subsequently, it identifies 
        different possible swapping operations (i.e., top/ bottom/ right/ left). Finally, it swaps and returns 
        the new node state string representations.
        
        Note: Here, in this function, duplicacy of node generated is not checked !
                
        Parameters
        ----------
        current_node : 4 X 4 numpy array.
        
        Returns
        -------
        top_node_info    : String representation of the new generated node after top swapping operation.
        bottom_node_info : String representation of the new generated node after bottom swapping operation.
        right_node_info  : String representation of the new generated node after right swapping operation.
        left_node_info   : String representation of the new generated node after left swapping operation.
        
        Note: If a swapping operation is not possible then it returns an empty string!
        
        """
            
        blank_tile = np.where(current_node == 0) # returns 2-D tuple
        m,n =  blank_tile[0][0], blank_tile[1][0]

        top = False
        bottom = False 
        right = False
        left = False

        if(m != 0): 
            top = True
        if(m != current_node.shape[0] -1): 
            bottom = True
        if(n != current_node.shape[1] -1): 
            right = True
        if(n != 0): 
            left = True

        top_node_info = "" 
        bottom_node_info = ""
        right_node_info = ""
        left_node_info = ""

        if(top == True): 
            new_node_top = copy.copy(current_node)
            new_node_top[m][n],new_node_top[m-1][n] = new_node_top[m-1][n],new_node_top[m][n]
            top_node_info = Array_to_String(new_node_top)

        if(bottom == True): 
            new_node_bottom = copy.copy(current_node)
            new_node_bottom[m][n],new_node_bottom[m+1][n] = new_node_bottom[m+1][n],new_node_bottom[m][n]
            bottom_node_info = Array_to_String(new_node_bottom)

        if(right == True): 
            new_node_right = copy.copy(current_node)
            new_node_right[m][n],new_node_right[m][n+1] = new_node_right[m][n+1],new_node_right[m][n]
            right_node_info = Array_to_String(new_node_right)
            
        if(left == True): 
            new_node_left = copy.copy(current_node)
            new_node_left[m][n],new_node_left[m][n-1] = new_node_left[m][n-1],new_node_left[m][n]
            left_node_info = Array_to_String(new_node_left)

        return top_node_info, bottom_node_info, right_node_info, left_node_info

    def swapping_comparison(node_states, current_node, track, node_index):
        
        """
        
        In this function, new child nodes are generated for a given parent node and later added to the tree.
        
        Note: Here, duplicacy of node generated is checked and only then added !
                
        Parameters
        ----------
        node_states  : dictionary type with key as node state number (starting from 1) and values as corresponding strings.
        current_node : 4 X 4 numpy array.
        track        : list type and contains path of each node generated.
        node_index   : int type and accounts for current node number.
        
        Returns
        -------
        node_states  : updated dictionary with new child nodes.
        track        : updated list with path of new child nodes. 
        
        """
            
        top_node_info, bottom_node_info, right_node_info, left_node_info = blank_tile_swapping(current_node)

        search_value_old = [top_node_info, bottom_node_info, right_node_info, left_node_info]
        search_value = []

        for i in search_value_old: 
            if (i != ""):
                search_value.append(i)

        parent_track = track[node_index -1] # this will return track of current(parent) node which will be a string

        child_key = list(node_states.keys())[-1] + 1

        for value in search_value:

            string_database = list(node_states.values())

            if(all(string != value for string in string_database)):
                node_states.update({child_key:value})
                child_track = ''
                child_track = parent_track + ' -> ' + str(child_key) 
                track.append(child_track)
                child_key += + 1

        return node_states, track

    def tree_generation(node_states, current_node, track, node_index):
        
        """
        
        Tree is generated by calling swapping_comparison function.
        
        Parameters
        ----------
        node_states  : dictionary type with key as node state number (starting from 1) and values as corresponding strings.
        current_node : 4 X 4 numpy array.
        track        : list type and contains path of each node generated.
        node_index   : int type and accounts for current node number.
        
        Returns
        -------
        node_states  : updated dictionary with new child nodes.
        track        : updated list with path of new child nodes. 
        
        """
        
        node_states, track = swapping_comparison(node_states, current_node, track, node_index)
        return node_states, track

    initial_node_info = Array_to_String(initial_state)
    goal_node_info = Array_to_String(goal_state)

    node_states = {}
    node_states.update({1: initial_node_info})

    track= []
    track.append('1')

    current_node = initial_state       
    node_index = 1

    while (node_states[node_index] != goal_node_info):

        node_states, track = tree_generation(node_states, current_node, track, node_index)
        current_node = String_to_Array(node_states[node_index+1])    
        node_index += 1
    
    end = time.time()
    
    time_taken = (end - start)*1000 # in milli seconds
    
    solution_path = track[node_index -1]
        
    print('\n\n----------------------- For TEST CASE = {} -----------------------'.format(test_case))
    print('\nGoal State reached at node {1} !!!'.format(test_case,node_index))
    print('\nRequired Solution trajectory:\t', solution_path)
    print('\nTime taken to solve:\t{0:1.3f} ms'.format(time_taken))
    
    ### Writing the solution trajectory to an Output File
    
    fname = './nodePath_' + str(test_case) + '.txt'
    myfile = open(fname,"w")
       
    myfile.write('Goal State reached at node {} !!!'.format(node_index))
    myfile.write('\nRequired Solution trajectory:\t {}\n'.format(solution_path))
    myfile.write('\nTime taken to solve:\t{0:1.3f} ms'.format(time_taken))
    solution_path = solution_path.split(' -> ')
    
    count = 1
    for node in solution_path:
        
        myfile.write('\n\n{0}) Node State: {1}'.format(count, int(node)))
        required_string = node_states[int(node)]
        myfile.write('\n\tString Representation: \t{0}'.format(required_string))
        required_array = String_to_Array(required_string)
        myfile.write('\n\tArray Representation:  \n{0}'.format(required_array))
        count += 1

    myfile.close()
    
    return


############ Goal State (kept fixed for all the below test cases) ############

goal_state = np.array([[1, 2, 3, 4],
                       [5, 6, 7, 8],
                       [9, 10, 11, 12],
                       [13, 14, 15, 0]])

############ For test case 1 ############

initial_state_1 = np.array([[1, 2, 3, 4],
                            [5, 6, 0, 8],
                            [9, 10, 7, 12],
                            [13, 14, 11, 15]])

puzzle_solution(initial_state_1, goal_state, 1) # solving for test case 1

############ For test case 2 ############

initial_state_2 = np.array([[1, 0, 3, 4],
                            [5, 2, 7, 8],
                            [9, 6, 10, 11],
                            [13, 14, 15, 12]])

puzzle_solution(initial_state_2, goal_state, 2) # solving for test case 2

############ For test case 3 ############

initial_state_3 = np.array([[0, 2, 3, 4],
                            [1, 5, 7, 8],
                            [9, 6, 11, 12],
                            [13, 10, 14, 15]])

puzzle_solution(initial_state_3, goal_state, 3) # solving for test case 3

############ For test case 4 ############

initial_state_4 = np.array([[5, 1, 2, 3],
                            [0, 6, 7, 4],
                            [9, 10, 11, 8],
                            [13, 14, 15, 12]])

puzzle_solution(initial_state_4, goal_state, 4) # solving for test case 4

############ For test case 5 ############

initial_state_5 = np.array([[1, 6, 2, 3],
                            [9, 5, 7, 4],
                            [0, 10, 11, 8],
                            [13, 14, 15, 12]])

puzzle_solution(initial_state_5, goal_state, 5) # solving for test case 5

