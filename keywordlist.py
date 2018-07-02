import keyword
key=input("Enter any word to check it's a keyword or not")

if keyword.iskeyword(key):
    print("it's a keyword--->>",key)
else:
    print("it's not a keyword")
    print("the list of all the keywords---->>\n", keyword.kwlist)


# count=0
# for i in keyword.kwlist:
#     if i==key:
#         count = 1
#         print("keword match")
#
# if count==0:
#     print(keyword.kwlist)

