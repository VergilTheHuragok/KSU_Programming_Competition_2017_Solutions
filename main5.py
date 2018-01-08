inp = input().replace(" ", "").upper()

teams = {"A": 0, "B": 0, "C": 0, "D": 0}

cases = ["AB", "AC", "AD", "BC", "BD", "CD"]

ind = 0
print(inp)
for case in cases:
    if inp[ind] == "W":
        teams[case[0]] += 3
    elif inp[ind] == "L":
        teams[case[1]] += 3
    elif inp[ind] == "T":
        teams[case[0]] += 1
        teams[case[1]] += 1

    ind += 1

win_scores = sorted(teams.values(), reverse=True)
win_teams = []

def get_team(score, win_teams):
    for team in teams:
        if teams[team] == score and team not in win_teams:
            return team

for score in win_scores:
    win_teams.append(get_team(score, win_teams))

out = ""
ind = 0
for team in win_teams:
    if ind == len(teams) - 1:
        semi = ""
    else:
        semi = "; "
    out += team + " " + str(teams[team]) + "pts" + semi
    ind += 1
print(out)
