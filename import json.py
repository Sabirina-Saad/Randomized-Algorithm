import json
import random

# intialize variables for house number, neighbors names and distance

house_no = 100

neighbor_names = ['Hani','khadijah', 'Ali', 'Ahmed','Hasan','zeinab','Farah','Khairul','Amir','Dina',
   'khalid', "Sara", "David", "Fatimah", "John", "Aminah", "James", "Nur", "Liam", "Sophia",
    "Adam", "Zara", "Omar", "Layla", "Musa", "Hana", "Isa", "Maryam", "Daniel", "Aisha",
    "Noah", "Emma", "Ethan", "Olivia", "Lucas", "Mia", "Mason", "Isabella", "Logan", "Amelia",
    "Jacob", "Emily", "Michael", "Charlotte", "Alexander", "Abigail", "Benjamin", "Harper",
    "Elijah", "Evelyn", "William", "Ella", "Jameson", "Sofia", "Sebastian", "Madison", "Jack",
    "Scarlett", "Henry", "Victoria", "Owen", "Aria", "Gabriel", "Grace", "Samuel", "Chloe",
    "Matthew", "Camila", "Joseph", "Penelope", "David", "Riley", "Carter", "Layla", "Wyatt",
    "Lillian", "Johnathan", "Nora", "Luke", "Zoey", "Isaac", "Mila", "Jayden", "Avery",
    "Dylan", "Ella", "Grayson", "Luna", "Levi", "Hannah", "Nathan", "Addison", "Caleb",
    "Eleanor"] #100 names

house_distances = [round(x * 0.1, 1) for x in range(1, 101)]  #rounds distance to 1 decimal 
distances = random.sample(house_distances, house_no)

# create test data 
generate_data =  [
    { "neighbor_names": random.choice(neighbor_names),
      "distance_km": distances[i]
      } 
    for i in range(house_no)  
]

# Save test data as JSON 
with open("generate_test_data.json", "w") as f:
    json.dump(generate_data, f, indent=3)

print('test data created')