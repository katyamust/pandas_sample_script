import pandas as pd

filename  = "big_file.csv"
chunk_size = 10000 #lines

list_of_dfs = []
reader = pd.read_csv(filename, low_memory=False, chunksize=chunk_size)
for chunk in reader:
    list_of_dfs.append(chunk)
    # df = df.append(chunk) # never do that! this is very inefficient

print('Concatenating... list of dfs')
df = pd.concat(list_of_dfs, ignore_index=True)


