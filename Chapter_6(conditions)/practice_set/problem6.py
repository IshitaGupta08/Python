#WAP to find out whether a given post is talking about "Ishita" or not

# post = "Ishita is a good girl"
post = input("Enter the post: ")

if("Ishita".lower() in post.lower()):
    print("This post is talking about Ishita")
else:
    print("Ishita is not in a post")