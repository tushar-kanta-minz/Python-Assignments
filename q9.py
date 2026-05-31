detections = [
    {"object": "box", "confidence": 78, "mode": "infrared", "distance": 2.5},
    {"object": "human", "confidence": 95, "mode": "camera", "distance": 1.2},
    {"object": "ball", "confidence": 82, "mode": "ultrasonic", "distance": 3.0},
    {"object": "human", "confidence": 88, "mode": "camera", "distance": 0.8},
    {"object": "chair", "confidence": 70, "mode": "infrared", "distance": 2.8}
]

valid_humans = list(filter(lambda x: x['object']=="human" and x['mode']=="camera" and x['confidence'] > 85 , detections))
print("Valid Humans",valid_humans)

distance_humans = list(map(lambda x:x['distance'], valid_humans))
print("Distances",distance_humans)

def alert(distance):
    if distance < 1:
        return "ALERT: Human Very Close!!"
    return "Humans detected at safe Distance"
    
for d in distance_humans:
    print(alert(d))