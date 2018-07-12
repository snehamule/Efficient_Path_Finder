'''
Created on Apr 24, 2017

@author: Sneha Mule
'''
import environment    
import state

class Search:    
    def __init__(self,initial_state,env):
        self.env=env
        self.initial_state=initial_state
      
    def heuristic(self,xCurr,yCurr,envirornment):
        tempValue=abs(envirornment.end_x - xCurr) + abs(envirornment.end_y-yCurr)
        heuristic=tempValue+abs(envirornment.elevations[envirornment.end_x][envirornment.end_y] - envirornment.elevations[xCurr][yCurr])
        return heuristic


    def getCost(self,xOld,yOld,xNew,yNew,envirornment):
        oldElevationCost = envirornment.elevations[yOld][xOld]
        newElevationCost=   envirornment.elevations[yNew][xNew]
        if (newElevationCost > oldElevationCost):
            cost=1+((newElevationCost - oldElevationCost) * (newElevationCost - oldElevationCost))
            return cost
        
        elif (newElevationCost < oldElevationCost):
            cost=1 + (oldElevationCost - newElevationCost)
            return cost
            
        else:
            return 1


    def calculateTotalCost(self,xOld,yOld,xNew,yNew,envirornment):
        #Confirm xCUrrent means xNew
        totalCost =self.getCost(xOld, yOld,xNew, yNew, envirornment) + 	  self.heuristic(xNew, yNew, envirornment)
        return totalCost
     
    def isNotVisited(self,x,y,visited):
        for i in visited:
            if((str(x)+str(y))==i):
                return False  
        return True

    def moveN(self,y):
        y+=1
        return  ++y   
            
    def moveE(self,x):
        x+=1
        return ++x
    
    def moveS(self,y):
        y-=1
        return --y   
    
    def moveW(self,x): 
        x-=1
        return --x
             
    def search(self):
        visited=[]
        totalCostDictionary={}
        index=0
        frontier=[self.initial_state] 
        currentNode=frontier.pop(index)
        while (frontier):
            x = currentNode.current_x
            y = currentNode.current_y
            #visited
            if(not(x == self.env.end_x and y==self.env.end_y)):    
                #For First Iteration  
                if(x == currentNode.current_x and y == currentNode.current_y):
                    visited.append(str(currentNode.current_x)+str(currentNode.current_y))
    
                #Agent Move to the North Direction
                if(y!= self.env.end_y and self.isNotVisited(x, self.moveN(y),visited)):
                    cost=self.getCost(x,y,x, self.moveN(y),self.env) 
                    print ('cost North',cost)
                    if (self.env.energy_budget > cost):
                        totalCost = self.calculateTotalCost(x,y,x,self.moveN(y), self.env)
                        self.initial_state.moves_so_far = str(currentNode.moves_so_far)+'N'
                        self.initial_state.cost_so_far = currentNode.cost_so_far + cost
                        self.initial_state.current_x = x
                        self.initial_state.current_y = self.moveN(y)
                        self.initial_state.currentPosition=str(x)+str(self.moveN(y))
                        frontier.append(self.initial_state)
                        totalCostDictionary[str(x)+str(self.moveN(y))] = totalCost
                        print('totalCostDictionary N',totalCostDictionary)
                
                
                #Agent Move to the East Direction
                if(x != self.env.end_x and self.isNotVisited(self.moveE(x), y,visited)):
                    cost=self.getCost(x,y,self.moveE(x),y,self.env) 
                    if (self.env.energy_budget > cost):
                        totalCost=self.calculateTotalCost(x,y,self.moveE(x),y,self.env)
                        self.initial_state.moves_so_far=str(currentNode.moves_so_far)+'E'
                        self.initial_state.cost_so_far=currentNode.cost_so_far + cost
                        self.initial_state.current_x = self.moveE(x)
                        self.initial_state.current_y = y
                        self.initial_state.currentPosition= str(self.moveE(x))+str(y)
                        frontier.append(self.initial_state)
                        totalCostDictionary[str(self.moveE(x))+str(y)] = totalCost
                        print('totalCostDictionary E',totalCostDictionary)
                
                #Agent Move to the South Direction
                if(y != 0 and self.isNotVisited(x, self.moveS(y),visited)) :
                    cost=self.getCost(x, y,x,self.moveS(y), self.env) 
                    if (self.env.energy_budget > cost):
                        totalCost = self.calculateTotalCost(x,y,x,self.moveS(y),self.env)
                        self.initial_state.moves_so_far = str(currentNode.moves_so_far)+'S'
                        self.initial_state.cost_so_far = currentNode.cost_so_far + cost
                        self.initial_state.current_x = x
                        self.initial_state.current_y = self.moveS(y)
                        self.initial_state.currentPosition=str(x)+str(self.moveS(y))
                        frontier.append(self.initial_state)
                        totalCostDictionary[str(x) + str(self.moveS(y))] = totalCost
                        print('totalCostDictionary S',totalCostDictionary)
                
                #Agent Move to the West Direction
                if(x != 0 and self.isNotVisited(self.moveW(x), y,visited)):
                    cost=self.getCost(x, y,self.moveW(x),y, self.env) 
                    if (self.env.energy_budget > cost):
                        totalCost=self.calculateTotalCost(x,y,self.moveW(x),y,self.env)
                        self.initial_state.moves_so_far = str(currentNode.moves_so_far) + 'W'
                        self.initial_state.cost_so_far = currentNode.cost_so_far + cost
                        self.initial_state.current_x = self.moveW(x)
                        self.initial_state.current_y = y
                        self.initial_state.currentPosition = str(self.moveW(x))+str(y)
                        frontier.append(self.initial_state)
                        totalCostDictionary[str(self.moveW(x))+str(y)] = totalCost
                        print('totalCostDictionary W',totalCostDictionary)
                        
                #Getting Minimum A* value from the Frontier 
                minValue=min(totalCostDictionary.values())
                print('Min value',minValue)
                minValuePath = (totalCostDictionary.keys()[(totalCostDictionary.values().index(minValue))])
                print('minValuePath',minValuePath)
                closedList=[]
               
                #print(frontier[1].currentPosition)
                for x in range (len(frontier)):
                    print('x.currentPosition',frontier[x].currentPosition)
                    if(frontier[x].currentPosition == minValuePath):
                        index = x
                        
                print("index",index)
                
                #Adding state into Closed List array
                closedList.append(frontier[index])   
                
                # Remove minimum value from Frontier and it's cost from total cost dictionary
                del totalCostDictionary[minValuePath]
            else:    
                openListState = state.State(frontier[-1].current_x,frontier[-1].current_y)
                openListState.currentPosition=frontier[-1].currentPosition
                    
                openListState.moves_so_far=frontier[-1].moves_so_far
                openListState.cost_so_far=frontier[-1].cost_so_far
                openlist=[openListState]
                    
                 
                #Add  Last value to the Solution
                solution=state.State(frontier[-1].current_x,frontier[-1].current_y)
                solution.moves_so_far=frontier[-1].moves_so_far
                solution.cost_so_far=frontier[-1].cost_so_far
                return solution,openlist,closedList        
                
                
     
        
                
                
        
        

        
