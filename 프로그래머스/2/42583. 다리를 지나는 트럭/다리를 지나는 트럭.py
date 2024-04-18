from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    current_weight = 0
    
    on_bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    
    while len(truck_weights) != 0:
        time += 1
        current_weight -= on_bridge.popleft()

        if current_weight + truck_weights[0] <= weight:
            current_weight += truck_weights[0]
            on_bridge.append(truck_weights.popleft())
        else:
            on_bridge.append(0)
            
    time += bridge_length

    return time