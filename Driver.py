from ClassOneReader import reader
from CLassTwoShow import show_class
from ClassThreeManger import manage_class
from ClassFourInput import input_class

# Driver
# print("----------------------Products------------------------")
#   print("Welcome to Products Site. Press enter to proceed.")
#   input()
input_file = dict()
categories = set()
selected_filtered_value = set()
lists = list()
r = reader()
i = input_class()
s = show_class()
m = manage_class()
input_file = r.file_reader()
categories = m.category(input_file)
s.set_show(categories)
categories = i.category_input(categories)
print(categories)
a = str(i.filter_via())  # a=color,size etc
selected_filtered_value = m.for_categories(categories, a)  # selected filter values = details of color/size etc
if selected_filtered_value != None and selected_filtered_value != "price":
    if s.set_show(selected_filtered_value):
        lists = m.filtering_for_color_size(categories, m.check_filtering_method(a, selected_filtered_value, categories),
                                           a,
                                           size_color_checker=True)
        lists=s.table(m.proceeding_menu_checker(i.proceeding_menu(), lists))
        s.whole_detail_of_id(i.id_selector(),lists)
    else:
        print("Nothing Found")

elif selected_filtered_value == "price":
    min = input("Enter minimum Price: ")
    max = input("Enter maximum Price: ")
    lists = m.filtering_for_color_size(categories, _min_price=min, _max_price=max,
                                       size_color_checker=True)
    lists=s.table(m.proceeding_menu_checker(i.proceeding_menu(), lists))
    s.whole_detail_of_id(i.id_selector(),lists)
else:
    print("There is no product in this filtering")
# self.proceeding_menu_checker(inp)
