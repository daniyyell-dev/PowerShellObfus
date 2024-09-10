# PowerShellObfus

**PowerShellObfus** is a tool designed to generate all possible variations of PowerShell command casings. This is important because PowerShell is often used by adversaries for malicious purposes, and varying the casing of commands is a common obfuscation technique. This tool can be used both for obfuscation purposes and for improving detection capabilities.

## Overview

PowerShell commands are case-insensitive, meaning `powershell`, `PowerShell`, `POWERSHELL`, etc., are all interpreted in the same way. However, adversaries often take advantage of this by using different casing combinations to evade detection by static signature-based tools.

**PowerShellObfus** provides a way to generate all possible casing variations for the string "powershell", enabling both offensive and defensive security practitioners to test and improve their detection capabilities.

## Features

- **Generate All Possible Casing Variations**: Generates all 1024 possible combinations of "powershell" casing.
- **Flexible Generation Options**: Allows users to specify the number of variations to generate or generate all possible combinations.

## Usage

Clone the repository and run the script using Python:

```sh
git clone https://github.com/yourusername/PowerShellObfus.git
cd PowerShellObfus
python3 powershellobfus.py [options]
