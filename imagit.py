import mysillylibrary

if __name__ == "__main__":
    fp = open("sillystory", "w")
    fp.write(mysillylibrary.story)
    fp.close()
