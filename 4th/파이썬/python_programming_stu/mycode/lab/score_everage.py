# 2차원 배열
# 학생별 과목의 평균을 계산

kor_score = [49, 79, 20, 100, 80]
math_score = [43, 59, 85, 30, 90]
eng_score = [49, 79, 48, 60, 100]
midterm_score = [kor_score, math_score, eng_score]

student_score = [0, 0, 0, 0, 0]

for i in range(3):
    for j in range(5):
        student_score[j] += midterm_score[i][j]

for i in range(5):
    student_score[i] = round((student_score[i] / 3), 2)

aver = {'A': student_score[0],
        'B': student_score[1],
        'C': student_score[2],
        'D': student_score[3],
        'E': student_score[4]}

print(aver)
