global f
f=0
#This t_movie function is used to select the movie
def t_movie():
    global f
    f=f+1
    print("Which movie do you want to watch?")
    print("1,Movie 1 ")
    print("2,Movie 2 ")
    print("3,Movie 3 ")
    print("4. back")
    movie=int(input("Choose your movie: "))
    if movie == 4:
        #In this it's goes to center function
        #from center it's goes to movie function
        #And it's come back here and go back to theater
        center()
        theater()
        return 0
    if f == 1:
        theater()

#This theater function is used to select the screen:
def theater():
    print("Which screen do you want to watch movie: ")
    print("1,SCREEN 1")
    print("2,SCREEN 2")
    print("3,SCREEN 3")
    a=int(input("Choose your screen: "))
    ticket=int(input("Number of ticket do you want?: "))
    timing(a)

#timing(a) is used to select timing for movies:
def timing(a):
    time1 = {
        "1":"10:00-1:00",
        "2":"1:10-4:10",
        "3":"4:20-7:20",
        "4":"7:30-10:30"
        }
    time2 = {
        "1":"10:15-1:15",
        "2":"1:25-4:25",
        "3":"4:35-7:35",
        "4":"7:45-10:45"
        }
    time3 = {
        "1":"10:30-1:30",
        "2":"1:40-4:40",
        "3":"4:50-7:50",
        "4":"8:00-10:45"
        }
    if a == 1:
        print("Choose your time: ")
        print(time1)
        t=input("Select your time: ")
        x=time1[t]
        print("Successfull!, enjoy movie at "+x)
    elif a==2:
        print("Choose your time: ")
        print(time2)
        t=input("Select your time: ")
        x=time2[t]
        print("Successfull!, enjoy movie at "+x)
    elif a==3:
        print("Choose your time: ")
        print(time3)
        t=input("Select your time: ")
        x=time3[t]
        print("Successfull!, enjoy movie at "+x)
    return 0

#movie(theater): This method is used to select movies accordingly to the theater

def movie(theater):
    if theater == 1:
        t_movie()
    elif theater == 2:
        t_movie()
    elif theater == 3:
        t_movie()
    elif theater == 4:
        city()
    else:
        print("wrong choice")

#center(): This method is used to select the theater

def center():
    print("Which theater do you wish to see the movie? ")
    print("1,Inox")
    print("2,Icon")
    print("3,pvp")
    print("4, back")
    a = int(input("choose your option: "))
    movie(a)
    return 0

#City(): This method is used to select the city:

def city():
    print("Hi welcome to movie ticket booking: ")
    print("Where you want to watch the movie?: ")
    print("1,city 1")
    print("2,city 2")
    print("3, city 3")
    place=int(input("Choice your option: "))
    if place==1:
        center()
    elif place==2:
        center()
    elif place==3:
        center()
    else:
        print("Wrong choice!!!")
    
city()    
