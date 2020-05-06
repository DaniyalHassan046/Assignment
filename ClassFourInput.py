
class input_class():
    filter_by = ("brand", "color", "price", "size")
    # Function to select category from menu

    def category_input(self,categories):
        inp = input("Select Category: ")
        cat = list(categories)
        print("Selected Category is: ", inp, " ", cat[int(inp) - 1])
        categories = cat[int(inp) - 1]
        return categories

    # Function to select filtering method from menu
    def filter_via(self):
        print("Select for Filtering via: ")
        print("1 brand\n2 color\n3 price\n4 size")
        inp = input("Select Number For filtering: ")
        print("Selected Filtering method is: ", inp, " ", self.filter_by[int(inp) - 1])
        self.filter_by = self.filter_by[int(inp) - 1]
        return self.filter_by
        self.check_filtering_method(self.filter_by)

    # Function to select option from 10 value's menu
    def proceeding_menu(self):
        # Next Menu
        print("1.show max price 10 items\n2.show min price 10 items\n3.show top rated 10 itemsd."
              "\n4.show latest 10 items")
        inp = input("Select number for further Proceeding: ")
        return inp



    # Function to select specific Id from details
    def id_selector(self):
        # Select Id
        inp = input("Select Id: ")
        return inp
        self.whole_detail_of_id(inp)