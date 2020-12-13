questions = {}

def groupQuestions(data):
    count = 0
    everyone = 0
    people = 0
    for x in data:
        if x != "":
            d = dict.fromkeys(x)
            for key, value in d.items():
                questions[key] = questions.setdefault(key, 0) + 1
            people += 1
        else:
            count += len(questions)
            everyone += len([key for key, value in questions.items() if value == people])
            people = 0
            questions.clear()
    count += len(questions)
    everyone += len([key for key, value in questions.items() if value == people])
    people = 0
    questions.clear()
    return(count, everyone)


with open('input.txt', 'rt') as f:
        data = [line.strip() for line in f.readlines()]

count, everyone = groupQuestions(data) 
print(count)
print(everyone)