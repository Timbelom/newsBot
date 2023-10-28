def clear(file_path):    
    try:
        with open(file_path, "w") as file:
            pass 
        print(f"Contents of '{file_path}' have been cleared.")
    except Exception as e:
        print(f"An error occurred: {e}")
