from blog import Blog
from post import Post

MENU_PROMPT = 'Enter "c" to create a blogs, "l" to read one, "p" to create a post, "q" to quit.'
POST_TEMP = '''
          --- {} ---
          
          {}
          '''

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
    title = input('Please enter blog title ')
    author = input('Please enter your name: ')
    blogs[title] = Blog(title, author)


def print_posts(blog):
    for post in blog.posts:
        print_post(post)

def print_post(post):
    print(POST_TEMP.format(post.title, post.content))

def ask_read_blog():
    title = input('Please enter the blog title:')
    print_posts(blogs[title])
    pass

def ask_create_post():
    #which = input('Please enter the blog title you want to create a post for: ')
    #if which in
    pass