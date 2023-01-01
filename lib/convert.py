class Convertor:
  def binaryToDecimal(self, binary_num):
    binary_num = list(str(binary_num))
    value = 0

    for i in range(len(binary_num)):
      digit = binary_num.pop()
        
      if digit == "1":
        value = value + pow(2,i)

    return value
  def octalToDecimal(self, octal_num):
    octal_num = int(octal_num)

    chk = 0
    i = 0
    decimal_num = 0

    while octal_num != 0:
      remainder = octal_num % 10
      if remainder > 7:
        chk = 1
        break

      decimal_num = decimal_num + (remainder * (8 ** i))
      i = i+1
      octal_num = int(octal_num/10)

    if chk == 0:
      return decimal_num
    
    return None
  def hexToDecimal(self, hex_num):
    conversion_table = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "A": 10 , "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}

    hex_num = hex_num.upper()
    decimal = 0

    power = len(hex_num) -1

    for digit in hex_num:
      decimal += conversion_table[digit]*16**power
      power -= 1

    return decimal

  def decimalToBinary(self, decimal_num):
    return bin(int(decimal_num))[2:]
  def decimalToOctal(self, decimal_num):
    return oct(int(decimal_num))[2:]
  def decimalToHex(self, decimal_num):
    return hex(int(decimal_num))[2:]

