# Project1: mic-kuu's favourite movies
This project is a result of Udcaity's Fullstack Developer Nanodegree assginment. It's a Python "backend" that will dynamically render a webpage containg a list of defined movies. 

![mic-kuu's favourite movies GUI](http://i.imgur.com/Ms0QeRv.jpg)

## Overview
The project has a very simple structure. The entry python script is *entertainment_center.py*. If you run it using python interpreter:
```python entertainment_center.py```
It will generate an index.html file in the root directory of the project. The script will automatically open the generated HTML file in the default system browser. The generated website consits of vertical panels that are expandable on click. The site uses the css flexbox to achieve a reponsive effect.

## How to use 
The movies that are generated into the webpage are defined as the `movies` array (*entertainment_center.py*) of python objects:
```python
blade_runner = media.Movie("Blade Runner",
                           "http://i.imgur.com/KykTdlk.jpg",
                           "https://www.youtube.com/embed/eogpIG53Cis?rel=0&amp;showinfo=0")
movies = [blade_runner, movie2, movie3]
```
In order to generate a different content, simply modify created movies objects and\or their arrangement in the movies array. The HTML+CSS is designed to work best with 2-6 movies defined. 

The project was designed and tested using **Python 2.7.3** and it will work best in that enviroment. There is no guarante that it will work on different Python releases.

## Contributions
Special thanks to [wesbos](https://github.com/wesbos) for the inspiration for the layout of the site - [repository](https://github.com/wesbos/JavaScript30/tree/master/05%20-%20Flex%20Panel%20Gallery)

## License
![Creative Commons License](https://i.creativecommons.org/l/by/4.0/88x31.png) 
This work is licensed under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/)
