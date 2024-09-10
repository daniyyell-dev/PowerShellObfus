# PowerShellObfus

**PowerShellObfus** is a tool designed to generate all possible variations of PowerShell command casings. This is important because PowerShell is often used by adversaries for malicious purposes, and varying the casing of commands is a common obfuscation technique. This tool can be used both for obfuscation purposes and for improving detection capabilities.


![Alt text](https://github.com/daniyyell-dev/PowerShellObfus/blob/main/power.png)


## Overview

PowerShell commands are case-insensitive, meaning `powershell`, `PowerShell`, `POWERSHELL`, etc., are all interpreted in the same way. However, adversaries often take advantage of this by using different casing combinations to evade detection by static signature-based tools.

**PowerShellObfus** provides a way to generate all possible casing variations for the string "powershell", enabling both offensive and defensive security practitioners to test and improve their detection capabilities.

## Features

- Generate All Possible Casing Variations
- Flexible Generation Options

## Usage

Clone the repository and run the script using Python:

```sh
git clone https://github.com/yourusername/PowerShellObfus.git
cd PowerShellObfus
python3 powershellobfus.py [options]
```


## Command-Line

    -n <number>: Specify the number of casing variations to generate.
    Example: python3 powershellobfus.py -n 200
    This will generate and display 200 variations.

    -max: Generate all possible combinations of casing variations.
    Example: python3 powershellobfus.py -max

    -h or --help: Show the help message.

## Why Use PowerShellObfus?

    Red Teaming and Offensive Security: Simulate different types of obfuscation used by adversaries to test detection rules.
    Blue Team and Defensive Security: Improve detection by understanding how variations in casing can bypass certain signatures and tools.

## Requirements

    Python 3.x

## Contributing

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.

## Disclaimer

This tool is intended for educational and testing purposes only. Use responsibly and do not engage in illegal activities.
