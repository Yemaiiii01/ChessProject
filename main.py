from views import MainView

def main():
    view = MainView()
    while True:
        action = view.show_main_menu()
        if action == '1':
            view.create_tournament()
        elif action == '2':
            view.manage_tournament()
        elif action == '3':
            view.view_tournaments()
        elif action == '0':
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
