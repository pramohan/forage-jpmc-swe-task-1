import unittest
from client3 import getDataPoint
from client3 import getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      correct_output = (quote['stock'], 
                        quote['top_bid']['price'], 
                        quote['top_ask']['price'], 
                        (quote['top_bid']['price'] + quote['top_ask']['price']) / 2)
      actual_output = getDataPoint(quote)
      
      self.assertEqual(correct_output, actual_output)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      correct_output = (quote['stock'], 
                        quote['top_bid']['price'], 
                        quote['top_ask']['price'], 
                        (quote['top_bid']['price'] + quote['top_ask']['price']) / 2)
      actual_output = getDataPoint(quote)
      
      self.assertEqual(correct_output, actual_output)
  """ ------------ Add more unit tests ------------ """
  
  def test_getRatio_nonZeroValues(self):
    prices = [(121.2, 121.68), (119.2, 121.68), (120.48, 117.87)]
    
    for price1, price2 in prices:
      correct_output = price1 / price2
      actual_output = getRatio(price1, price2)
      
      self.assertEqual(correct_output, actual_output)
      
  def test_getRatio_zeroPriceB(self):
    prices = [(121.2, 0), (119.2, 0), (120.48, 0)]
    
    for price1, price2 in prices:
      correct_output = None
      actual_output = getRatio(price1, price2)
      
      self.assertEqual(correct_output, actual_output)
      
  def test_getRatio_zeroPriceA(self):
    prices = [(0, 121.2), (0, 119.2), (0, 120.48)]
    
    for price1, price2 in prices:
      correct_output = 0
      actual_output = getRatio(price1, price2)
      
      self.assertEqual(correct_output, actual_output)

if __name__ == '__main__':
    unittest.main()
