import json

with open('task_7.json', 'w', encoding='utf-8') as fw:
    with open('task_7.txt', encoding='utf-8') as f:
        profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in f}
        result = [profit, {'средняя прибыль': round(sum([int(i) for i in profit.values() if int(i) > 0]) /
                                                    len([int(i) for i in profit.values() if int(i) > 0]))}]
    json.dump(result, fw, ensure_ascii=False, indent=4)
