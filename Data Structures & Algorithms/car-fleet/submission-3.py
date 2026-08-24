class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # pair each position w its speed in tuples
        pair_list = []
        for i in range(len(position)):
            pair_list.append((position[i], speed[i]))
        
        # sort by descending order

        pair_list.sort(reverse=True)


        stack = deque()
        for pos, speed in pair_list:
            time = (target - pos)/speed
            # if stack is empty, initiate stack with the first element
            if len(stack) == 0:
                stack.append([time])
            # otherwise, check its current time. if the time of this car is less or equal than the time in the stop of the stack, that car is apart of that fleet
            else:
                if time <= stack[-1][0]:
                    stack[-1].append(time)
                else:
                    stack.append([time])
        
        return len(stack)




            
    
