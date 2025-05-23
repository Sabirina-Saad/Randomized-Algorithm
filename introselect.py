import json
import time

from quickselect import quickselect
from median_of_medians import median_of_medians

#introselect for unsorted list
    
#calcuting the execution time of the algorithm using time method
start_time = time.perf_counter()

#open data saved in json file
with open('generate_test_data.json', 'r') as file:
    houses_data = json.load(file)

#extract data 
distances = [house["distance_km"] for house in houses_data]

def introselect(arr, k, max_depth=None):
    if max_depth is None:
        max_depth = 2 * int(len(arr) ** 0.5)
    if len(arr) <= 5 or max_depth == 0:
        return median_of_medians(arr,k)
    try:
        return quickselect(arr, k)
    except RecursionError:
        return median_of_medians(arr, k)

k = int(input("Enter the k value: ")) - 1   #user inputs kth element 

kth_distance = introselect(distances, k)  #introselect function takes distance and k element

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