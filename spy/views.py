from django.shortcuts import render
import serial
# Create your views here.

def home(request):
	ser = serial.Serial('/dev/ttyUSB0')  # open serial port
	ser.baudrate = 57600
	x= ser.read()
	try:
		y=eval(x)
	except:
		y=1
	return render(request,'Home.html', {'x': y})

def wash(request):
	return render(request,'Washrooms.html', {})

def status(request):
	ser = serial.Serial('/dev/ttyUSB0')  # open serial port
	ser.baudrate = 57600
	x= ser.read()		
	return render(request, 'hi.html', {'x': x})