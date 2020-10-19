# luhn
Uses Luhn algorithm to validate and generate valid credit card numbers.

The generator.txt file is written in Rexx and works with a mainframe system.

The key to create a number that satisfies the Luhn algorithm is to implement its checksum formula, in which the last digit, also known as the check digit, must match the formula's calculations. In the generator code, the algorithm is reversed engineered and instead utilizes the checksum formula to generate the check digit, resulting in a number that satisfies the Luhn algorithm.

(Source: Wikipedia)
![Check digit example](luhn-wiki.png)
