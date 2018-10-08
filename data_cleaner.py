import csv

with open('Data/airbnb_listings.csv', 'r') as csvfile:
    rdr= csv.reader(csvfile)
    with open('Data/airbnb_listings_clean.csv', 'w') as result:
        wtr= csv.writer(result)
        for r in rdr:
            wtr.writerow((r[4], r[5], r[6], r[7], r[9], r[11], r[14]))
