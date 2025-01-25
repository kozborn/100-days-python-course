# try:
#
#   something that might cause an exception
#
# except:
#
#    Do this if there was an exception
#
# else:
#
#    Do this if there were no exceptions
#
# finally:
#
#    at the end do this
#






# try:
#     with open('data.txt', 'r') as file:
#         file.read()
# except Exception as error:

# try:
#     file = open("input.txt", "r")
# except Exception as error:
#     file = open("input.txt", "w")
# else:
#     file.readline()
# finally:
#     print("Done")

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]


def count_likes(posts):

    total_likes = 0
    for post in posts:
        try:
            total_likes = total_likes + post['Likes']
        except KeyError:
            pass


    return total_likes


print(count_likes(facebook_posts))


    # print(error)