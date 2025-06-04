def solution(operations):
    answer = []
    for i in operations:
        command, num = i.split()
        num = int(num)
        
        if command == "I":
            answer.append(num)
        elif command == "D" and num==1:
            if len(answer)!= 0:
                answer.remove(max(answer))
        elif command == "D" and num==-1:
            if len(answer)!= 0:
                answer.remove(min(answer))
        
    if len(answer)==0:
        answer=[0,0]
    else:
        answer=[max(answer), min(answer)]
    return answer