#!/usr/bin/env python3
"""
The Digital Detective - Number Converter
Student: Saksham Jaiswal (USN: 2402608065)
Mission 5: Numbers and Data

This script prompts the user for a decimal integer, converts it into
binary and hexadecimal representations using Python's built-in functions,
and displays the formatted results.
"""

def main():
    print("=" * 45)
    print("   Digital Detective: Number Converter Tool   ")
    print("=" * 45)
    
    user_input = input("Enter a positive decimal integer: ").strip()
    
    try:
        # Convert string input into an integer
        decimal_val = int(user_input)
        
        if decimal_val < 0:
            print("Note: Working with positive numbers as specified in mission guidelines.")
        
        # Built-in conversions
        binary_val = bin(decimal_val)       # returns string prefixed with '0b'
        hex_val = hex(decimal_val).upper()  # returns string prefixed with '0X'
        
        print("\n--- Conversion Results ---")
        print(f"Decimal (Base 10):     {decimal_val}")
        print(f"Binary (Base 2):       {binary_val} (or raw: {bin(decimal_val)[2:]})")
        print(f"Hexadecimal (Base 16): 0x{hex(decimal_val)[2:].upper()}")
        print("=" * 45)
        
    except ValueError:
        print(f"Error: '{user_input}' is not a valid decimal integer.")

if __name__ == "__main__":
    main()
