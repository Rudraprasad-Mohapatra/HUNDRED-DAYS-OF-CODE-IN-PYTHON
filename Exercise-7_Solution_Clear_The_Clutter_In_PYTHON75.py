import os

# os.rename("cluttered/file.txt", "cluttered/6.txt")

files = os.listdir("cluttered")
i=1
for file in files:
    # if file.isnumeric:
    #     os.rename(f"cluttered/{file}", f"cluttered/{file}.png")
    if file.endswith(".png"):
        print(file)
        os.rename(f"cluttered/{file}.png", f"cluttered/{i}.png")
        i = i + 1

