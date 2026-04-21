# main.py
import temperature

def main():
    print('=== Temperature Converter ===')
    print('1. Celsius to Fahrenheit')
    print('2. Fahrenheit to Celsius')
    print('3. Celsius to Kelvin')
    choice = int(input('Enter choice (1/2/3): '))

    if choice == 1:
        c = float(input('Enter temperature in Celsius: '))
        f = temperature.celsius_to_fahrenheit(c)
        print(f'{c}°C = {f:.2f}°F')

    elif choice == 2:
        f = float(input('Enter temperature in Fahrenheit: '))
        c = temperature.fahrenheit_to_celsius(f)
        print(f'{f}°F = {c:.2f}°C')

    elif choice == 3:
        c = float(input('Enter temperature in Celsius: '))
        k = temperature.celsius_to_kelvin(c)
        print(f'{c}°C = {k:.2f} K')

    else:
        print('Invalid choice!')

main()
