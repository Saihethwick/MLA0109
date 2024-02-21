def is_valid_mapping(mapping, encoded_arr, encoded_s):
    sum_encoded_arr = sum(encoded_arr)
    return sum_encoded_arr == encoded_s

def encode_string(s, mapping):
    encoded_str = "".join(mapping.get(c, '') for c in s)
    return int(encoded_str) if encoded_str else 0

def backtrack(arr, s, mapping, idx, encoded_arr, encoded_s):
    if idx == len(arr):
        return is_valid_mapping(mapping, encoded_arr, encoded_s)
    
    for char in arr[idx]:
        if char not in mapping:
            for digit in range(10):
                if digit not in mapping.values():
                    mapping[char] = str(digit)
                    encoded_arr[idx] = encode_string(arr[idx], mapping)
                    if backtrack(arr, s, mapping, idx + 1, encoded_arr, encoded_s):
                        return True
                    del mapping[char]
    
    return False

def can_encode_strings(arr, s):
    mapping = {}
    encoded_arr = [0] * len(arr)
    encoded_s = encode_string(s, mapping)
    return backtrack(arr, s, mapping, 0, encoded_arr, encoded_s)

# Example usage:
arr = ["SEND", "MORE"]
s = "MONEY"
print("Output:", "Yes" if can_encode_strings(arr, s) else "No")
