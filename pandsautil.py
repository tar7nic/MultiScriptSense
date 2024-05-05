# Credits to -> https://github.com/Pun-it
import os
import pandas as pd

def making_datasets():
    # Load the file
    files = os.listdir("Relative_Path")
    # Getting all the files that end with .txt
    listofnames = [x for x in files if x.endswith(".txt")]
    print(listofnames)
    # List initialized for storing the names of the created csv files
    listofcsv = []
    # Iterating thru all the text files names
    for name in listofnames:
        # splitting the file name into two halves, before and after '.' , 
        # here we are taking the first part as that contains the name of the file.  
        newname = name.split('.')[0]

        # opening the text file
        with open(f'{name}',encoding= 'utf-8') as f :
            # readign all the lines
            lines = f.readlines()

        #storing all the lines by separating them and storing them in a list.
        line_feats = [line.strip() for line in lines]

        # A dict initialized to store each text with it's corresponding index
        line_dict = {}

        # Going thru all the lines
        for i in line_feats:
            # The line had text and numbers separated by "\t"[tab]

            # Getting the index
            a = i.split("\t",1)[0]
            # Getting the text
            b = i.split("\t",1)[1]
            # Appending the text in the dict with te corresponding index
            line_dict[int(a)] = b

        # Creating a dataframe from the dict
        heheheha = pd.DataFrame.from_dict(line_dict,'index')
        # Renaming the column that contains text to "text"
        heheheha = heheheha.rename(columns= {0 : "Text"})
        # Creating a new columns and populating it with thename of the language
        heheheha['Language'] = f"{newname}"
        # Saving the file with the corresponding_name.csv
        heheheha.to_csv(f'{newname}.csv')
        # Opening the data frame
        new_ds = pd.read_csv(f"{newname}.csv")
        # Appending the DataFrame to a list , so it be used lated for concatination
        listofcsv.append(new_ds)
    
    # Concatinating the datasets and creating a big dataset
    data = pd.concat(listofcsv,axis = 0)
    # Saving to csv
    data.to_csv("knownData.csv")
    # Adding a "Type" and populating it too 
    data['Type'] = "known"
    # Saving : )
    data.to_csv("knownDataWithLang.csv")
    # Dropping a Column
    data = data.drop(['Language'],axis = 1)
    # Saving ": )" 
    data.to_csv("knownDataWithOutLang.csv")

if __name__ == "__main__":
    making_datasets()
