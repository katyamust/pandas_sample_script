# pandas samples

Repo contains code samples working with pandas DataFrame, so  one can use it wihtout seaching stackoveflow over and over again
 
Loading from csv format, initial cleansing and histogram

Data for analysis come in often in csv format but contain different object such as text, numbers, GUIDs, html css snippets, etc

This code snippets load various type of csv files into pandas DataFrame and can print out statistical analysis for various columns of DataFrame



Generally pansdas.Series is way slower than numpy series in a range of operaiton. so extract pandas_serie.values ( which is type numpy series) to fast processing of pandas columns
