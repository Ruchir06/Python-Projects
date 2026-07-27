day = str(input("Enter the day of the week: ")).capitalize()
match day: 
    case 'Monday' | 'Tuesday' | 'Wednesday' | 'Thursday' | 'Friday':
        print(f"{day} is a weekday")
    case 'Saturday' | 'Sunday':
        print(f"{day} is a weekend")
    case _:
        print(f"{day} is not a valid day")