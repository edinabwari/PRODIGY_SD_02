Temp_options = ('a', 'b', 'c')

while True:
    print()
    print(' TEMPERATURE SCALE LIST: ')
    print('a = Fahrenheit')
    print('b = Celsius')
    print('c= Kelvin')
    print()

    user_input = input('Choose the temperature scale: ')
    print()

    if user_input in Temp_options:
        break
    else:
        print('OPTION NOT AVAILABLE. CHOOSE OPTIONS FROM THE LIST.')

if user_input == 'a' :
    print()
    Temp_value_in_Fahrenheit = input('Enter the temperature value of Fahrenheit : ')
    converted_temp_c = (int(Temp_value_in_Fahrenheit) - 32) * 5/9
    converted_temp_k = converted_temp_c + 273.1
    print()
    print(f"The converted temperature from {Temp_value_in_Fahrenheit} Fahrenheit to Celsius is {converted_temp_c} ")
    print(f"The converted temperature from {Temp_value_in_Fahrenheit} Fahrenheit to Kelvin is {converted_temp_k} ")

elif user_input == 'b':
     print()
     Temp_in_Celsius = input('Enter the temperature value in Celsius: ')
     converted_temp_f = (int(Temp_in_Celsius) * 9/5) + 32
     converted_temp_k = int(Temp_in_Celsius) + 273.15
     print()
     print(f"The converted temperature from {Temp_in_Celsius} Celsius to Fahrenheit  is {converted_temp_f} ")
     print(f"The converted temperature from {Temp_in_Celsius} Celsius to Kelvin is {converted_temp_k} ")

elif user_input == 'c':
    print()
    Temp_value_in_Kelvin = input('Enter the temperature value in Kelvin: ')
    converted_temp_c = int(Temp_value_in_Kelvin) - 273.15
    converted_temp_f = (int(converted_temp_c) * 9/5) + 32
    print()
    print(f"The converted temperature from {Temp_value_in_Kelvin} Celsius to Fahrenheit  is {converted_temp_f} ")
    print(f"The converted temperature from {Temp_value_in_Kelvin} Celsius to Kelvin is {converted_temp_c} ")


