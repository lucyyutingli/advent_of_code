def sum_answers(file):
    new_file = open(file, "r")
    lines = new_file.read()
    answers = lines.split("\n\n")
    sum = 0
    
    for i,j in enumerate(answers):
        answers[i] = j.replace("\n", "")
    for k in answers:
        sum += len(set(k))
    print(sum)
    
sum_answers("day6_input.txt")

def sum_answers_all(file):
    new_file = open(file, "r")
    lines = new_file.read()
    groups = lines.split("\n\n")    
    current = 0
    
    for i,j in enumerate(groups):
        if i == len(groups) - 1:
            num_people = j.count("\n")
        else:
            num_people = j.count("\n") + 1
        print(j)
        print(num_people)
        
        current_answers = j.replace("\n", "")
        seen_characters = ""
        total_answers = 0
        answer_counter = 0
        
        for i in current_answers:
            if i in seen_characters:
                continue
            else:
                answer_counter = current_answers.count(i)
                if answer_counter == num_people:
                    total_answers += 1
                seen_characters += i
        current += total_answers
        
    print(current)        
            
    
sum_answers_all("day6_input.txt")
