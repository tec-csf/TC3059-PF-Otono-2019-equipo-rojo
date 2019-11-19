# Antony Adrián Morales Rosas
# V1.0.0
# Dataset Creator

import sys
from progress.bar import Bar
from random import randint
from faker import Faker
fake = Faker()

# Setting number of data in the files
nUsers = 2000
nPosts = 3000
nFollows = 1000
nLikes = 1000

# Setting a loading UserCSV toolbar
barUser = Bar('Genarating UserCSV.csv', max=nUsers, suffix='%(percent)d%%')
# Creating and open to write a .csv file for UserCSV
f = open("UserCSV.csv", "w")
# Writing the first line
f.write("id,username,mail,password,name,location,description,verified,created_at,birthday,lang,profile_banner_url,profile_img_url\n")
for i in range(0, nUsers):
    barUser.next()
    f.write(str(i) + "," + fake.user_name() + "," + fake.email() + "," + fake.password(length=10, special_chars=False) + "," + fake.name() + "," + fake.country() + "," + fake.sentence(nb_words=10) + "," +
            str(fake.boolean(chance_of_getting_true=80)) + "," + fake.iso8601(tzinfo=None, end_datetime=None) + "," + fake.iso8601(tzinfo=None, end_datetime=None) + ",EN," + fake.image_url() + "," + fake.image_url() + "\n")
f.close()
barUser.finish()


# Setting a loading PostsCSV toolbar
barPost = Bar('Genarating PostsCSV.csv', max=nPosts, suffix='%(percent)d%%')
# Creating and open to write a .csv file for PostsCSV
f = open("PostsCSV.csv", "w")
f.write("id,text,created_at\n")
for i in range(0, nPosts):
    barPost.next()
    f.write(str(i) + "," + fake.sentence(nb_words=17) + "," +
            fake.iso8601(tzinfo=None, end_datetime=None) + "\n")
f.close()
barPost.finish()


# Setting a loading FOLLOWSCSV toolbar
barFollow = Bar('Genarating FOLLOWSCSV.csv',
                max=nFollows, suffix='%(percent)d%%')
# Creating and open to write a .csv file for FOLLOWSCSV
f = open("FOLLOWSCSV.csv", "w")
f.write("from_user, to_user, date\n")
for i in range(0, nFollows):
    barFollow.next()
    rand1 = randint(0, nUsers)
    rand2 = randint(0, nUsers)
    f.write(str(rand1) + "," + str(rand2) + "," +
            fake.iso8601(tzinfo=None, end_datetime=None) + "\n")
f.close()
barFollow.finish()

# Setting a loading CREATEDCSV toolbar
barCreated = Bar('Genarating CREATEDCSV.csv',
                 max=nPosts, suffix='%(percent)d%%')
# Creating and open to write a .csv file for CREATEDCSV
f = open("CREATEDCSV.csv", "w")
f.write("post_id,user_id,creation_date\n")
for i in range(0, nPosts):
    barCreated.next()
    rand1 = randint(0, nUsers)
    rand2 = randint(0, nUsers)
    f.write(str(rand1) + "," + str(rand2) + "," +
            fake.iso8601(tzinfo=None, end_datetime=None) + "\n")
f.close()
barCreated.finish()

# Setting a loading LIKESCSV toolbar
barLikes = Bar('Genarating LIKESCSV.csv', max=nLikes, suffix='%(percent)d%%')
# Creating and open to write a .csv file for LIKESCSV
f = open("LIKESCSV.csv", "w")
f.write("user_id,post_id,like_date\n")
for i in range(0, nLikes):
    barLikes.next()
    rand1 = randint(0, nUsers)
    rand2 = randint(0, nUsers)
    f.write(str(rand2) + "," + str(rand1) + "," +
            fake.iso8601(tzinfo=None, end_datetime=None) + "\n")
f.close()
barLikes.finish()
