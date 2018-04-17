from texttable import Texttable
import _pickle as FileTruck


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

    def retrieve_data(self):
        """
        This method restores data from disk to the program - just the reverse of store data
        It uses cpickle or rather _pickle(renamed version for py3) to load the data-structure
        :return: None
        """
        pass

    def store_data(self):
        """
        This method restores data from disk to the program - just the reverse of store data
        It uses cpickle or rather _pickle(renamed version for py3) to dump the data-structure
        :return: None
        """
        pass

    def id_creator(self):
        """
        creates a New Id for a new Bookmark
        :return:
        """
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

    def display_list(self):
        """
        The name is pretty self explanatory
        This method prints a list of all saved bookmarks
        :return:
        """
        print("\nWELCOME TO TMARK: A customisable Terminal Bookmarking System")
        print("================  ------------------------------------------")
        print()
        for bookamrks in self.list_by_name:
            temp_bookmark = self.list_by_name[bookamrks]
            print("ID\t\t:", temp_bookmark.id)
            print("NAME\t:", temp_bookmark.name)
            print("URL\t\t:", temp_bookmark.url)
            print("TAGS\t:", temp_bookmark.tags)
            print("\n------------------------------------------------------------------------------")
        else:
            print("You Bookmark List is empty!")
            print("To get started, just type: a_command_goes_here_not_decided_yet ")
            print("To get Help, type: >> tmark --help")
            print("For more Information/source code visit: https://github.com/t3chn0tr0n/tmux")

    def create(self):
        """
        Creates a new Bookmark
        :return:
        """
        b = Bookmark()

        name_of_bookmark = input("Enter the name: ")
        url_of_bookmark = input("Enter the url: ")
        tags_for_bookmark = input("Enter tags for the bookmark, seperated by commas(,): ").split(",")

        b.name = name_of_bookmark
        b.url = url_of_bookmark
        b.id = b.name[0].upper() + (str(self.id_creator()).zfill(3))
        b.tags = tags_for_bookmark          # this is only temporary! for alpha version

        self.list_by_name[b.name] = b


obj = BookmarkSystem()
# Empty Display
obj.display_list()

obj.create()
obj.display_list()




