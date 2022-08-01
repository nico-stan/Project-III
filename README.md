# Project III - Hourglass games new home

<p align="center">
<img src="https://media3.giphy.com/media/9JgeSP0jlRAVBOG9FD/giphy.gif?cid=ecf05e47jp3l0uc3mrb3f6la40lmqjda5av04epacqm4qpx9&rid=giphy.gif&ct=g" width="400" height="200" />
</p>

## **Premisse:**

Locating business is a challenging choice considering that are many interests to be met. As we decided to start the **Hourglass games**, we looked for the best building according to our company values and needs. In **Hourglass videogame**, we value:

<p>
 
- Be Adventurous, Creative, and Open-Minded
- Have all you need close to where your heart lives (at walking distance)
- Innovation Needs Inspiration and Care
- Pursue Growth and Learning Being Inspired by the Best
- All our Employees Wellbeing is Priceless
- Be Passionate and Determined
- Embrace and Drive Change

We asked our employees what they needed to feel happy about our new home. The criteria are:
- Designers like to go to design talks and share knowledge. There must be some nearby companies that also do design.
- 30% of the company staff have at least 1 child.
- Developers like to be near successful tech startups that have raised at least 1 Million dollars.
- Executives like Starbucks A LOT. Ensure there's a starbucks not too far.
- Account managers need to travel a lot.
- Everyone in the company is between 25 and 40, give them some place to go party.
- The CEO is vegan.
- If you want to make the maintenance guy happy, a basketball stadium must be around 10 Km.
- The office dog—"Dobby" needs a hairdresser every month. Ensure there's one not too far away.
 
</p>

## Location Research
1. First step was quering the companies database using mongo. As we value inspiration and want to be close to the tech and design environment, we looked for tech startpus location (biotech, cleantech, ecommerce, games video, nanotech, software, web) considering as startups companies founded from 2000 on, with less than 100 employees, that raised more than 1000000 in funding rounds. We ended up with a list of the top ten cities with more startups. We selected the top 3 as they were also listed as the best place to find job as a designer (www.designrush.com). The cities we considered were: New York, London and San Francisco.

</p>
<p>
 
2. We did some web scraping for life costs, health and crime rates. Between the three cities, health index is good and relatively similar and crime rates are slightly higher in San Francisco, though that does not refer to the neighborhoods we would consider to locate **Hourglass games**. Moreover, costs with transportation and square meter prices in the center were cheaper in San Francisco in 2022. With the tech high levels of attrition rate and agressive competition, we know that to attract the best talents and keep them working happy and satisfied with us we need to invest. Companies that keep their talents with people analytics have 30% higher stock prices, 79% higher return on equity and 96% higher revenue on three years and 56 % higher profit margins than their counterparts (Ferrar & Green). Therefore, we plan to pay slightly above the international market, invest in quality of work life having their main needs fullfiled in walking distance, considering everyone need as equaly important and boost their creativity with a high quality network within and outside our company. </p>
<p>
 
Moreover, we don't want our employees stuck in long hours drive to be able to connect with other companies or worse: to far from their kids so that they cannot follow their developmnet. As San Francisco is known as the smallest big city and as a hotspot for statups at this moment, we decided to locate **Hourglass games** there. Besides, the population range of age is the same as in our company, so it will be easier to our employees to make friends and feel home in a very inclusive and open minded location.
 
</p>
<p>
 
3. Plotting the statups and design companies with Foursquare API it is possible to notice that the highest concentration of companies nowadays is in the Mission District, having moved from where it was in the previous years. Therefore, that was pottentialy chosen as neighboorhod. Aditionally, this neighborhood has a sub climate different than the rest of San Francisco with less fog and wind.

</p>
<p>
 
4. We believe that un creative teams everyone is equally important, so we also checked for the rest of our criteria to find a new hoe using Foursquare API. We were able to meet all the requirements in a 3 km radius.
 
</p>
 
 # Creating Dataframes from Foursquare queries
df1 = foursquare (key,"Design Studio", location, radius, 15)
df2 = foursquare (key,"Children School", location, radius, 5)
df3 = foursquare (key,"Startup", location, radius, 15) #Get more updated results for Startups.
df4 = foursquare (key,"Starbucks", location, radius, 10)
df5 = foursquare (key,"San Francisco International Airport", location, 30000, 1)
df6 = foursquare (key,"Bar", location, radius, 10)
df7 = foursquare (key,"Vegan Restaurant", location, radius, 5)
df8 = foursquare (key,"Basketball Stadium", location, 5000, 2)
df9 = foursquare (key,"Pet Grooming", location, radius, 5)
df= pd.concat([df_startup, df1, df2, df3, df4, df5, df6, df7, df8, df9], ignore_index=True)
4. 
5.


Use an API to get venues (and for this, you'll need a starting point; some coordinates from which you will call the API)
Justify your decision using data, not just visualization. How? Maybe measuring distances, maybe assinging weights depending on the importance of your criteria, maybe calculating the density of schools/Starbucks, etc.
​





## Our New Home 
​
Our location has to be aligned with our values. Therefore, we need a home that meets the following requirements:
<p>

 

​
## Considerations and limitations
​


### How reliable is this data?
<p align="left">
<img src=" " />
</p>


​
## Project files
​
The main directory has 3 subdirectories:
- Input: Holds the data used to analyze the hypothesis. It is a folder with multiple files which are then merged into a single dataframe in the Output folder df_clean.
- Output: Contains the df created from the original data, and a folder named images with the figures that are used multiple times through the project.
- src: Contains python files with all functions created specifically for this analysis.
- README: This file works as a report for the project
In the root directory there are 2 Jupyter Notebook files that include all the code used in the project:
- "Exploratory data analysis" (EDA): This file explores the data (how much data there is, how is it organized and the quality of it). This file also scrapes information from wikipedia on Net Migration by country and merges all input files into a single dataframe.
- Plotting: This file is used to create plots that help visualize the data in order to check if the hypothesis is true.

​
## Annex
​
**- Variable**
Explanation
