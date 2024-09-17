import pandas as pd

# Path to the HDF5 file
hdf5_file_path = 'memristor_data.h5'

# Open the HDF5 file
with pd.HDFStore(hdf5_file_path, mode='r') as store:
    # List all keys (datasets) in the HDF5 file
    print("Datasets available in the HDF5 file:")
    for key in store.keys():
        print(f" - {key}")

    # Load and inspect the data for each key
    print("\nInspecting data from each key:")
    for key in store.keys():
        print(f"\nKey: {key}")

        # Get information about the stored object
        storer = store.get_storer(key)
        print(f"Data type of stored object: {type(storer)}")

        # Check if the object is a Frame (DataFrame) or Table
        if isinstance(storer, pd.io.pytables.FrameFixed):
            try:
                # Load the dataset into a pandas DataFrame
                df = store.get(key)
                print("\nColumns in the DataFrame:")
                print(df.columns.tolist())  # Print all column names
                print("\nFirst few rows of the DataFrame:")
                print(df.head())  # Display the first few rows of the dataset
            except Exception as e:
                print(f"Error loading data for {key}: {e}")
        elif isinstance(storer, pd.io.pytables.Table):
            try:
                # If it's a Table, load it as a DataFrame
                df = store.select(key)
                print("\nColumns in the DataFrame:")
                print(df.columns.tolist())  # Print all column names
                print("\nFirst few rows of the DataFrame:")
                print(df.head())  # Display the first few rows of the dataset
            except Exception as e:
                print(f"Error loading data for {key}: {e}")
        else:
            print(f"The object under {key} is not a pandas DataFrame or Table.")
