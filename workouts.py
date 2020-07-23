import pandas as pd 
from matplotlib import pyplot as plt

class User:
    __file_path = "users.csv"

    __users = {} #store data here

    def __init__(self):
        User.__read_data()
        self.record = None

    @classmethod
    def __read_data(cls):
        try:
            file = open(User.__file_path, 'r')
            for line in file:
                column = line.split(',')
                User.__users[column[0]] = [column[0], column[1]]
            file.close()
        except Exception as e:
                print("error--", Exception, " ", e)

    def login(self, name):
        if User.__users.get(name):
            self.record = User.__users.get(name)
            print(f'Welcome back {self.record[0]}.')
        else: 
            print("I can't find that user name.")

    @classmethod
    def add_user(cls, name):
        file = open(User.__file_path, 'a+')
        file.write(f"{name},[]\n")
        file.close()
        User.__read_data()
        print(f"Your account has been created")

    def __save_data(self):
        with open(User.__file_path, "r+") as f:
            d = f.readlines()
            f.seek(0)
            for i in d:
                column = i.split(',')
                if column[0] != self.name:
                    f.write(i)
            f.write(f"{self.name},[]\n")
            f.truncate()
    @property
    def user_name(self):
        self.name = self.record[0]
        return f"{self.name}"

class Exercise:
    __file_path = "workouts.csv"
    
    def __init__(self, user, date, exercise_name, sets, reps):
        self.user_name = None
        self.date = date
        self.exercise = exercise_name
        self.sets = sets 
        self.reps = reps
        self.set_user_and_add_workout(user)
    
    def send_data_to_user(self):
        pass

    def set_user_and_add_workout(self, user):
        if isinstance(user, User):
            self.user_name = user.user_name
            file = open(Exercise.__file_path, 'a+')
            file.write(f"{id(self)},{self.user_name},{self.date},{self.exercise},{self.sets},{self.reps}\n")
            file.close()
        else:
            print("Sorry, I cant find that user. Set up an account and try again. ")

class Reports:
    df = pd.read_csv('workouts.csv')
    df['total_reps'] = df['reps'] * df['sets']
    df.drop(labels = ['id'], axis='columns', inplace=True)

    def __init__(self, user):
        self.user = user
        self.show_all_my_exercises()
        self.by_exercise()
        self.find_total_reps()
        # self.all_exercise_totals()
    
    def show_all_my_exercises(self):
        usr = self.user.user_name
        print(" ")
        print("All of your exercises")
        print(Reports.df[Reports.df['username'] == usr])
        
    def by_exercise(self):
        report = Reports.df['exercise_name'].value_counts()
        labels = Reports.df['exercise_name'].value_counts().index
        # for line in report:
        #     print(line.index)
        print(" ")
        print("Exercise Value Counts")
        print(report)
        print(labels)
        plt.pie(report, labels=labels, autopct='%1.1f%%')
        plt.legend
        plt.show()
    
    def find_total_reps(self):
        usr = self.user.user_name
        print(" ")
        print("Exercise stats by day")
        print(Reports.df[Reports.df['username'] == usr].groupby(['date', 'exercise_name']).agg('sum'))

    def all_exercise_totals(self):
        print(Reports.df[['username', 'exercise_name', 'sets', 'reps']])





test1 = User()
test1.login('TestUser')
# print(test1.user_name)
# ex1 = Exercise(test1, "07/22/2020", "jump rope", 3, 50)
# test3.add_user("Test 3")
# test1 = User()
# test1.login('TestUser')
rep1 = Reports(test1)
# ex1 = Exercise(test1, "07/19/2020", "Push ups", 3, 20)
# ex2 = Exercise(test1, "07/19/2020", "Pull ups", 3, 20)
# ex3 = Exercise(test1, "07/19/2020", "Squats", 3, 20)
# ex4 = Exercise(test1, "07/19/2020", "Bench press", 3, 20)
# ex5 = Exercise(test1, "07/19/2020", "Lat Pulldown", 3, 20)

# test2 = User()
# test2.login('Test 2')
# ex1 = Exercise(test2, "07/21/2020", "Bulgarian Squat", 3, 10)
# rep1 = Reports(test2)

# ex1 = Exercise(test2, "07/19/2020", "Push ups", 3, 20)
# ex2 = Exercise(test2, "07/19/2020", "Pull ups", 3, 20)
# ex3 = Exercise(test2, "07/19/2020", "Squats", 3, 20)
# ex4 = Exercise(test2, "07/19/2020", "Bench press", 3, 20)
# ex5 = Exercise(test2, "07/19/2020", "Lat Pulldown", 3, 20)

# test3 = User()
# test3.login('Test 3')
# ex1 = Exercise(test3, "07/19/2020", "Push ups", 3, 20)
# ex2 = Exercise(test3, "07/19/2020", "Pull ups", 3, 20)
# ex3 = Exercise(test3, "07/19/2020", "Squats", 3, 20)
# ex4 = Exercise(test3, "07/19/2020", "Bench press", 3, 20)
# ex5 = Exercise(test3, "07/19/2020", "Lat Pulldown", 3, 20)


