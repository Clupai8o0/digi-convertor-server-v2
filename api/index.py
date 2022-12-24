from flask import Flask, jsonify
from lib.convert import Convertor

app = Flask(__name__)

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/convert/<string:fromType>/<string:toType>/<string:value>', methods=['GET'])
def convert(fromType, toType, value):
	BINARY = "Binary"
	DECIMAL = "Decimal"
	OCTAL = "Octal"
	HEXADECIMAL = "Hexadecimal"

	convertor = Convertor()
	decimal = 0

	if fromType == BINARY:
		decimal = convertor.binaryToDecimal(value)
	elif fromType == DECIMAL:
		decimal = value
	elif fromType == OCTAL:
		decimal = convertor.octalToDecimal(value)
	elif fromType == HEXADECIMAL:
		decimal = convertor.hexToDecimal(value)

	if toType == BINARY:
		value = convertor.decimalToBinary(decimal)
	elif toType == DECIMAL:
		value = decimal
	elif toType == OCTAL:
		value = convertor.decimalToOctal(decimal)
	elif toType == HEXADECIMAL:
		value = convertor.decimalToHex(decimal)

	response = jsonify({})

	if value:
		response = jsonify({
			"value": value,
			"msg": f"{fromType} type successfully converted to {toType} type"
		})
	else:
		response = jsonify({
			"value": None,
			"msg": f"There was a problem while converting"
		})

	response.headers.add("Access-Control-Allow-Origin", "*")
	
	return response