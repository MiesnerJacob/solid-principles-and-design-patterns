import math

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be equal to zero.")
        self.__numerator = numerator
        self.__denominator = denominator
        
    def numerator(self):
        return self.__numerator

    def denominator(self):
        return self.__denominator

    def add(self, other):
        return Fraction(
            numerator=(self.__numerator * other.__denominator) + (other.__numerator * self.__denominator),
            denominator=self.__denominator * other.__denominator
        )

    def subtract(self, other):
        return Fraction(
            numerator=(self.__numerator * other.__denominator) - (other.__numerator * self.__denominator),
            denominator=self.__denominator * other.__denominator
        )

    def multiply(self, other):
        return Fraction(
            numerator=self.__numerator * other.__numerator,
            denominator=self.__denominator * other.__denominator
        )

    def divide(self, other):
        if other.__numerator == 0:
            raise ValueError("Your entered fraction cannot have a numerator equal to zero.")
        return Fraction(
            numerator=self.__numerator * other.__denominator,
            denominator=self.__denominator * other.__numerator
        )

    def simplify(self):
        gcd = math.gcd(self.__numerator, self.__denominator)
        return Fraction(
            numerator=self.__numerator // gcd,
            denominator=self.__denominator // gcd
        )
    
    def __str__(self):
        return f"{self.__numerator}/{self.__denominator}"


# Test your implementation
fraction1 = Fraction(1, 4)
fraction2 = Fraction(1, 2)

fraction3 = fraction1.add(fraction2)
print(fraction3)  # Should output "6/8"

fraction4 = fraction3.simplify()
print(fraction4)  # Should output "3/4"