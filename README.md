# Project III - Hourglass games new home

<p align="center">
<img src="https://media3.giphy.com/media/9JgeSP0jlRAVBOG9FD/giphy.gif?cid=ecf05e47jp3l0uc3mrb3f6la40lmqjda5av04epacqm4qpx9&rid=giphy.gif&ct=g" width="400" height="200" />
</p>

## **Premise:**

Locating business is a challenging choice considering that there are many interests to be met. As we decided to start the **Hourglass games**, we looked for the best building according to our company values and needs. In **Hourglass videogame**, we value:

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
- The office dog "Dobby" needs a hairdresser every month. Ensure there's one not too far away.
 
</p>

## Location Research
1. First step was querying the companies' database using Mongo. As we value inspiration and want to be close to the tech and design environment, we looked for tech startups location (biotech, cleantech, ecommerce, games video, nanotech, software, web) considering as startups companies founded from 2000 on, with less than 100 employees, that raised more than $1000000 in funding rounds. We ended up with a list of the top ten cities with more startups. We selected the top 3 as they were also listed as the best place to find a job as a designer (www.designrush.com). The cities we considered were: New York, London and San Francisco.

</p>
<p>
 
2. We did some web scraping for life costs, health and crime rates. Between the three cities, the health index is good and relatively similar and crime rates are slightly higher in San Francisco, though that does not refer to the neighborhoods we would consider to locate **Hourglass games**. Moreover, costs with transportation and square meter prices in the center were cheaper in San Francisco in 2022. With the tech high levels of attrition rate and aggressive competition, we know that to attract the best talents and keep them working happy and satisfied with us we need to invest. Companies that keep their talents with people analytics have 30% higher stock prices, 79% higher return on equity and 96% higher revenue in three years and 56 % higher profit margins than their counterparts (Ferrar & Green, 2021). Therefore, we plan to pay slightly above the international market, invest in quality of work life, having their main needs fulfilled in walking distance, considering everyone's needs equally as important and boost their creativity with a high quality network within and outside our company. </p>
<p>
 
Moreover, we don't want our employees stuck in long hours drives to be able to connect with other companies or worse: to far from their kids so that they cannot follow their development. As San Francisco is known as the smallest big city and as a hotspot for startups at this moment, we decided to locate **Hourglass games** there. Besides, the population range of age is the same as in our company, so it will be easier for our employees to make friends and feel like home in a very inclusive and open minded location.
 
</p>
<p>
 
3. Plotting the startups and design studios with the Foursquare API it is possible to notice that the highest concentration of companies nowadays is in the Mission District, having moved from where it was in the previous years. Therefore, that was potentially chosen as a neighborhood. Additionally, this neighborhood has a subclimate different from the rest of San Francisco with less fog and wind (plotted with cartoframe). 
 
 ![MissionDistrict]( https://raw.githubusercontent.com/nico-stan/Project-III/714fd9eb6e1dd4e783df1f29eb3458de217bd833/Output/Districts_Cartoframes.png)
 
 The best location for the building would be in the center of the startup and design studios network (plotted with folium).

 ![MissionDistrict]( https://raw.githubusercontent.com/nico-stan/Project-III/714fd9eb6e1dd4e783df1f29eb3458de217bd833/Output/Districts_Folium.png)

</p>
<p>
 
4. As 3 kilometers is the distance that people are usually willing to walk when they need to solve issues, we established that as a threshold for the location.
 
![Radius3k](https://raw.githubusercontent.com/nico-stan/Project-III/714fd9eb6e1dd4e783df1f29eb3458de217bd833/Output/Circles_Folium.png)
 
</p>
 
5. We believe that in creative teams everyone is equally important, so we also checked for the rest of our criteria to find a new home using Foursquare API. In the map it is possible to see that all the criteria important for our employees and Dobby were met in the 3 km radius.
 
<p>
 
![final plot](https://user-images.githubusercontent.com/46969106/182244843-dc8df0fc-19e1-4467-8b9c-190bd51f384b.png)
 
</p>
<p>
 
We also have a nearby airport for our accountants!
  
![ airport](https://user-images.githubusercontent.com/46969106/182244914-1668e586-7336-4728-9067-48c9448ce37c.png)

## Our New Home 

At **Hourglass games** we are crazy about fun and serious about people and data. We believe that people are at their best when they have fun and they are happy. And this starts at home. So our new locations respects the need of all our employees so they can do better what they know the best: make other people happy while they feel taken care of. Our new building is aligned with our values. This is a place to be productive and happy. </p>


![Pionner](https://user-images.githubusercontent.com/46969106/182246740-c46aa604-dec9-4e0e-947b-bb7702036d1c.png)

</p>
And Dobby says: thanks!

<p align="center">
<img src="https://media0.giphy.com/media/4Zo41lhzKt6iZ8xff9/giphy.webp?cid=ecf05e473x7jjzo8xkoo0i8sdd9w1u3atvz01f9pgtcotbqr&rid=giphy.webp&ct=g" width="450" height="350" />
</p>

## Project files

The main directory has 3 subdirectories:
- Input: Holds the data used to find our location with json.
- Output: Contains the images with the figures that are used multiple times through the project.
- src: Contains python files with all functions created specifically for this analysis.
In the root directory there are three additional files:
- README: This file works as a report for the project
- A Jupyter Notebook that includes all the code used in the project
- A Jupyter Notebook with the dataframe from the web scraping

## Reference:
Ferrar and Green (2021). Excellence in People Analytics: How to Use Workforce Data to Create Business Value. Kogan Page.

## Authors:
Juliana and Nicolas collaborated equally for the end result of this project.

