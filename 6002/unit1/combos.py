# generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo


def yieldAllCombos(items):
    """
      Generates all combinations of N items into two bags, whereby each 
      item is in one or zero bags.

      Yields a tuple, (bag1, bag2), where each bag is represented as 
      a list of which item(s) are in each bag.
    """
    N=len(items)
    for i in range(3**N):
        combo1=[]
        combo2=[]
        for j in range(N):
            # basically, we need to convert the combinations into number based 3
            # then check for each digit's place for item placement (not-placed, bag1, bag2)
            if (i // 3**j) % 3 == 1:
                combo1.append(items[j])
            if (i // 3**j) % 3 == 2:
                combo2.append(items[j])
        yield (combo1, combo2)
        
if __name__ == "__main__":
    items = ['apple', 'orange', 'peach', 'banana']
    print("power set:")
    for combo in powerSet(items):
        print(combo)

    print ("yield all combos:")
    for combo in yieldAllCombos(items):
        print(combo)
