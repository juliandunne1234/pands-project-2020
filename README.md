# PANDS-PROJECT-2020: Iris Flower Data Set

|Name           |Email         |
|---------------|--------------|
|Julian Dunne   |G00267940@gmit.ie   
______________________________________

## Planning the project

* Understanding the problem statement
    
    * What are the project requirements:
        * Research data set online and write summary about it
        * Download dataset and add to repository
        * Write program called analysis.py that:
            * Output a summary of each variable to single text file
            * Saves a histogram of each vairable to png files
            * Output scatter plot of each pair of variables 

* Pre-requisites to starting project:
    * Setup the Github repository for the project
    * Basic understanding of how to write in Markdown: [Traversy Media](https://www.youtube.com/watch?v=HUBNt18RFbo "Markdown Crash Course")
______________________________________

## Researching the Iris Flower Data Set

The [Iris Flower Data Set](https://en.wikipedia.org/wiki/Iris_flower_data_set) consists of 50 samples taken from three types of Iris flower: Setosa, Virginica and Versicolor. Four measurements were taken from each sample: Sepal length and width and Petal length and width. Based on the combination of these measurements, a linear discriminant model was developed to distinguish the three types of Iris flower from one another.

## Online search for the Iris Flower Data Set

An initial online search to find a suitable CSV file was performed. The dataset that was first used in the code did not have a header row which had to be manually added. This can be found in the initial commits to Github. This URL was changed as part of later commits whereby a dataset was found that already contained a header row: [Iris_Flower_Data_Set.CSV](https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/639388c2cbc2120a14dcf466e85730eb8be498bb/iris.csv)

Issues encounterd when downloading dataset:
* Using the Python Pandas library to import the CSV file the dataset is then written to a text file.

    * The data displayed in the text file by default is truncated. In order to show the full non truncated dataset a search was performed online and a useful example was found which used the Pandas set_option: 
    [Pandas Set_Option](https://stackoverflow.com/questions/25351968/how-to-display-full-non-truncated-dataframe-information-in-html-when-convertin).

## Analysis.py

1. Output a summary of each variable to a single text file. This summary was written to a text file with the analysis performed by using .describe() method which had been used in previous class lectures.

1. Save a Histogram of each variable to png files. Code was written in ipython to create a Histogram for a single variable using the Python Matplotlib library. Using %logstart this code was recorded into an ipython log file and could be easily copied into the analysis.py file and readily used to create Histograms for the remaining variables.

1. Output a scatter plot of each pair of variables. Instead of using the Matplotlib again the Seaborn library was used instead. A youtube search of Seaborn tutorials led to a video on performing [Pair-Plots using Seaborn](https://uk.video.search.yahoo.com/search/video;_ylt=AwrJQ5tSyoleTmoAUhAM34lQ;_ylu=X3oDMTByZmVxM3N0BGNvbG8DaXIyBHBvcwMxBHZ0aWQDBHNlYwNzYw--?p=how+to+download+seaborn+scatter_matrix+function&fr=mcafee&guce_referrer=aHR0cHM6Ly91ay5zZWFyY2gueWFob28uY29tL3NlYXJjaD9mcj1tY2FmZWUmdHlwZT1FMjExR0I4ODVHMCZwPWhvdyt0bytkb3dubG9hZCtzZWFib3JuK3NjYXR0ZXJfbWF0cml4K2Z1bmN0aW9u&guce_referrer_sig=AQAAAJNIBxxFlctk1yWt9jzgraMiq6J37oOazPeqY4f5r48uaZLEPi_asbMdwgHABZetmfG-8FRYXvpWTg1XpVLtmuMmnvvcboyjIj8IwpmIPukz9vkzBO-nQEjeH4UbUA3y6qNUQ1xD1gptiqGa5awBm7cLpi7CEEYN-Xpt2u-0Pt7-&_guc_consent_skip=1586088607#id=1&vid=53d1d380ec502a55cf8e90142459c37f&action=view). The Seaborn Pair-plot between each variable was saved to a single png file with assistance from further youtube videos:
[Save Seaborn Pair-Plot as a png file](https://stackoverflow.com/questions/32244753/how-to-save-a-seaborn-plot-into-a-file).
