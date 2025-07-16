# problem

I have processed data already, yet new data has come. 
I would like to only get the recent data(from a few days ago)

# solution - pandas

1. Get the end date
2. get the 'KEY'(works like key and foreign key in the db) values from the main.csv to a list
3. For every df get the row values where the 'PARENT_KEY' `.isin()` keys list
4. save the files


