import os

# Set the path to the folder where the files will be generated
path = "C:\\Users\\mikec_g1kgiu8\\OneDrive\\Desktop\\CS 5322\\TopicModeling\\Articles 2.0"

# Loop through 400 times to create 400 .txt files
for i in range(1, 401):
    # Generate the filename (e.g. 1.txt, 2.txt, etc.)
    filename = str(i) + ".txt"
    # Generate the full file path
    filepath = os.path.join(path, filename)
    # Create the file and write some data to it
    with open(filepath, "w") as f:
        f.write("This is file number " + str(i))