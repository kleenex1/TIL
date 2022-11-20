def solution(survey, choices):
    answer = ''
    persona = {"R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0}

    for i in range(len(choices)):
        l = survey[i][0]
        r = survey[i][1]
        if choices[i] - 4 > 0:
            persona[r] += choices[i] -4 
        elif choices[i] - 4 < 0:
            persona[l] += 4 - choices[i]

    answer += "R" if persona["R"] >= persona["T"] else "T"
    answer += "C" if persona["C"] >= persona["F"] else "F"
    answer += "J" if persona["J"] >= persona["M"] else "M"
    answer += "A" if persona["A"] >= persona["N"] else "N"
            
    return answer

survey = ["AN", "CF", "MJ", "RT", "NA"]
chocies = [5, 3, 2, 7, 5]

print(solution(survey, chocies))