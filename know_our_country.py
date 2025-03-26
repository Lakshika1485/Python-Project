from random import shuffle

li=[
    ("What is the captial of your country", "India"),
    ("What is the national bird of your country", "Peacock"),
    ("What is the national animal of your country", "Tiger"),
    ("What is the national tree of your country", "Baniyan"),
    ("What is the national flag of your country", "Tiranga"),
    ("What is the national flower of your country", "Lotus"),
] 
shuffle(li)
right =0
wrong =0
for que, right_ans in li:
    ans= input(que + " ")
    if ans.title == right_ans:
        right+=1
    else:
        print("Wrong ans")
        wrong-=1
print("good job")
print("you gave ", right_ans , "right answer and", wrong, "wrong answers")