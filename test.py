
def insert_list(lst, index, item):
    lst.insert(index, item)
    print(f"Item '{item}' inserted at index {index}.")
def remove_list(lst, item):
    if item in lst:
        lst.remove(item)
        print(f"Item '{item}' removed from the list.")
    else:
        print(f"Item '{item}' not found in the list.")
def sort_list(lst):
    lst.sort()
    print("List sorted.")
def extend_list(lst, new_items):
    lst.extend(new_items)
    print("List extended with new items.")
def reverse_list(lst):
    lst.reverse()
    print("List reversed.")
def traverse_list(lst):
    print("List elements:")
    for item in lst:
        print(item)
        
def main():
    my_list = []
    
    while True:
        print("\nMenu:")
        print("1. Insert item into the list")
        print("2. Remove item from the list")
        print("3. Sort the list")
        print("4. Extend the list")
        print("5. Reverse the list")
        print("6. Traverse the list")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")
        if choice == '1':
            index = int(input("Enter the index to insert: "))
            item = input("Enter the item to insert: ")
            insert_list(my_list, index, item)
        elif choice == '2':
            item = input("Enter the item to remove: ")
            remove_list(my_list, item)
        elif choice == '3':
            sort_list(my_list)
            n = sort_list()
            print(n)
        elif choice == '4':
            new_items = input("Enter new items (comma-separated): ").split(',')
            extend_list(my_list, new_items)
        elif choice == '5':
            reverse_list(my_list)
        elif choice == '6':
            traverse_list(my_list)
        elif choice == '7':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")
if __name__ == "__main__": main()

