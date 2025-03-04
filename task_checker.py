#Ask for users name
name = input("What is your name?")
#start task details
total_tasks = 5
completed_tasks = 0
#define each task
task1_status = input ("Did you complete your 30 minutes reading exercise? (yes/no): ")
if task1_status.lower() == 'yes':
    completed_tasks += 1

task2_status = input("Did you go to MSIMBO class today? (yes/no): ")
if task2_status.lower() == 'yes':
    completed_tasks += 1

task3_status = input("Did you do 50 pushups? (yes/no): ")
if task3_status.lower() == 'yes':
    completed_tasks += 1

task4_status = input("Did you pray today? (yes/no): ")
if task4_status.lower() == 'yes':
    completed_tasks += 1

task5_status = input("Did you comminicate with loved ones today? (yes/no): ")
if task5_status.lower() == 'yes':
    completed_tasks += 1

#Calculate progress
progress_percentage = (completed_tasks / total_tasks) * 100
print(f"You are {progress_percentage} done!")
#provide feedback
if progress_percentage == 100:
    print(f"Amazing job {name}! You've completed all tasks!")
elif progress_percentage >= 66.6:
    print(f"Keep going {name}! You're more than halfway there!")
else:
    print(f"You can do it {name}! Every step counts!")