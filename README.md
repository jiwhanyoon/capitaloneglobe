# WebGL Globe

### 10/29/2016


This is a **WebGL Globe** for a project to submit to Capital One. The demo version can be accessed here.


[My Globe](https://jiwhanyoon.github.io/capitaloneglobe/)

----

![](https://github.com/jiwhanyoon/capitaloneglobe/blob/master/view.png)

The WebGL Globe is an open platform for geographic data visualization from Chrome Experiments that allows users to enter many types of data and map where the associated events occurred on the planet - I chose to use the data set that represented the latitude, longitude, and magnitude of the earthquakes that happened throughout the world in 1964, 1969, and 1974. The data can be accessed from [here](http://datasets.flowingdata.com/earthquakes1974.csv).

----

Data parsing and reorganization was done in Python - read more about the steps I have taken through "Paragraph.txt" file.

## Data Format

The following illustrates the `JSON` data format that the globe expects:

```javascript
var data = [
    [
    'seriesA', [ latitude, longitude, magnitude, latitude, longitude, magnitude, ... ]
    ],
    [
    'seriesB', [ latitude, longitude, magnitude, latitude, longitude, magnitude, ... ]
    ]
];
```


If you want to build you own globe, visit [WebGL Home](https://www.chromeexperiments.com/globe).

