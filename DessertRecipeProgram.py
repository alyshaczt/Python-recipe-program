# Problem: People have ingredients in their kitchen and want to see what desserts they can make based on what ingredients they already have
# Solution: code used to give user recipe options for dessert based on what they have in their kitchen and also gives option to show user the ingredients to recipes they did not have the proper ingredients for

# define function that asks questions about what ingredients the user has and gives them options of what desserts they could make with the ingredients they have stated they have
def dessert_recipes():
    # ask user whether they have an egg substitute or not, if not then they will require less ingredients for certain recipes
    egg_or_no = input("Do you have an egg substitute? 'yes' or 'no'?:")

    # tell user how to answer the following questions that they are going to be asked
    print("Please answer the following questions with either 'yes' or 'no'")
    print(". . .")

    # ask user series of questions about what ingredients they have that can be answered with either yes or no
    question1 = input("Do you have eggs?:")
    question2 = input("Do you have butter?:")
    question3 = input("Do you have white sugar?:")
    question4 = input("Do you have brown sugar?:")
    question5 = input("Do you have vanilla extract?:")
    question6 = input("Do you have flour?:")
    question7 = input("Do you have milk?:")
    question8 = input("Do you have baking powder?:")
    question9 = input("Do you have cocoa powder?:")
    question10 = input("Do you have salt?:")
    question11 = input("Do you have chocolate chips?")
    question12 = input("Do you have any fruit?:")
    question13 = input("Do you have cinnamon?:")
    question14 = input("Do you have cornstarch?:")
    question15 = input("Do you have vegetable oil and/or olive oil and/or canola oil?:")
    question16 = input("Do you have baking soda?:")
    print(". . .")

    # if the fact that they don't have an egg substitute is true, then these are the ingredients required to make the following recipes
    if (egg_or_no == "no")==True:

        #if user has eggs, butter, white sugar, vanilla extract, flour, milk and baking powder, then they have the proper ingredients for vanilla cake/cupcakes
        if (((question1=="yes") and (question2=="yes")) and ((question3=="yes") and (question5=="yes")) and ((question6=="yes") and (question7=="yes")) and (question8=="yes")):
            print("With these ingredients you could make a Vanilla Cake or Vanilla Cupcakes!")
            print("Find the whole recipe with specific details on how to make the cake from this link: https://www.allrecipes.com/recipe/17481/simple-white-cake/")
            print(". . .")
        #if user did not have eggs, butter, white sugar, vanilla extract, flour, milk and baking powder, then they don't have the proper ingredients for vanilla cake/cupcakes
        else:
            print("You don't have the proper ingredients to make Vanilla Cake or Vanilla Cupcakes")
            print(". . .")

        #if user has eggs, butter, white sugar, vanilla extract, flour, baking powder, cocoa powder, and salt, then the user has the proper ingredients for brownies
        if (((question1=="yes") and (question2=="yes")) and ((question3=="yes") and (question5=="yes")) and ((question6=="yes") and (question8=="yes")) and ((question9=="yes") and (question10=="yes"))):
            print("With these ingredients you could make Brownies!")
            print("Find the whole recipe with specific details on how to make the brownies from this link: https://www.allrecipes.com/recipe/10549/best-brownies/")
            print(". . .")
        #if user did not have eggs, butter, white sugar, vanilla extract, flour, baking powder, cocoa powder, and salt, then user cannot make brownies
        else:
            print("You don't have the proper ingredients to make Brownies")
            print(". . .")

        #if user has eggs, butter, white sugar, brown sugar, vanilla extract, flour, salt and chocolate chips, then the user has enough ingredients to make chocolate chip cookies
        if (((question1=="yes") and (question2=="yes")) and ((question3=="yes") and (question4=="yes")) and ((question5=="yes") and (question6=="yes")) and ((question10=="yes") and (question11=="yes"))):
            print("With these ingredients you could make Chocolate Chip Cookies!")
            print("Find the whole recipe with specific details on how to make the cookies from this link: https://www.allrecipes.com/recipe/10813/best-chocolate-chip-cookies/")
            print(". . .")

        #if user does not have eggs, butter, white sugar, brown sugar, vanilla extract, flour, salt and chocolate chips, then user does not have the proper ingredients to make chocolate chip cookies
        else:
            print("You don't have the proper ingredients to make Chocolate Chip Cookies")
            print(". . .")

        #if user has butter, brown or white sugar, flour, salt, fruit, cinnamon, and cornstarch, then they have the proper ingredients to make Pie with any type of fruit filling
        if (((question2=="yes") and ((question3 or question4)=="yes")) and ((question6=="yes") and (question10=="yes")) and ((question12=="yes") and (question13=="yes")) and (question14=="yes")):
            print("With these ingredients you could make Pie! Whether it be a Blueberry Pie or Apple Pie, depending on what fruit you have.")
            print("Find the whole recipe with specific details on how to make the pie from this link: https://www.inspiredtaste.net/22662/flaky-pie-crust-recipe/")
            print(". . .")
        #if user does not have butter, brown or white sugar, flour, salt, fruit, cinnamon, and cornstarch, then they don't have the proper ingredients to make Pie with any type of fruit filling
        else:
            print("You don't have the proper ingredients to make Pie")
            print(". . .")

        #if user has eggs, white sugar, brown sugar, flour, milk, baking powder, salt, chocolate chips, and vegetable oil and/or olive oil and/or canola oil, then they have the proper ingredients to make chocolate chip muffins
        if (((question1=="yes")) and ((question3=="yes") and (question4=="yes")) and ((question6=="yes") and (question7=="yes")) and ((question8=="yes") and (question10=="yes")) and ((question11=="yes") and (question15=="yes"))):
            print("With these ingredients you could make Chocolate chip muffins!")
            print("Find the whole recipe with specific details on how to make the muffins from this link: https://www.allrecipes.com/recipe/7906/chocolate-chip-muffins/")
            print(". . .")
        #if the user does not have eggs, white sugar, brown sugar, flour, milk, baking powder, salt, chocolate chips, and vegetable oil and/or olive oil and/or canola oil, then they do not have the proper ingredients to make chocolate chip muffins
        else:
            print("You don't have the proper ingredients to make Chocolate chip muffins")
            print(". . .")

        #if user has eggs, butter, white sugar, vanilla extract, flour, baking powder and baking soda, then user has the proper ingredients to make sugar cookies
        if (((question1=="yes") and (question2=="yes")) and ((question3=="yes") and (question5=="yes")) and ((question6=="yes") and (question8=="yes")) and (question16=="yes")):
            print("With these ingredients you could make Sugar Cookies!")
            print("Find the whole recipe with specific details on how to make the cookies from this link: https://www.allrecipes.com/recipe/9870/easy-sugar-cookies/")
            print(". . .")
        #if user does not have eggs, butter, white sugar, vanilla extract, flour, baking powder and baking soda, then the user does not have the proper ingredients to make sugar cookies
        else:
            print("You don't have the proper ingredients to make Sugar Cookies")
            print(". . .")

    # if the fact that they do have an egg substitute is true, then these are the ingredients required to make the following recipes (recipes are the same except eggs are no longer required)
    if (egg_or_no == "yes")==True:

        #if user has butter, white sugar, vanilla extract, flour, milk and baking powder, then they have the proper ingredients for vanilla cake/cupcakes
        if ((question2=="yes") and ((question3=="yes") and (question5=="yes")) and ((question6=="yes") and (question7=="yes")) and (question8=="yes")):
            print("With these ingredients you could make a Vanilla Cake or Vanilla Cupcakes!")
            print("Find the whole recipe with specific details on how to make the cake from this link: https://www.allrecipes.com/recipe/17481/simple-white-cake/")
            print(". . .")
        #if user does not have butter, white sugar, vanilla extract, flour, milk and baking powder, then they do not have the proper ingredients for vanilla cake/cupcakes
        else:
            print("You don't have the proper ingredients to make Vanilla Cake or Vanilla Cupcakes")
            print(". . .")

        #if user has butter, white sugar, vanilla extract, flour, baking powder, cocoa powder, and salt, then the user has the proper ingredients for brownies
        if ((question2=="yes") and ((question3=="yes") and (question5=="yes")) and ((question6=="yes") and (question8=="yes")) and ((question9=="yes") and (question10=="yes"))):
            print("With these ingredients you could make Brownies!")
            print("Find the whole recipe with specific details on how to make the brownies from this link: https://www.allrecipes.com/recipe/10549/best-brownies/")
            print(". . .")
        #if user does not have butter, white sugar, vanilla extract, flour, baking powder, cocoa powder, and salt, then the user does not have the proper ingredients for brownies
        else:
            print("You don't have the proper ingredients to make Brownies")
            print(". . .")

        #if user has butter, white sugar, brown sugar, vanilla extract, flour, salt and chocolate chips, then user has enough ingredients to make chocolate chip cookies
        if ((question2=="yes") and ((question3=="yes") and (question4=="yes")) and ((question5=="yes") and (question6=="yes")) and ((question10=="yes") and (question11=="yes"))):
            print("With these ingredients you could make Chocolate Chip Cookies!")
            print("Find the whole recipe with specific details on how to make the cookies from this link: https://www.allrecipes.com/recipe/10813/best-chocolate-chip-cookies/")
            print(". . .")
        #if user does not have butter, white sugar, brown sugar, vanilla extract, flour, salt and chocolate chips, then user does not have enough ingredients to make chocolate chip cookies
        else:
            print("You don't have the proper ingredients to make Chocolate Chip Cookies")
            print(". . .")

        #if user has butter, brown or white sugar, flour, salt, fruit, cinnamon, and cornstarch, then they have the proper ingredients to make Pie with any type of fruit filling
        if (((question2=="yes") and ((question3 or question4)=="yes")) and ((question6=="yes") and (question10=="yes")) and ((question12=="yes") and (question13=="yes")) and (question14=="yes")):
            print("With these ingredients you could make Pie! Whether it be a Blueberry Pie or Apple Pie, depending on what fruit you have.")
            print("Find the whole recipe with specific details on how to make the pie from this link: https://www.inspiredtaste.net/22662/flaky-pie-crust-recipe/ ")
            print(". . .")
        #if user does not have butter, brown or white sugar, flour, salt, fruit, cinnamon, and cornstarch, then they do not have the proper ingredients to make Pie with any type of fruit filling
        else:
            print("You don't have the proper ingredients to make Pie")
            print(". . .")

        #if user has white sugar, brown sugar, flour, milk, baking powder, salt, chocolate chips, and vegetable oil and/or olive oil and/or canola oil, then they have the proper ingredients to make chocolate chip muffins
        if (((question3=="yes") and (question4=="yes")) and ((question6=="yes") and (question7=="yes")) and ((question8=="yes") and (question10=="yes")) and ((question11=="yes") and (question15=="yes"))):
            print("With these ingredients you could make Chocolate chip muffins!")
            print("Find the whole recipe with specific details on how to make the muffins from this link: https://www.allrecipes.com/recipe/7906/chocolate-chip-muffins/")
            print(". . .")
        #if user does not have white sugar, brown sugar, flour, milk, baking powder, salt, chocolate chips, and vegetable oil and/or olive oil and/or canola oil, then they don't have the proper ingredients to make chocolate chip muffins
        else:
            print("You don't have the proper ingredients to make Chocolate chip muffins")
            print(". . .")

        #if user has butter, white sugar, vanilla extract, flour, baking powder and baking soda, then user has the proper ingredients to make sugar cookies
        if ((question2=="yes") and ((question3=="yes") and (question5=="yes")) and ((question6=="yes") and (question8=="yes")) and (question16=="yes")):
            print("With these ingredients you could make Sugar Cookies!")
            print("Find the whole recipe with specific details on how to make the cookies from this link: https://www.allrecipes.com/recipe/9870/easy-sugar-cookies/")
            print(". . .")
        #if user does not have butter, white sugar, vanilla extract, flour, baking powder and baking soda, then the user does not have the proper ingredients to make sugar cookies
        else:
            print("You don't have the proper ingredients to make Sugar Cookies")
            print(". . .")

# define a function that allows users to view the full list of ingredients from the recipes they want it from
def dessert_ingredients():

    # ask user whether they want to see the full list of ingredients for certain recipes
    more_opts= input("Do you wish to see the ingredients needed for the recipes that you don't have the proper ingredients for? 'yes' or 'no'?")
    print(". . .")

    # if they state yes to wanting to see the full ingredient list for some recipes provided
    if more_opts=="yes":

        # tell user how to input which recipes they want (give specific names of all recipes and tell them to separate different recipes with commas)
        print("The recipes available to see the full ingredients to include the 'Sugar cookies', the 'Vanilla cake', the 'Brownies', the 'Pie', the 'Chocolate chip cookies', and the Chocolate chip 'Muffins'.")
        print("When stating the recipes you want the full ingredients to, please state them as shown above in the quotes, each seperate recipe seperated by commas (no spaces between the commas")
        print(". . .")

        # def diff_opts by asking user which recipes they would like to see the full ingredients for
        diff_opts= input("What recipes would you like to see the ingredients for?: ")
        print(". . .")

        # split the diff_opts string into list, the diff_opts string will be separated by comma
        diff_opts_list = diff_opts.split(",")

        # define i as equal to 0 before the while loop, so that it can be used to iterate through diff_opts_list
        i = 0

        # define SizeofL (size of list) as the length of diff_opts_list
        sizeofL = len(diff_opts_list)

        # make a while loop that continues to loop as long as i is less than the total size of the list (in other words, if i is within diff_opts_list, then the loop continues)
        while i < sizeofL:

            # if an element in the diff_opts_list is equal to "sugar cookies", then show user the ingredients to make sugar cookies
            if (diff_opts_list[i])=="Sugar cookies":
                print("Ingredients to make Sugar Cookies:")
                print("-Flour")
                print("-Baking powder")
                print("-Baking soda")
                print("-Butter")
                print("-White sugar")
                print("-1 egg")
                print("-Vanilla Extract")
                print(". . .")

            # if an element in the diff_opts_list is equal to 'Muffins' or 'Chocolate chip Muffins', then show user the ingredients to make Chocolate chip Muffins
            if (diff_opts_list[i])== ('Muffins' or 'Chocolate chip Muffins'):
                print("Ingredients to make Chocolate Chip Muffin :")
                print("-Flour")
                print("-White sugar")
                print("-Brown sugar")
                print("-Baking powder")
                print("-Salt")
                print("-Milk")
                print("-Vegetable oil")
                print("-1 egg")
                print("-Chocolate chips")
                print(". . .")

            # if an element in the diff_opts_list is equal to 'Vanilla cake', then show user the ingredients to make Vanilla cake
            if (diff_opts_list[i]) == "Vanilla cake":
                print("Ingredients to make Vanilla Cake/Cupcakes:")
                print("-Flour")
                print("-White sugar")
                print("-Baking powder")
                print("-Butter")
                print("-2 eggs")
                print("-Vanilla extract")
                print("-Milk")
                print(". . .")

            # if an element in the diff_opts_list is equal to 'Brownies', then show user the ingredients to make Brownies
            if (diff_opts_list[i]) == "Brownies":
                print("Ingredients to make Brownies:")
                print("-Flour")
                print("-White sugar")
                print("-Cocoa powder")
                print("-Baking powder")
                print("-Salt")
                print("-Butter")
                print("-2 eggs")
                print("-Vanilla extract")
                print(". . .")

            # if an element in the diff_opts_list is equal to 'Pie', then show user the ingredients to make Pie
            if (diff_opts_list[i])== "Pie":
                print("Ingredients to make Pie:")
                print("-Fruit")
                print("-White sugar or Brown Sugar")
                print("-Baking soda")
                print("-Salt")
                print("-Butter")
                print("-Flour")
                print("-Vanilla extract")
                print("-Cinnamon")
                print("-Cornstarch")
                print(". . .")

            # if an element in the diff_opts_list is equal to 'Chocolate chip cookies', then show user the ingredients to make chocolate chip cookies
            if (diff_opts_list[i])=="Chocolate chip cookies":
                print("Ingredients to make Chocolate Chip Cookies:")
                print("-Flour")
                print("-White sugar")
                print("-Brown sugar")
                print("-Baking soda")
                print("-Salt")
                print("-Butter")
                print("-2 eggs")
                print("-Vanilla extract")
                print("-Chocolate chips")
                print(". . .")

            # once an element has gone through the loop, add one to the index, allowing the next element of the diff_opts_list to go through the loop
            i+=1

# def a function that allows user to decide if they want to continue going through the program or not once they have finished going through it once
def dessert_recipes_loop():

    # def cont_or_not (continue or not) variable with "yes", so that the user can begin the program
    cont_or_not="yes"

    # make a while loop so that while cont_or_not does not equal 'no' the program will loop back and repeat the code
    while cont_or_not!="no":

        # add the dessert_recipes function so that it can be incorporated into this program
        dessert_recipes()
        # add the dessert_ingredients function so that it can be incorporated into this program, after the dessert_recipes function has ran
        dessert_ingredients()

        # use variable cont_or_not to ask user if they would like to go through the program again
        cont_or_not = input("Would you like to try again? 'yes' or 'no'?:")

if __name__ == "__main__":
    dessert_recipes_loop()