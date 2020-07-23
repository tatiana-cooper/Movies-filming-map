
# Movies filming map
This program builds the dots on the map according to:  
1) countries were the movie was made in a given year;
2) if these countries are English-speaking;
3) if these countries are landlocked;

![image](https://drive.google.com/uc?export=view&id=1gqBhmWv0WayFI7B9-uPe2dJXiND36D5M)


In this project I mastered:

**Python** <br>
**Folium** <br>
**Geopy** <br>
**Json** <br>


## Files
> file_parsing.py — this file parsing film's information from the `locations.list`.

> json_parsing.py — this file loads data from `countries.json`.

> main.py — this file launches the project and generates map.

> sort_countries.py — this file sorts countries by landlocked and English-speaking criteria.

> countries.json — this file contains information about counties.

> locations.list — this file is IMDb's movies data.(https://www.imdb.com/)

> Map_1900.html and Map_1892.html — resulting files of the program's run (in 1900 and 1892 filming years). 


## Installation
The project requires Python 3+.

### Clone
Clone this repo to your local machine using  `https://github.com/tatiana-cooper/Movies-filming-map.git`

### Setup
Windows 10:

For launching app:
```sh
> python main.py
```

### Warning! 
For some yers the program runtime may take a long period of time to finish <br>
because of the large amount of data to process<br>
It happends because it takes too long for Geopy lib to convert location name into coordinates<br>


## Usage
All usage steps are described dynamically during the program run.

