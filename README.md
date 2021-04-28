# mars-web-scraping

### Introduction
Let's have some fun with the Mission to Mars! In this little challenge, a web application that scrapes various websites for data related to the Mission to Mars was build, and all the information scraped are displayed in a single HTML page. 

### Instruction
The first folder **mission_to_mars** is place where all scripts are stored. In here, we can find the following documents:
1. [mission_to_mars.ipynb](https://github.com/Grace-Bijun-Li/web-design-challenge/blob/main/WebVisualization/Resources/readme_image/summary.PNG)
    - This is the Jupyter notebook that completes all of the scraping and analysis tasks from the following websites:
        - [NASA Mars News Site](https://mars.nasa.gov/news/) -> collect the latest News Title and Paragraph Text.
        - [JPL Featured Space Image](https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html) -> find the current Featured Mars Image.
        - [Mars Facts](https://space-facts.com/mars/) -> scrape the table containing facts about the planet including Diameter, Mass, etc.
        - [USGS Astrogeology](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) -> obtain high resolution images for each of Mar's hemispheres.

2. [scrape_mars.py](https://github.com/Grace-Bijun-Li/web-design-challenge/blob/main/WebVisualization/Resources/readme_image/summary.PNG)
    - This is the file that transforms all scrapings from the Jupyter notebook mentioned above. This python file allows the scraping to be connected to the MongoDB with Flask templating.

3. [app.py](https://github.com/Grace-Bijun-Li/web-design-challenge/blob/main/WebVisualization/Resources/readme_image/summary.PNG)
    - This file is the python file that creates the route to deploy the HTML page.

4. The **templates** folder that contains the [index.html](https://github.com/Grace-Bijun-Li/web-design-challenge/blob/main/WebVisualization/Resources/readme_image/summary.PNG) template, which will take the mars data dictionary and display all of the data in the appropriate HTML elements.

Another folder **screenshots** contains the screenshots of the final applications (the HTML page). The HTML page will look like this:
![final_application_1.png](Images/final_app_part1.png)
![final_application_2.png](Images/final_app_part2.png)