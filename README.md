# PANDS-PROJECT-2020: Iris Flower Data Set

|Name           |Email         |
|---------------|--------------|
|Julian Dunne   |G00267940@gmit.ie   
______________________________________

## Step 1: Planning the project
* Defining the problem statement
    *  Understand the project requirements
* Pre-requisites
    * Setup the Github repository for the project
    * Basic knowledge of how to write in Markdown: [Traversy Media](https://www.youtube.com/watch?v=HUBNt18RFbo "Markdown Crash Course")
______________________________________

## Step 2: Researching the Iris Flower Data Set

<p>The Iris Flower Data Set consists of 50 samples taken from three types of Irs flower: Setosa, Virginica and Versicolor. Four measurements were taken from each sample: Sepal length and width and Petal length and width. Based on the combination of these measurements, a linear discriminant model was developed to distinguish the three types of Iris flower from one another.<p>

* Summary above gathered from Wikipedia:
[Iris Flower Data Set](https://en.wikipedia.org/wiki/Iris_flower_data_set)

<p>Further reading & links:<p>

[Pattern Recognition](https://www.theseus.fi/bitstream/handle/10024/64785/yang_yu.pdf?sequence=1)

[Exploratory Data Analysis](https://medium.com/analytics-vidhya/exploratory-data-analysis-iris-flower-dataset-a21c368a1f4)


Research videos on youtube and summarise what was learned:
* Link 5

<p>Complete this intro before final commit
______________________________________

## Step 3: Downloading the Iris Flower Data Set

<p>Find a suitable Iris Flower Data Set CSV file online and import using Python Pandas.

Issues to resolve included the following:
* ~~CSV file found online was missing a header row which includes the column detail~~ updated code to include a different URL for data set that already has header column.
* Once imported to Pandas and written to a text file it truncates the data.
    * Display text in non-truncated form.
* ~~Read modifed text file using Pandas and print full non-truncated version in Python editor~~ Remove code that is not in project scope.
<p>

## Step 4:Writing Analysis.py

1. Output a summary of each variable to a single text file. Write to a file named iris_variable_summary.txt using the .describe() method.

1. Save a Histogram of each variable to png files. Code was written in ipython to create a Histogram for a single variable. Using %logstart this code was recorded in script format which could then be copied into the analysis.py file. and used to create Histograms for the remaining variables.

1. Output a scatter plot of each pair of variables. 
A video found on youtube showing how to perform pairplots using python Seaborn
https://uk.video.search.yahoo.com/search/video;_ylt=AwrJQ5tSyoleTmoAUhAM34lQ;_ylu=X3oDMTByZmVxM3N0BGNvbG8DaXIyBHBvcwMxBHZ0aWQDBHNlYwNzYw--?p=how+to+download+seaborn+scatter_matrix+function&fr=mcafee&guce_referrer=aHR0cHM6Ly91ay5zZWFyY2gueWFob28uY29tL3NlYXJjaD9mcj1tY2FmZWUmdHlwZT1FMjExR0I4ODVHMCZwPWhvdyt0bytkb3dubG9hZCtzZWFib3JuK3NjYXR0ZXJfbWF0cml4K2Z1bmN0aW9u&guce_referrer_sig=AQAAAJNIBxxFlctk1yWt9jzgraMiq6J37oOazPeqY4f5r48uaZLEPi_asbMdwgHABZetmfG-8FRYXvpWTg1XpVLtmuMmnvvcboyjIj8IwpmIPukz9vkzBO-nQEjeH4UbUA3y6qNUQ1xD1gptiqGa5awBm7cLpi7CEEYN-Xpt2u-0Pt7-&_guc_consent_skip=1586088607#id=1&vid=53d1d380ec502a55cf8e90142459c37f&action=view

Another web search was required to find a way to save seaborn.png files:
https://stackoverflow.com/questions/32244753/how-to-save-a-seaborn-plot-into-a-file




______________________________________
#### EVERYTHING BELOW WILL BE REMOVED DURING FINAL GIT PUSH - ONLY USED FOR REFERENCE WHEN WRITING IN MARKDOWN

<!-- Italics -->
*This text* is Italic

\*This text\* is not Italic

_This text is also_ Italic

<!-- Strong -->
**This text** is in bold

__This text__ is in bold

<!-- Strikethrough -->
~~This text~~ is strikethrough

#Use below line to seperate content

---
___

<!-- Blockquote -->
> This is a quote

<!-- Links -->
[Traversy Media](https://www.youtube.com/watch?v=HUBNt18RFbo "Mardown Crash Course")

<!-- UL -->
* Item 1
* Item 2
* Item 3
    * Nested Item 1
    * Nested Item 2

<!-- OL -->
1. Item 1
1. Item 2
1. Item 3

<!-- Inline Code Block-->
`<p> This is a paragraph <p>`

<!-- Images -->
![Markdown Logo](https://xxxxx)

<!-- Github Markdown -->
<!-- Code Blocks -->

```python
def add(num1, num2):
    return num1 + num2
```


<!-- Task Lists -->
* [x] Task 1
* [x] Task 2
* [ ] Task 3






