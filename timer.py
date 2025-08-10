import time

question = int(input("How many pomodoro rounds do you want to do?: "))

for x in range(question):
    print("Pomodoro Round ", x + 1, " - ", "Focus Timer  🍅")

    for y in range(5, 0, -1):
        print(y)
        time.sleep(1)

    print("✅ Focus complete! Time for a break")

    for d in range(3, 0, -1):
        print(d)
        time.sleep(1)
    print("Break Time Complete. Lets get back to work")
