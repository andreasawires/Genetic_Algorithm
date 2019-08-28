# Genetic Algorithm for Reinforcement Learning
This algorithm is based on Darwin Evolution Theory.  
We set a target that we want the algorithm reaches  
At the Beginnig the algorithm create a compleatly random population, by default 200, based on what genes it has, in this case letters and symbols.  
From the this first population it calculates the fitness for each componet of the population.  
The fitness function simply calculates how similar is that component to the target.  
Then it picks the components with the highest fitness score and then using those components apply the crossover function which create another population with a major fitness.  
For each population it counts a generation and at the end we'll get the number of generations and the time spent to find the target  
## How to run it
* First of all check if you have python >=3.6.0
* Clone or download this repo or simply copy the code
* Set the target and then run it.  

>Make sure you use symbols present in the variable **genes**, if not just add it.  Remember more genes it has and more time and generations it will take to get to the target.