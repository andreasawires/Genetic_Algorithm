import datetime
start = datetime.datetime.now()
import random

def genetic(target, size_population=200, mutation=0.01):
    
    # fitness function
    def fitness(element):
        score = 0.0
        for i in range(len(element)):
            if element[i] == target[i]:
                score += 1
        fitness = score/len(target)
        return fitness ** 2
    
    # all the genes
    genes = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZàèéìòù !?1234567890,."
    population = []

    # generate the first population
    generation = 1
    print("--------------------")
    print(f"Generation {generation}\n")
    for j in range(size_population):
        person = ""
        for i in range(len(target)):
            person += genes[random.randrange(len(genes))]
        print(f"{person} {round(fitness(person) * 100, 2)}%")
        population.append(person)

    result = False
    while result == False:
        # mating pool
        matingPool = []
        for i in population:
            n = round(fitness(i) * 100)
            for j in range(n):
                matingPool.append(i)
        
        generation += 1
        print("--------------------")
        print(f"Generation {generation}\n")
        newPopulation = []

        for j in population:
            # crossing over
            parentA = matingPool[random.randrange(len(matingPool))]
            parentB = matingPool[random.randrange(len(matingPool))]
            # creation of a midpoint
            midpoint = random.randrange(len(target))
            child = ''
            for i in range(len(parentA)):
                if i > midpoint:
                    child += parentA[i]
                else:
                    child += parentB[i]
            
            # apply mutation
            child = list(child)
            for i in range(len(child)):
                if random.randrange(101)/100 < mutation:
                    child[i] = genes[random.randrange(len(genes))]
            child = "".join(child)
            if child != target:
                print(f"{child} {round(fitness(child) * 100, 2)}%")
                newPopulation.append(child)
                population = newPopulation
            else:
                deltatime = datetime.datetime.now() - start
                print(f"{child} {round(fitness(child) * 100, 2)}%")
                print("---------------------")
                print(f"'{child}' found at Generation {generation} in {deltatime}")
                result = True
                break

if __name__ == "__main__":
    genetic(target="HIRE ME!")