#One paragraph explanation of what I built and what I used to build it 


The project I have built is a visualization of the earthquakes data in 1964, 1969, and 1974.

The original data set was in CSV (comma separated values) format and contained the info WebGL wanted (latitude, longitude, magnitude) as well as many extraneous fields such as depth, type, place, etc. I converted the CSV file into a JSON file using an online converter, which successfully outputted the values in arrays. In Python, I wrote a data transforming algorithm to collect just the information I needed (year, latitude, longitude, and magnitude) using the json library in Python - this is included as “data_transform.py” in the scripts folder. After appending all the values I needed for this project, I saved it as a separate .json file, which was similar in structure to the pre-provided “population909500.json.” In index.html, I read that file in by 
{
xhr.open('GET', 'quakes.json', true)
}
and changed the ‘id’ field to correspond appropriately. When I loaded inititally, it didn’t load. After reading through the code a couple times, I realized that whenever we attached the script and mentioned the source, we it was trying to search for the “globe” directory while the program was already inside the “globe” directory. After a futile search for the directory, the program didn’t output the globe I wanted. So I went on to erase the “/globe/“ to allow my program to realize there is no need to search for a globe directory because it was already inside it. Also, no globe showed up at all in the beginning. Because the globe wasn’t a simple display, I read the provided ‘globe.js’ file to figure out when the javascript was calling for the world.jpg image. Because the inspection of the site that was loaded locally complained that it could not locate the “world.jpg” file, I tried changing the name of the file, extensions, and even a different image, but none of it worked. Then, I realized that when it was loading texture via 
{
uniforms['texture'].value = THREE.ImageUtils.loadTexture('world1.jpg’),
}
it had “imgDir" in front of it, which caused the same problem as before: searching for a “globe” directory to go into while already being in that directory. So I took out the “imgDir” and sure enough, the globe finally showed up. 