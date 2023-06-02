from databasing import dig_followers, save_database, load_database, generate_diagram
from request_handling import get_user_id, init_session
import datetime

if __name__ == '__main__':
    print("Generating diagram...")

    # Get username and password

print("Enter your GitHub username:")
username = input()

# should be using token instead of password, but tokens are hard
# ended up switching to token anyway
print("Enter your GitHub token:")
password = input()
init_session(username, password)

user = input("Enter the username of the user you want to generate a diagram for: ")
depth = int(input("Enter the depth of the diagram: "))
user_id = get_user_id(user)
start_time = datetime.datetime.now()

print(str(start_time) + " Starting dig 🫡")
dig_followers(user_name=user, prev_id=user_id, depth=depth)
print(str(datetime.datetime.now()) + " Dig complete 🪓")
save_database()

load_database()
print("Generating diagram...")
generate_diagram(r'diagram.png')

