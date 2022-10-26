import sys
import argparse


def parse_readme(full_text: str) -> tuple[list[str], list[str]]:

	admin_block = full.split("\n\n")[0].split("\n")[1:]
	user_block = full.split("\n\n")[1].split("\n")[1:]

	admin_block[0] = admin_block[0][:-6]

	all_users = admin_block[::2] + user_block
	
	passwords = [password[14:] for password in admin_block[1::2]]
	
	return all_users, passwords


# print(f"{admin_block!r}")
# print(f"{user_block!r}")

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Process the list of users from the README')
	parser.add_argument("text", help="The block of users from the README. Include the headers for the sections, and the passwords")
	parser.add_argument("target", choices=["users", "passwords", "both"])

	args = parser.parse_args()
		
	users, passwords = parse_readme(args.text)

	if args.target == "users":
		print('\n'.join(users))
	elif args.target == "passwords":
		print("\n".join(passwords))
	elif args.target == "both":
		print("Users:")
		print("\n".join(users))
		print()
		print("Passwords:")
		print("\n".join(passwords))
	
	
	
	