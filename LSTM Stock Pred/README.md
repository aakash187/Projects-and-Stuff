*In this implementation of a recurrent neural network, 
I took a stock's price points for the last 2 weeks, 
implemented an RNN to feed on the last 120 price points of the data,
and then predicted the next day's prices, one point at a time.*

* I used the yfinance module to get the data from the internet
so that there is no need to download data again and again. 
It enables us to download stock data flexibly 
right from the 2 minute interval to the moth long intervals.

* I only used the closing price in this case as the results I got with this one were pretty satisfactory.
Then I used a standard scaler in order to normalise the prices because
scaling is important in order to get better results in this case, I have found.

* I then proceeded to stack the previous 120 price points together
in order to provide them as an input to the RNN

* The RNN was made up of 4 layers, each having 150 neurons and a dropout of 0.2 which were tuned to get a satisfactory result
* After training, I tested it on the test set and plotted the predicted price vs actual stock price, which returned an MSE of 0.69
at a price range near 550, which is less than 1% of the price.

