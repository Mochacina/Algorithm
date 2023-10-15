def solution(today, terms, privacies):
    answer = []
    
    today_n = dateToNum(today)
    terms_l = {n.split(" ")[0]:int(n.split(" ")[1]) for n in terms}
    
    for n, privacy in enumerate(privacies):
        date = dateToNum(privacy.split(" ")[0])
        term = privacy.split(" ")[1]
        print(today_n, date+terms_l.get(term)*28)
        if today_n >= date+terms_l.get(term)*28: answer.append(n+1)
    
    return answer

def dateToNum(today):
    today_l = today.split(".")
    today_n = int(today_l[0])*336 + int(today_l[1])*28 + int(today_l[2])
    return today_n

today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

print(solution(today, terms, privacies))