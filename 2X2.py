#!/usr/bin/env python
# coding: utf-8

# In[5]:
import numpy as np 
import copy 
import math 

def Array_to_String(current_node): 
    string = ""
    flattened_node= current_node.flatten()
    for i in range(len(flattened_node)): 
        string += str(flattened_node[i]) + "|"
    return string

def String_to_Array(string): 
    new_list = string.split("|")[:-1]
    for i in range(len(new_list)):
        new_list[i]=int(new_list[i])
    array = np.array(new_list).reshape(2,2) # this will be a 2X2 array!
    return array 
    
def blank_tile_swapping(current_node): 
    blank_tile = np.where(current_node == 0) # returns 2-D tuple
    m,n =  blank_tile[0][0], blank_tile[1][0]
      
    top = False
    bottom = False 
    right = False
    left = False

    if(m==1): 
        top = True
    if(m ==0 ): 
        bottom = True
    if(n ==1): 
        left = True
    if (n ==0): 
        right = True
    
    top_node_info = "" 
    bottom_node_info = ""
    left_node_info = ""
    right_node_info = ""
    
    if(top == True): 
        new_node_top = copy.copy(current_node)
        new_node_top[m][n],new_node_top[m-1][n] = new_node_top[m-1][n],new_node_top[m][n]
        top_node_info = Array_to_String(new_node_top)
    
    if(bottom == True): 
        new_node_bottom = copy.copy(current_node)
        new_node_bottom[m][n],new_node_bottom[m+1][n] = new_node_bottom[m+1][n],new_node_bottom[m][n]
        bottom_node_info = Array_to_String(new_node_bottom)
    
    if(left == True): 
        new_node_left = copy.copy(current_node)
        new_node_left[m][n],new_node_left[m][n-1] = new_node_left[m][n-1],new_node_left[m][n]
        left_node_info = Array_to_String(new_node_left)

    if(right == True): 
        new_node_right = copy.copy(current_node)
        new_node_right[m][n],new_node_right[m][n+1] = new_node_right[m][n+1],new_node_right[m][n]
        right_node_info = Array_to_String(new_node_right)
          
    return top_node_info, bottom_node_info, left_node_info, right_node_info

def swapping_comparision(current_node, node_states):
    top_node_info, bottom_node_info, left_node_info, right_node_info = blank_tile_swapping(current_node)
    
    search_value_old = [top_node_info, bottom_node_info, right_node_info, left_node_info]
    search_value = []
#     print(search_value_old)
    for i in search_value_old: 
#         print(i) 
        if (i != ""):
            search_value.append(i)
#             print(search_value)
    
    
#     print('Node_states: {}\n'.format(node_states))
#     print('Search_Value: {}\n'.format(search_value))

#     iteration = 0
    for value in search_value:
            
        last_key = list(node_states.keys())[-1] + 1
        string_database = list(node_states.values())
#         print("===== Start of Iteration: {} =====\n".format(iteration))

        if(all(string != value for string in string_database)):
#             print('{} is not present in Test_Dict\n'.format(value))
            node_states.update({last_key:value})
#             print("Updated Test_Dict: {}\n".format(node_states))
#         else:
#             print('{} is present in Test_Dict\n'.format(value))
#             print("Updated Test_Dict: {}\n".format(node_states))

#         print("===== End of Iteration: {} =====\n".format(iteration))
#         iteration += 1
        
    return node_states

def tree_generation(node_states, current_node):
    node_states = swapping_comparision(current_node, node_states)
    return node_states
  

if __name__ == "__main__":

    initial_state = np.array([[1,2],
                              [3,0]])

    goal_state = np.array([[2,0],
                           [1,3]])
    node_states = {}
    initial_node_info = Array_to_String(initial_state)
    node_states.update({1: initial_node_info})

    goal_node_info = Array_to_String(goal_state)

    for node_index in range(0,4):


    #         if (list(node_states.values())[node_index] == goal_node_info):
    #             print("\nGoal State reached (check node {})".format(node_index+1))
    #             break

        current_node = String_to_Array(list(node_states.values())[node_index])
        if ((current_node == goal_state).all()):
            print("\nGoal State reached (check node {})".format(node_index+1))
            break 


        else:     
            node_states = tree_generation(node_states, current_node)
            print("\n\nIteration Number: {}".format(node_index))
            print(node_states)
            f = open('./nodePath.txt','ab')
            np.savetxt(f,current_node,delimiter=' ',fmt='%d')
            f.write(b"\n")
            f.close()
