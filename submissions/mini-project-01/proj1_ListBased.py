def shopping_list():
    my_list = []
    print("***** Welcome to Kuya Ken's Tindahan! *****")

    while True:

        print("\nOptions:")
        print("1. Add item to the shopping list")
        print("2. View shopping list")
        print("3. Remove item from the shopping list")
        print("4. Quit")

        choice = input("\nEnter the number of your choice: ")

        if choice == "1":
            item = input("Enter the item you want to add: ")
            my_list.append(item)
            print(f"{item} has been added to your shopping list.")

        elif choice == "2":
            print("Your shopping list:")
            for item in my_list:
                print(item)

        elif choice == "3":
            item_to_remove = input("Enter the item you want to remove: ")
            if item_to_remove in my_list:
                my_list.remove(item_to_remove)
                print(f"{item_to_remove} has been removed from your shopping list.")
            else:
                print(f"{item_to_remove} is not in your shopping list.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid number. Please enter a number between 1 and 4.")

shopping_list()
