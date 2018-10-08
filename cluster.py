import csv
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np

testdata = ['Modern 1bedroom app. near city cent', 'a modern, spacious and clean ground floor appartment near the city center and close to the airport. Hotspots like the Vondelpark and Leidseplein are just around the corner.', 'I have a modern and clean ground floor apartment (no steep stairs are rare in amsterdam) in \'Amsterdam West\'. (just a few minutes from the Vondelpark and City Center)  You can use my bike (the best way to get around in Amsterdam) but the tramstop (7&17 tram) is only a few steps from my house,  which takes you into the center of Amsterdam within 10 min. Parking isn\'t free in front of my house but there are free parking possibilities nearby. Just around the corner there is a very long  "shopping" street the "Kinkerstraat" for all your daily needs and more. My apartment is only 20 min. from the airport or central station, There are two really good coffee shops within 2 min but I don’t allow smoking inside. You can smoke in the backyard but not before 11am or after 6pm because the smell bothers my upstairs neighbors. Off course you can smoke 24/7 in front of the house or anywhere outside. The Vondelpark and Rembrandtpark are just around the corner:)  Main attractions like the Leidseplein, ', 'a modern, spacious and clean ground floor appartment near the city center and close to the airport. Hotspots like the Vondelpark and Leidseplein are just around the corner. I have a modern and clean ground floor apartment (no steep stairs are rare in amsterdam) in \'Amsterdam West\'. (just a few minutes from the Vondelpark and City Center)  You can use my bike (the best way to get around in Amsterdam) but the tramstop (7&17 tram) is only a few steps from my house,  which takes you into the center of Amsterdam within 10 min. Parking isn\'t free in front of my house but there are free parking possibilities nearby. Just around the corner there is a very long  "shopping" street the "Kinkerstraat" for all your daily needs and more. My apartment is only 20 min. from the airport or central station, There are two really good coffee shops within 2 min but I don’t allow smoking inside. You can smoke in the backyard but not before 11am or after 6pm because the smell bothers my upstairs neighbors. Of', "It's a quiet neigbourhood, with shops and restaurants around the corner. Just a few minutes from The Vondelpark and only 10 minutes from the city center. Also only 20 minutes from te airport!! If you like you can even use my bike (best way to get around in Amsterdam:-) Otherwise I can give you (chargeable) cards to use for the public transport (trains, trams and busses) If I have time I can pick you up or drive you to the airport......", "Only 20 minutes from te airport!! If I have time I can pick you up or drive you to the airport......Otherwise it's only a short trip by train. If you like you can use my bike (best way to get around in Amsterdam:-) Otherwise I can give you (chargeable) cards to use for the public transport (trains, trams and busses) The stops are just 1 min from my appartment.....", "House rules are simple. Keep it clean and don't break anything:-) When you smoke please do this outside (I have a small garden where you can relax and sit) but above all, enjoy Amsterdam!!!"]

data = ""
for element in testdata:
    data += str(element)
data = [data]

vectorizer = CountVectorizer()
vectorizer.fit(data)
vector = vectorizer.transform(data)
print(vector.toarray())
plt.scatter()



#with open('Data/airbnb_listings_clean.csv', 'r') as csvfile:
#   data=csv.reader(csvfile)
#   for row in data:
#       print(row)
#       vectorizer = CountVectorizer()
#       vectorizer.fit(row)
#       print(vectorizer.vocabulary_)
