import json
import time

#median of median for unsorted list
    
#calcuting the execution time of the algorithm using time method
start_time = time.perf_counter()

#open data saved in json file
with open('generate_test_data.json', 'r') as file:
    houses_data = json.load(file)

#extract data
distances = [house["distance_km"] for house in houses_data]


#define median of median function with array and k smallest element

def median_of_medians(arr, k):
    if len(arr) < 10:   #check if length array is less than 10 recurrsively stops the function
        return sorted(arr)[k]   #sort the array 
    
    #divide array into sub-arrays
    sublists_arr = [arr[i:i + 5] for i in range(0, len(arr), 5)]  #divide into 5 sub-arrays
    medians = [sorted(sublist)[len(sublist) // 2] for sublist in sublists_arr]  #sort and find median in each sub-array

    #find median of medians 
    pivot = median_of_medians(medians, len(medians) // 2)

    # Partitioning
    low = [x for x in arr if x < pivot]  #if x less than pivot placed to low partition
    high = [x for x in arr if x > pivot]  #if x greater than pivot placed to high partition
    k_element = len(low)   #place kth smallest element to low partition
 
    #check if k is less than k_element
    if k < k_element:
        return median_of_medians(low, k)  
    elif k > k_element:
        return median_of_medians(high, k - k_element - 1)
    else:
        return pivot
    
k = int(input("Enter the k value: ")) - 1   #user inputs kth element 

kth_distance = median_of_medians(distances, k)  #median function takes distance and k element

# Find the corresponding house
matching_houses = [house for house in houses_data if house["distance_km"] == kth_distance]

#check the house match the kth element
if matching_houses:
    house = matching_houses[0]
    print(f"Your {k + 1}th nearest house is {house['neighbor_names']}."
          f"Her house is {house['distance_km']} km away from your house.")
else:
    print("No house neighbour found")



end_time = time.perf_counter()
print(f'Algorithm execution time {end_time - start_time:.3f} seconds')