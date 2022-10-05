import sys



def parse_readme_users(full_text: str) -> tuple[list[str], list[str]]:

	admin_block = full.split("\n\n")[0].split("\n")[1:]
	user_block = full.split("\n\n")[1].split("\n")[1:]

	admin_block[0] = admin_block[0][:-6]

	all_users = admin_block[::2] + user_block
	
	passwords = [password[14:] for password in admin_block[1::2]]
	
	return all_users, passwords


# print(f"{admin_block!r}")
# print(f"{user_block!r}")

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("Not enough arguments!")
		exit(-1)
	if len(sys.argv) > 2:
		print("Too many arguments!")
		exit(-2)
		
	full = sys.argv[1]
	users, passwords = parse_readme_users(full)
	
	print("Users:")
	print("\n".join(users))
	print()
	print("Passwords:")
	print("\n".join(passwords))
	
	
	
	