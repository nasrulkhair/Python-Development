"""
#MANUALLY TESTING A DATA 

# 1. VALIDATING A DATA PIPELINES AT "CHECKPOINTS"

# Extract and transform tax_data
raw_tax_data = extract("raw_tax_data.csv")
clean_tax_data = transform(raw_tax_data)

# Check the shape of the raw_tax_data DataFrame, compare to the clean_tax_data DataFrame
print(f"Shape of raw_tax_data: {raw_tax_data.shape}")
print(f"Shape of clean_tax_data: {clean_tax_data.shape}")

# ___________________

raw_tax_data = extract("raw_tax_data.csv")
clean_tax_data = transform(raw_tax_data)
load(clean_tax_data, "clean_tax_data.parquet")

print(f"Shape of raw_tax_data: {raw_tax_data.shape}")
print(f"Shape of clean_tax_data: {clean_tax_data.shape}")

# Read in the loaded data, observe the head of each
to_validate = pd.read_parquet("clean_tax_data.parquet")
print(clean_tax_data.head(3))
print(to_validate.head(3))

# _______________________
# checking the equality of the data

raw_tax_data = extract("raw_tax_data.csv")
clean_tax_data = transform(raw_tax_data)
load(clean_tax_data, "clean_tax_data.parquet")

print(f"Shape of raw_tax_data: {raw_tax_data.shape}")
print(f"Shape of clean_tax_data: {clean_tax_data.shape}")

to_validate = pd.read_parquet("clean_tax_data.parquet")
print(clean_tax_data.head(3))
print(to_validate.head(3))

# Check that the DataFrames are equal
print(to_validate.equals(clean_tax_data))




# 2. TESTING A DATA PIPELINED END-TO-END

# Trigger the data pipeline to run three times
for attempt in range(0, 3):
	print(f"Attempt: {attempt}")
	raw_tax_data = extract("raw_tax_data.csv")
	clean_tax_data = transform(raw_tax_data)
	load(clean_tax_data, "clean_tax_data.parquet")
	
	# Print the shape of the cleaned_tax_data DataFrame
	print(f"Shape of clean_tax_data: {clean_tax_data.shape}")
    
# Read in the loaded data, check the shape
to_validate = pd.read_parquet("clean_tax_data.parquet"
                              
# ___________________________________________________________________________
#UNIT TESTING A DATA PIPELINE WITH ASSERT

# 1. Validating a data pipeline with assert
# 2. Writing unit test with pytest
# 3. Creating fixtures with pytest
# 4. Unit testting a data pipeline with fixtures

"""