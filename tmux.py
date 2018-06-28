import sqlite3
from pathlib import Path


class Bookmark:
    id = ""
    name = ""
    url = ""
    tags = []
    fav_scale = 0
    special_tags = []


class BookmarkSystem:
    last_allocated_id_no = 0
    list_by_name = {}
    tags = {}
    ids = {}

    def retrieve_data(self, c):
        """
        This method restores data from disk to the program - just the reverse of store data
        It uses cpickle or rather _pickle(renamed version for py3) to load the data-structure
        :return: None
        """
        pass

    @property
    def id_creator(self):
        """
        creates a New Id for a new Bookmark
        :return:
        """
        self.last_allocated_id_no = 0
        new_id = self.last_allocated_id_no + 1
        self.last_allocated_id_no += 1
        return new_id

    def tag_creators(self):
        """
        Gives life to the tag system
        Will be implemented at later stages - probably for beta versions
        plans - * It would create a dictionary of tags
                * each tag would have a list of websites
                * If a new tag is created by user, add it here
                * A list of tags should be shown when user creates a new Bookmark
        :return: None
        """
        pass

    def display_list(self, table):
        """
        The name is pretty self explanatory
        This method prints a list of all saved bookmarks
        :return:
        """
        print("\nWELCOME TO TMARK: A customisable Terminal Bookmarking System")
        print("================  ------------------------------------------\n")

        try:
            table.execute("SELECT * FROM bookmarks")
            bookmark = table.fetchall()
            flag = 0
            for data in bookmark:
                flag = 1
                print("ID\t\t:", data[0])
                print("NAME\t:", data[1])
                print("URL\t\t:", data[2])
                table.execute("SELECT tag FROM tags WHERE bookmark_id IS ?", data[0][0])
                tags = table.fetchall()
                print("TAGS\t:", data[0])
                for x in tags:
                    print(x, end=" ")
                print("\n------------------------------------------------------------------------------")
        except sqlite3.OperationalError:
            flag = 0

        if flag == 0:
            print("You Bookmark List is empty!")
            print("To get started, just type: a_command_goes_here_not_decided_yet ")
            print("To get Help, type: >> tmark --help")
            print("For more Information/source code visit: https://github.com/t3chn0tr0n/tmux")

    def create(self, table, database):
        """
        Creates a new Bookmark
        :return:
        """
        b = Bookmark()
        table.execute("CREATE TABLE IF NOT EXISTS bookmarks(id TEXT, name TEXT, url TEXT)")
        table.execute("CREATE TABLE IF NOT EXISTS tags(tag TEXT, bookmark_id TEXT)")

        b.name = input("Enter the name: ")
        b.url = input("Enter the url: ")
        b.tags = input("Enter tags for the bookmark, separated by commas(,): ").split(",")
        b.id = b.name[0].upper() + (str(self.id_creator).zfill(3))

        table.execute("INSERT INTO bookmarks(id, name, url) VALUES(?, ?, ?)", (b.id, b.name, b.url))
        for tag in b.tags:
            table.execute("INSERT INTO tags(tag, bookmark_id) VALUES(?, ?)", (tag.strip(), b.id))

        database.commit()


# connecting to SQLITE DB
database = sqlite3.connect('bookmarks.db')
db = database.cursor()

obj = BookmarkSystem()

# Empty Display
obj.display_list(db)

obj.create(db, database)
obj.display_list(db)

# Disconnecting from Database
db.close()
database.close()
