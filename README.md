# AnimalRoadkillAnalysis
Analysis on Animals deaths due to road accidents over Cincinnatti Area

I like to drive alone, go for adventures. once, I was driving from Ohio to Pennsylvania to gaze at stars in Cherry Springs State park. 
Along the way I noticed something on the roads. Every now and then I saw dead animals on the road, like very frequently. Even I dodged one or two. 
I felt sorry for those dead animals and also concerned about the people safety because some animals like deers might create damages to people if they bump one.
After coming home, I started searching for animal road death data. Few cities especially Cincinnati had reporting system using which people report the sight of dead animal or death incidents.
I tried to gather every states' data to see what can be done. Sent couple of mails to state authorities to ask for any such such data but not successful.
So I started working on Cincinnati data. The CSV file got time,date, place of incident, and most importantly description of what they saw.
Here I wanted what type of animals are dying more frequently and tried to categorize animals death numbers geographically to see any correlation.
But there was no animal name column, rather there is description column where people typed what they saw. Within that they gave animal name, some did not. 
So I wrote a small piece of python program to parse the description in every row and detect the animal name in it and put it as a separate column adjacent to the description. 
I used fuzzy logic to match the nearest animal name from the description to the list of animals that I have prepared. because of lot typos in the description. 
I could have used auto correct library alone to do this job but I did not do that because auto correct sometimes changed the animal name to some other word that think its right. 
Finally I created a heat bubbled over the map to find the hotspots where someone have to be careful while driving.

below is the dashboard. And watch out for racoons while driving!


https://public.tableau.com/views/AnimalRoadkillAnalysis-CityofCincinnati/Dashboard1?:language=en-US&:display_count=n&:origin=viz_share_link
