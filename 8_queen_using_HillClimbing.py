
import random

"""function one: the parameter is the current checkerboard layout state,
and the queen logarithm of the current eight queens layout conflicts is judged according to the layout."""
def get_numof_conflict(status):
        num = 0
        for i in range(len(status)):
                for j in range(i + 1,len(status)):
 
                        if status[i] == status[j]:
                                num += 1
                        offset = j - i
                        if abs(status[i]-status[j]) == offset:
                                num += 1
        return num

"""function two: the parameter is the current checkerboard layout state,
using the hill climbing method to select the best layout of the neighbor state and return"""
def  hill_climbing(status):
        convert = {}
        length = len(status)
        for col in range(length):
                best_move = status[col]
                for row in range(length):
                        if status[col] == row:
                                continue
                        status_copy = list(status)
                        status_copy[col] = row
                        convert[(col,row)] = get_numof_conflict(status_copy)
 
        answers = [] # 
        conflict_now = get_numof_conflict(status) #current queen conflict logarithm
 
        # Store all possible successor dictionaries to find the best successor
        for key,value in convert.items():
                if value < conflict_now:
                        conflict_now = value
        for key,value in convert.items():
                if value == conflict_now:
                        answers.append(key)
 
        #If the best successor set element is greater than one randomly select one
        if len(answers) > 0:
                x = random.randint(0,len(answers)-1)
                col = answers[x][0]
                row = answers[x][1]
                status[col] = row
 
        return status
 
"""function three: find a solution that the eight queens satisfy the conflict number of 0,
and loop out the subsequent set of each step until there is no rush > sudden"""
def Queens():
        status = [0,1,2,3,4,5,6,7] # initial state, all queens are on the diagonal
 
        """When the number of conflicts is greater than 0,
        the loop solves the best successor until the eight queens solution is found."""
        while get_numof_conflict(status) > 0:
                status = hill_climbing(status)
                print("\n",status)
                print(get_numof_conflict(status))
        print("\n","the answer is")
        print(status)
 
if __name__ == '__main__':
        Queens()
