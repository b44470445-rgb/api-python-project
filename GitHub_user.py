import requests

username = input("Enter GitHub username: ")

url = f"https://api.github.com/users/{username}"

response = requests.get(url)

print(response.status_code)
print(response.json())
print("Hello Bishal")
print("Hello Brother's") 