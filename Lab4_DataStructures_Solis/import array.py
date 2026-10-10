
from array import array


number_array = array.array('i', [sys_config["base_seed"],
sys_config["vector_dim"], 100])
print(f"Integer Array: {number_array}")

print("\nAttempting to append a string...")
try:
    number_array.append("invalid")
except TypeError as error_msg:
    print(f"TypeError: {error_msg}")