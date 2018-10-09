import csv
import re

with open('Data/airbnb_listings.csv', 'r') as csvfile:
    rdr= csv.reader(csvfile)
    for r in rdr:
        with open("Data/listings_separated/"+re.sub('\W+','', str(r[4])), "w") as result:
            wtr = csv.writer(result)
            wtr.writerow((r[5], r[6], r[7], r[9], r[11], r[14]))