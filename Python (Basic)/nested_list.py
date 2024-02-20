if __name__ == '__main__':
    students_dict = {} # {name: score,}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        students_dict[name] = score
    
    # order by score(dict_value)
    score_list = sorted(set(students_dict.values()))
    
    # find second last score -> score_list[1]
    # find names of that score
    second_lowest_students = []
    for name, score in students_dict.items():
        if score == score_list[1]:
            second_lowest_students.append(name)
            
    # order by their names alphabetically
    second_lowest_students = sorted(second_lowest_students)
    # print(*second_lowest_students,sep='\n')
    for name in second_lowest_students:
        print(name)
