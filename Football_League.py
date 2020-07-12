if __name__ == "__main__":
    num = int(input("Enter number of teams : "))
    team_names = list(map(str,input("Enter team names : ").split()))
    dict_scores = {}
    dict_rank = {}
    for i in team_names:
        dict_scores[i] = [0,0,0,0,1]
    no = int(input("Number of matches : "))
    for i in range(no):
        score = list(map(str,input("Enter Score : ").split()))
        # goals scored
        dict_scores[score[0]][0] = dict_scores[score[0]][0]+int(score[2])
        dict_scores[score[1]][0] = dict_scores[score[1]][0]+int(score[3])
        # goals conceded
        dict_scores[score[0]][1] = dict_scores[score[0]][1]+int(score[3])
        dict_scores[score[1]][1] = dict_scores[score[1]][1]+int(score[2])
        # goal difference
        dict_scores[score[0]][2] = dict_scores[score[0]][0]-dict_scores[score[0]][1]
        dict_scores[score[1]][2] = dict_scores[score[1]][0]-dict_scores[score[1]][1]
        # points
        if score[2]>score[3]:
            dict_scores[score[0]][3] = dict_scores[score[0]][3] + 2
            dict_scores[score[1]][3] = dict_scores[score[1]][3] + 0
        elif score[2]<score[3]:
            dict_scores[score[1]][3] = dict_scores[score[1]][3] + 2
            dict_scores[score[0]][3] = dict_scores[score[0]][3] + 0
        else:
            dict_scores[score[0]][3] = dict_scores[score[0]][3] + 1
            dict_scores[score[1]][3] = dict_scores[score[1]][3] + 1
            
    def points():
        for i in team_names:
            dict_rank[i] = num - dict_scores[i][3]
        # print(dict_rank)
        print(sorted(dict_rank.items(), key = 
            lambda kv:kv[1]))
    points()
    # print(dict_scores)