# Udacity-Movie-Site
Welcome to my first project submission for the Udacity Full Stack Nanodegree: The Movie Trailer Site

The project contains three files: Media.Py, entertainment_center.py, and fresh_tomatoes.py.

To run the project, download all three files to a folder on your computer. Open entertainment_center.py and run. This project makes use
of a python API used to query movie data called tmdb3. This module must be installed prior to runtime. PIP tmdb3 works fine. 

Due to querying restrictions in place at TheMovieDB.org, it is not possible to query more than 40 items in under 10 seconds.
To bypass this limitation, I've added a one second delay in between each Movie class instantiation. In the real world this would not be a
real solution. However, if a site like this were live, I'd be able to use proper caching or pay for a higher level access.

Thank you.
