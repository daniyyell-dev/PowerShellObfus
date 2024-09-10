import argparse
from itertools import product

def generate_casing_variations(base_string, limit=None):
    combinations = product('01', repeat=len(base_string))
    
    variations = []
    for i, combo in enumerate(combinations):
        if limit and i >= limit:
            break
        variation = ''.join(
            char.upper() if bit == '1' else char.lower()
            for char, bit in zip(base_string, combo)
        )
        variations.append(variation)
    
    return variations

def main():
    
    about = """
    ===== PoWERsheLL_CaSe_InSensiTive ===
    =   by Daniyyell /09/10/2024     ====
    =====================================
    """
    print(about)

    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Generate PowerShell possible casing variations.')
    parser.add_argument('-n', type=int, help='Number of variations to generate.')
    parser.add_argument('-max', action='store_true', help='Generate all possible combinations for obfuscation')
    
    args = parser.parse_args()
    
    # Determine the number of variations to generate
    base_string = 'powershell'
    if args.max:
        limit = None  # No limit if --max is specified
    elif args.n is not None:
        if args.n < 1:
            print("Error: The number of variations must be a positive integer.")
            return
        limit = args.n
    else:
        print("Ooops..: You must specify either -n or -max or -h for help")
        return

    try:
        # Generate variations
        variations = generate_casing_variations(base_string, limit)
        
        # Print variations
        for var in variations:
            print(var)
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
