import json

def get_author_name(a):
	if a.lower() == "h":
		return "Haizlbliek"
	if a.lower() == "z":
		return "Zephyrus"

	return a

def add_song(title, authors, url, date):
	authors = [ get_author_name(a) for a in authors ]

	with open('songs.json', 'r', encoding='utf-8') as f:
		content = f.read()

	song = {
		"title": title,
		"versions": [
			{
				"authors": authors,
				"url": url
			}
		],
	}
	if date:
		song["versions"][0]["date"] = date

	insert_index = content.rfind("}") - 1

	insert_text = ",\n\t\"" + title + "\": " + json.dumps(song, indent="\t").replace("\n", "\n\t")

	new_content = content[:insert_index] + insert_text + content[insert_index:]

	with open('songs.json', 'w', encoding='utf-8') as f:
		f.write(new_content)

if __name__ == "__main__":
	title = input("Title:")
	authors = [a.strip() for a in input("Author(s):").split(",")]
	date = input("Date:")
	url = input("Url:")

	add_song(title, authors, url, date)
