### Exercise 00 : Line chart

Exercise 00

Line chart

Turn-in directory : ex00/

Files to turn in : 00_line_chart.ipynb

Allowed functions : import pandas as pd, import sqlite3

Today, you will work with the same datasets that you used on the previous day.

We will try to understand the data about how the students of the educational company
behave. You will use Pandas and SQL again to sharpen your skills and use various
libraries for data visualization in Python: Matplotlib, Seaborn, and Plotly.

As usual, let us start with something simple. If you have not drawn a graph in Python,
it is time to do it for the first time.

Remember how we analyzed the newsfeed page? Did you wonder how often the page
was visited in time?

* make a connection to the [database](https://drive.google.com/open?id=1zQ8AR2Ry3ajzB3UZO1Sfk3xtDJlzQF2M) (it is the same as the previous day)
* run a query that gets the datetime from the pageviews table, selecting only the
users and not the admins
* using Pandas, create a new dataframe where the visits are counted and grouped by
date
* using Pandas method .plot(), create a graph
    * the size of the font should be 8
    * the size of the figure is (15,8)
    * the graph must have the title Views per day
    * notice the rotation of xticks on the graph below
* close the connection to the database

### Exercise 01 : Line chart with styles

Exercise 01

Line chart with styles

Turn-in directory : ex01/

Files to turn in : 01_line_chart_styles.ipynb

Allowed functions : import pandas as pd, import sqlite3

Cool! Remember that we have the data about the commits? Wouldn’t it be cool to
draw both of the metrics in time on the same graph? What if we will see some patterns?

You need to create exactly the same graph as below (both values and style):

* analyze only the users and not the admins
* analyze only the dates when there were both views and checker commits
* use size of the font should be 8
* the size of the figure is (15,8)
* at the end of your Jupyter Notebook create a markdown cell and insert the question:
“How many times was the number of views larger than 150?” Insert: “The answer
is ___”. Put the number in the text instead of the underline.

### Exercise 02 : Bar

Exercise 02

Bar

Turn-in directory : ex02/

Files to turn in : 02_bar_chart.ipynb

Allowed functions : import pandas as pd, import sqlite3

We have another question for you to answer: when do our users usually commit the
labs: in the night, morning, afternoon, or evening? And how has it changed over time?

Do what you need to do to create a graph like this:

* analyze only the users and not the admins
* the fontsize and the figsize are still the same
* night is from 0:00:00 to 03:59:59, morning is from 04:00:00 to 09:59:59, afternoon
is from 10:00:00 to 16:59:59, evening is from 17:00:00 to 23:59:59
* choose a palette that you really enjoy, you do not have to replicate it from the graph
  above
* at the end of your Jupyter Notebook, create a markdown cell and insert the ques-
  tions:
  * “When do our users usually commit the labs: in the night, morning, afternoon,
  or evening?”, the answer is the two most common periods.
  * Which day has:
    * the most number of commits
    * and at the same time, the number of commits in the evening is higher than in the afternoon?

The answer is the date of that day.

### Exercise 03 : Bar charts

Exercise 03

Bar charts

Turn-in directory : ex03/

Files to turn in : 03_bar_charts.ipynb

Allowed functions : import pandas as pd, import sqlite3

What if the average number of commits is different when it is a working day or
weekend?

Do what you need to do to create a graph like this:

* analyze only the users and not the admins
* the fontsize and the figsize remain the same
* for each hour, calculate the average number of commits on working days and on
weekends (if there were no commits in an hour, do not use it to calculate the
average) use these values for your graph, for example: Mon, 17-18: 5 commits, Tue,
17-18: 6 commits, Wed, 17-18: 7 commits
* choose a palette that you really enjoy, you do not have to replicate it from the graph
above
* at the end of your Jupyter Notebook, create a markdown cell and insert the question
  * “Is the dynamic different on working days and weekends?”, for the answer
include the hour when the number of commits is the largest during working days and the hour when it is the largest during the weekend.

### Exercise 04 : Histogram

Exercise 04

Histogram

Turn-in directory : ex04/

Files to turn in : 04_histogram.ipynb

Allowed functions : import pandas as pd, import sqlite3, import matplotlib.pyplot as plt

In the previous exercise, you had to draw a distribution grouping the values using
Pandas. Wouldn’t it be nice if we could draw it in a more automatic way? Well, we can.

But we have to use another type of visualization – histograms. This time, we will not
use the averages. We will use the absolute numbers of commits and will compare them
during working days and weekends.

Do what you need to do to create a graph

* analyze only the users and not the admins
* create two lists of values (for working days and for weekends) for the histogram
input
* the figsize is still the same, you can choose the fontsize as well as the color palette
* use a level of transparency for the histogram in front equal to 0.7
* at the end of your Jupyter Notebook, create a markdown cell and insert the question:
“Are there hours when the total number of commits was higher on weekends than
on working days?” In your answer, put the top-4 examples.

### Exercise 05 : Boxplot

Exercise 05

Boxplot

Turn-in directory : ex05/

Files to turn in : 05_boxplot.ipynb

Allowed functions : import pandas as pd, import sqlite3, import matplotlib.pyplot as plt

Remember how we tried to figure out if the newsfeed affected the behavior of the test
and control users? Last time, we just calculated the average values. But do we know
something about the variances? What if it changed too? What if we had some outliers?

To answer those questions it may be handy to draw a boxplot.

Do what you need to do to create a graph like this:

* use the data from the [file](https://drive.google.com/file/d/1B6M7Ku89ViIStXvWU6j7PyDnCTb0McEI/view?usp=sharing), read it to a dataframe and make any modification that
you may find useful to solve the task
* the figsize is still the same, you can choose whatever fontsize you like
* the color palette should be the same as in the example
* the fontsize of the title is 15
* the width of the box lines is 3, the width of the median lines is 2
* at the end of your Jupyter Notebook, create a markdown cell and insert the question:
“What was the IQR of the control group before the newsfeed?” In your answer, put
the approximate value that you can get just by looking at the graph, round it to
the nearest 10

### Exercise 06 : Scatter Matrix

Exercise 06

Scatter Matrix

Turn-in directory : ex06/

Files to turn in : 06_scatter_matrix.ipynb

Allowed functions : import pandas as pd, import sqlite3, from pandas.plotting import
scatter_matrix

Remember how we tried to find out if there was a correlation between the number of
visits to the Newsfeed and the average difference between the first commit and the lab
deadline? The problem is that the correlation coefficient shows whether there is a linear
relationship between the two variables. But what if it is not linear? How can we see
that? That’s right – by drawing graphs!

Do what you need to do to create a graph 

* create a dataframe where each user of the test group has the average difference,
number of pageviews and number of commits
* do not take project1 into account for calculations of the average difference and the
number of commits
* take the number of commits from the checker table
* the figsize is still the same, you can choose whatever fontsize you like as well as the
color palette
* the size of the dots should be 200
* the width of the lines of the diagonal graphs (kde) should be 3
* at the end of your Jupyter Notebook, create a markdown cell and insert the ques-
tions:
  * “Can we say that if a user has a low number of pageviews then they likely
have a low number of commits?” The answer: yes or no. 
  * “Can we say that if a user has a low number of pageviews then they likely have
a small average difference between the first commit and the lab deadline?” The
answer: yes or no. 
  * “Can we say that there are many users with a low number of commits and a
few with a high number of commits”? The answer: yes or no. 
  * “Can we say that there are many users with a small average difference and a
few with a large average difference”? The answer: yes or no.

### Exercise 07 : Heatmap

Exercise 07

Heatmap

Turn-in directory : ex07/

Files to turn in : 07_heatmap.ipynb

Allowed functions : import pandas as pd, import sqlite3, import matplotlib.pyplot as plt, from
mpl_toolkits.axes_grid1 import make_axes_locatable

Several exercises back, we wanted to see if there are different patterns for users during
working days and weekends. In this exercise, let us find out if there are different patterns
for users between different weekdays and between different hours.

* analyze only the users and not the admins
* you can choose the color palette that you like for both of the graphs that you will
need to draw in this exercise
* use the table checker for your query
* use absolute values of the commits, not the averages
* sort the dataframes by the total number of commits made by a user
* at the end of your Jupyter Notebook create a markdown cell and insert the questions
(answer them looking only at the graphs):
  * ◦ “Which user has the most commits on Tue?” The answer: user_*. 
  * “Which user has the most commits on Thu?” The answer: user_*. 
  * “On which weekday do the users not like making a lot of commits?” The
answer, for example: Mon. 
  * “Which user at which hour made the largest number of commits?” The answer,
for example: user_1, 15
  
Do what you need to do to create two graphs like this:

### Exercise 08 : Seaborn

Exercise 08

Seaborn

Turn-in directory : ex08/

Files to turn in : 08_seaborn.ipynb

Allowed functions : import pandas as pd, import sqlite3, import matplotlib.pyplot as plt, import
seaborn as sns

Ok, sometimes in the previous exercises we ignored project1 in our calculations. The
project was a competition. It had longer deadlines and much more commits than ordinary
labs had. Let us see the dynamic of commits in this project per user. This time we will
use another library for data visualization in Python – Seaborn. In general, it is much
easier to create something beautiful in that library.

Do what you need to do to create a graph 

* analyze only the users and not the admins
* take into account only logs from the table checker where the status is ready
* you can choose the palette that you enjoy
* the linewidth should be 3
* the background of the graph is gray
* the height should be 10, and the width should 1.5x in relation to the height
* the fontsize of the title should be 30
* the fontsize of the axises labels is 15
* at the end of your Jupyter Notebook create a markdown cell and insert the questions
(answer them looking only at the graphs):
  * “Which user was the leader in the number of commits almost all of the time?”
The answer: user_*. 
  * “Which user was the leader for only a short period of time?” The answer:
user_*.

### Exercise 09 : Plotly

Exercise 09

Plotly

Turn-in directory : ex09/

Files to turn in : 09_plotly.ipynb

Allowed functions : import pandas as pd, import sqlite3, import plotly.graph_objects as go,
import numpy as np

* Matplotlib and Seaborn are really powerful libraries and you can use them for most
of the tasks that you may have related to DataViz. But they do not offer you the
functionality of creating interactive charts and animations. And Plotly can help
you with that. In this exercise, you will need to create almost the same graph as
in the previous exercise but in an animation.

Do what you need to do to create a graph

It is not an easy task, and it is hard to find good and clear tutorials, so use this [link](https://github.com/datageekrj/YouTubeChannelHostingFiles/blob/master/lineRace.py)
as a reference.
