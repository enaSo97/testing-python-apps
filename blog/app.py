from blog import Blog
from post import Post

MENU_PROMPT = 'Enter "c" to create a blogs, "l" to read one, "p" to create a post, "q" to quit.'

blogs = dict() #blog_name : Blog object


def menu():
    #show the user the available blogs
    #let the user make  choice
    #Do something with that choice
    #eventually exit
    print_blogs()
    selection = input(MENU_PROMPT)
    while selection != q:
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()

        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()
        selection = input(MENU_PROMPT)

def print_blogs():
    #print available blogs
    for key, blog in blogs.items(): #(blog_name, BLog)
        print("- {}".format(blog))


def ask_create_blog():
    author = input('Please enter blog name: ')
    title = input('Please enter blog title ')
    blogs[title] = Blog(title, author)


def ask_read_blog():
    #title = input('Please enter the blog title:')
    #for key, blog in blogs.item():
    #    if (blog.title == title):
    pass

def ask_create_post():
    #which = input('Please enter the blog title you want to create a post for: ')
    #if which in
    pass