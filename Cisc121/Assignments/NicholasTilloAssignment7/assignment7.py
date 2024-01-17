# Name:   <Nicholas Tillo>
# Student Number: <20291255>
# Email:  <20njt4@queensu.ca>

# I confirm that this assignment solution is my own work and conforms to 
# Queen's standards of Academic Integrity

import numpy as np
import random



def find_values(line):
    ''' Turns the information from the file into a list of [name, qualities*] '''
    final_list = line.replace("\n", "").split(" ")
    return final_list

#The file downloaded from the site. 
name = "Assignments/NicholasTilloAssignment7/text.txt"

#From a file path, extracts all the text and turns it into a 2d array. 
def create_array(file_path):
    file = open(file_path, "r" , encoding= "utf8")
    couner = 0
    arra = np.empty([1,16])
    for line in file:
        values = find_values(line)
        arra = np.append(arra, [values], axis = 0)
    arra = np.delete(arra, 0,0)
    #print(arra.size)
    #print(len(arra))
    return arra



def random_row(array):
    return random.randrange(1, len(array) - 1)

def chose_random_rows(num, array):
    chosen_list = []
    for num in range(num):
        chosen_list.append(array[random_row(array)])
    return chosen_list

def k_means_clustering(num_of_groups, array, chosen_list):
    '''Inputs a number of groups wanted, an array and a list of chosen values. It finds the closest points to the chosen ones. 
    using the menhatten metric. Then creating a new set of chosen values to create more accurate clusters. 

    '''
    distances = []
    cluster_dict = {}
    for value in range(len(chosen_list)):
        cluster_dict[value] = []
    first = True
    for row in array:
        if first:
            first = False
            continue
        shortest_distance = manhatten_metric(row, chosen_list[0])
        shortest_name = chosen_list[0][0]
        counter = 0
        finalpos = 0
        for chosen_point in chosen_list[1:]:
            value = manhatten_metric(row, chosen_point)
            counter += 1
            if  value < shortest_distance:
                shortest_distance = value
                shortest_name = chosen_point[0]
                finalpos = counter
            
        distances.append(shortest_name)
        cluster_dict[finalpos].append(list(row))
    print((distances))
    return create_new_values(cluster_dict, num_of_groups)
        
    
    
    #print(distances)    
    #print(cluster_dict)




def manhatten_metric(row1, row2):
    '''Inputs two rows of the array, then finds the "distance" between them, the amount of diffrent numbers there are.'''
    totaldistance = 0

    for num in range(len(row1)):
        try: 
            totaldistance += abs(int(row1[num]) - int(row2[num]))
        except:
            continue
    return totaldistance


animal_array = create_array(name)

#print(array22)

def create_new_values(clustered_dict, num_of_cluster):
    final_points = []
    #For each cluster, For each animal within each cluster, for each value within each animal. 
    for values in range(num_of_cluster):
        new_point= ["Cluster#" +str(values)]
        for object in clustered_dict[values]:
            for num in range(1, len(object)):
                #Add up all the values in the list to make a new list. If its the last object in the cluster,divides it to get the average
                
                if object[0] == clustered_dict[values][0][0]:
                    #If it is the first row in the cluster, then creates a base list by appending. 
                    new_point.append(int(object[num]))
                else:
                    new_point[num] += int(object[num])
                    if object[0] == clustered_dict[values][-1][0]:
                        
                        new_point[num] = new_point[num]/ len(clustered_dict[values])
        final_points.append(new_point)                
        
    print(final_points)
    return final_points
                

def k_means_helper(desired_clusters, array, num): 
    ''' Helper function to call the k_means_clustering multiple times. '''
    cluster_list = chose_random_rows(desired_clusters, array)
    for value in range(num):
        cluster_list = k_means_clustering(desired_clusters,array , cluster_list)
    print(cluster_list)


k_means_helper(7, animal_array, 0)

