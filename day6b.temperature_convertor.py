# temperature convertor

'''
Convert Celsius to Fahrenheit.
- `F = ((9/5) * C) + 32`
Convert Fahrenhiet to Celsius
- `C = (F-32)*(5/9)`
'''
def celsius_to_fahrenheit(temp):
  return (((9/5) * temp) + 32)


def fahrenheit_to_celsius(temp):
  return ((temp - 32) * (5/9))


print(celsius_to_fahrenheit(30))
print(fahrenheit_to_celsius(86))
