if __name__ == '__main__':
    names = []
    scores = []
    scores1 = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        names.append(name)
        scores.append(score)
        scores1.coppy(scores)
    min = scores[0]
    #print(scores)
    #print(names)
    scores1.sort()
    for i in scores:
        if min > i:
            min = i
    print(min)
    for a in scores1:
        while a == min:
            scores1.remove(a)
    print(scores1)    
    predict = scores1[0]
    for i in range(len(names)):
        if predict == scores[i]:
            print(names[i])