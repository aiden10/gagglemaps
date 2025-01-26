Inspiration

We wanted to find empty areas/rooms on campus. But we had no time to check each room ourselves to find a spot. This is why we decided to just put some hidden cameras in all the rooms so that we can check all the rooms from the comfort of own home. This way, we can know ahead of time what space is free!
What it does

By using a camera and microphone planted in a classroom, we are able to view live footage of the class and check what is being said. We are also able to maintain a headcount in every room that can be viewed live.
How we built it

Using OpenCV and speech_recognition python libraries, we collected video and audio data from the rooms. Afterward, we processed and uploaded the data to our MySQL database. Using FastAPI to create endpoints, our frontend retrieves the data and displays it to the user!
Challenges we ran into

    Getting all the room data, there are way too many rooms at UW! Quest is hard to scrape!
    Finding a good area to put our camera and microphone
    Making a scalable frontend considering the quantity of rooms

Accomplishments that we're proud of

-Successful capturing of video and audio with accurate captioning -Creating a live interactive heatmap showcasing the school's current traffic -Speeding up the process of finding available study spaces
What we learned

We learned a lot of things, a lot of the libraries and concepts we used were completely new to us. -OpenCV, speech_recognition library, HTML, CSS, JavaScript, MySQL, FastAPI, websockets, git as well as an attempt at web scraping.
