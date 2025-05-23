import json
import time
import random

#quickselect for unsorted list
    
#calcuting the execution time of the algorithm using time method
start_time = time.perf_counter()


#open data saved in json file
with open('generate_test_data.json', 'r') as file:
    houses_data = json.load(file)

#extract data
distances = [house["distance_km"] for house in houses_data]

#quickselect algorithm
def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]
    
    pivot_dist = random.choice(arr)
    lows = [x for x in arr if x < pivot_dist]
    highs = [x for x in arr if x > pivot_dist]
    pivots = [x for x in arr if x == pivot_dist]
    
    if k < len(lows):
        return quickselect(lows, k)
    elif k > len(lows) + len(pivots):
        return quickselect(highs, k - len(lows) - len(pivots))
    else:
        return pivots[0]
    

#input
k = int(input("Enter the k value: ")) - 1   #user inputs kth element 

kth_distance = quickselect(distances, k-1)  #quickselect function takes distance and k element

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