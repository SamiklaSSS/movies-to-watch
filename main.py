import json

moviesS = []

# read movies file into variable
with open('movies.json', 'r') as openfile:
    # Reading from json file
    moviesJ = json.load(openfile)

moviesR = []

i = -1

while True:
    print("\nMovie Tracker Menu:")
    print("1. Pievienot filmu")
    print("2. Rādīt visas pievienotas filmas sakartotas pēc reitinga")
    print("3. Rādīt vēl neskatītās filmas")
    print("4. Atzimēt filmu kā skatītu")
    print("5. Dzēst filmu no saraksta")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        # https://www.w3schools.com/python/python_dictionaries.asp
        # https://www.w3schools.com/python/python_lists_add.asp
         title = input("Enter movie title: ")
         rating = input("Enter movie rating: ")
         if input("Have you watched this movie?(Answer Yes or No)") == "Yes":
             watched = True
         else:
             watched = False

         movie = {
            "title": title,
            "rating": float(rating),
            "watched": watched
         }
         moviesS.append(movie) 
         print(moviesS)
         with open("movies.json", "w") as movies_file:
             json.dump(moviesS, movies_file)
         pass
    
    elif choice == "2":
        # https://www.w3schools.com/python/python_lists_sort.asp
        # https://www.w3schools.com/python/python_dictionaries_access.asp
        pass
    
    elif choice == "3":
        # https://www.w3schools.com/python/python_lists_comprehension.asp
        # https://www.w3schools.com/python/python_dictionaries_access.asp
        print("You want to see unwatched films? I will show you!")
        moviesJ.sortR
        sortR:
             while i < 100:
             i = i + 1
         if watched == False:
            watched == True
         elif watched = True:
            watched == False
         return
        moviesR.append()
    else:
        pass
        print(moviesR)
        pass
    
    elif choice == "4":
        # https://www.w3schools.com/python/python_lists_change.asp
        # https://www.w3schools.com/python/python_dictionaries_change.asp
        id = int(input("Enter the index of the movie to mark: "))
        print(moviesJ[id])
        if  watched == ("Watched = False"):
            watched == ("Watched = True")
            return(watched, moviesJ[id])
        elif  watched == ("Watched = True"):
            watched == ("Watched = False")
            return(watched, moviesJ[id])
        else:
            print("Error")
        pass
    
    elif choice == "5":
        # https://www.w3schools.com/python/python_lists_remove.asp
        id = int(input("Enter the index of the movie to remove: "))
        remove.moviesJ(movie[id])
    
    elif choice == "6":
        print("Exiting...")
        break
    
    else:
        print("Invalid choice. Please try again.")

# writing movies to file
#with open("movies.json", "w") as movies_file:
#    json.dump(moviesS, movies_file)
