from crewai import Task
from textwrap import  dedent

class YouTubeAutomationTask():

    def youtube_coordinator_task(self,video_topic,video_details,agent ):
        return Task(
            description=dedent(f"""Oversee the YouTube preparation process including market research, title ideation, 
                description creation and email creation required to make a YouTube video.  The ultimate goal is for 
                you to generate a report including a research table, potential high click-through-rate-titles,
                a YouTube video description and an email newsletter update about the new video.

                The video topic is: {video_topic}
                The video details are: {video_details}

                Here is an example report that you can use as a template:
                - It is important to note that the example report only contains 2 videos,
                  but the final report should contain 15 videos.
                - It is important to note that the example report only contain 3 CTRO titles,
                  but the final report should contain 10 titles.

                Example Report:
                # YouTube Competition Research Table:
                - Video 1:
                    - Title: "How to Make Your First YouTube Video (START to FINISH)"
                    - View Count: 320,000
                    - Days Since Published: 780 
                    - Channel Subscriber Count:29000000
                    - Video URL: "https://www.youtube.com/watch?v=bKvfzxtadL8"

                - Video 2:
                    - Title: "How to Make YouTube Videos on Your Phone!"
                    - View Count: 181000
                    - Days Since Published: 300
                    - Channel Subscriber Count: 29000000
                    - Video URL:"https://www.youtube.com/watch?v=wsyu38CBy7E"

                ...

                # Potential High CTRO Titles:
                - How to Make Your First YouTube Video
                - How to Make YouTube Videos on Your Phone!
                - How to Make YouTube Videos for Beginners
                [The rest of the potential high CTRO titles go here]

                #YouTube Video Description:
                Attention developers and AI enthusiasts! Learn how to create a powerful Streamlit app that integrates cutting-edge Generative AI Models like GPT-3 with the Python PPTX library to revolutionise your presentation game!
                In this step-by-step guide, you'll explore the magic of Large Language Models (LLMs) like GPT-3 and witness how it seamlessly processes your input text, crafting visually stunning PowerPoint slides using PPTX that leave a lasting impact on your audience.
                Embrace the future of presentation-making, where AI becomes your creative ally. Watch now and embark on the adventure of building your Text-to-PPT app using GPT-3, Streamlit, Python, and the powerful pptx library. 

                Like, Subscribe & Share this tutorial with fellow developers to spread the knowledge of AI-powered presentations! 
                Resources:
                - https://serper.dev/
                - https://www/crewai.io/

                # Email Announcement:
                Subject: New CrewAI Tutorial: Learn How To Use the Latest CrewAI Features

                Hey [FIRST NAME GOES HERE]!

                Exciting update: CrewAI's new version is here, making it quicker and more dependable!

                You loved our first CrewAI tutorial, so I just published a new one for you.

                In this tutorial, you'll get up to speed with CrewAI's new features. We'll then apply these updates by building an AI Newsletter, demonstrating how to use what you've learned in a real project.

                [VIDEO PREVIEW HERE]

                Here's what's in store:

                Learn to manage a team with CrewAI's new Hierarchical workflow.
                Discover how asynchronous tasks can boost your efficiency.
                Find out how the Expected Output feature ensures accuracy and reliability.
                Plus, lots more insights!
                Dive into the tutorial to explore CrewAI's enhanced functions:

                [VIDEO PREVIEW HERE]

                Questions or want to share how you're doing? Email me or comment on YouTube.

                Happy coding!

                Cheers, 
                GenAI
                                   
            """),
            agent=agent,
            output_file="output/YouTube_Video_Creation_Report.txt",
            expected_output=dedent(f"""
                Generate a report that is formatted exactly like the example report provided to you earlier.
                Make sure the report contains 15 videos, 10 potential high CTRO titles, a YouTube video description,
                and an email newsletter.  The researched video should have all the required details and valid URLs.
            """)
        )
        

    def researcher_task(self,video_topic,video_details,agent ):
        return Task(
            description=dedent(
                f"""For a given video topic and description, search youtube videos to find
                15 high-performing YouTube videos on the same topic.  Once you have found the videos,
                research the YouTube video details to finish populating the missing fields in the research
                CSV.  When delegating tasks to other agents, make sure you include the URL of the video that you need 
                them to research.

                This research CSV will be used by other agents to help them generate titles and other agents to help 
                them generate titles and other aspects of the new YouTube video that we are planning to create.

                Research CSV Outline:
                - Title of the video
                - View count
                - Days since published
                - Channel subscriber count
                - Video URL

                The video topic is: {video_topic}
                The video detail is {video_details}
                Important Notes:
                - Make sure the CSV uses ; as the delimiter
                - Make sure the final research CSV does not contain duplicate videos
                - It is SUPER IMPORTANT that you properly match up view counts, subscriber counts,
                    and everything else to the video URL.
                - It is SUPER IMPORTANT that you only populate the resesrch CSV with real Youtube videos and YouTube
                    URLs that actually link to the YouTube Video.
            """),
            agent=agent,
            output_file="output/YouTube_Video_Creation_Report.txt",
            expected_output=dedent(f"""
                Video Title; Video Count; Days Since Published; Channel Subscriber Count; Video URL
                How to make Youtube video; 100,000; 30; 1000; https://www.youtube.com/watch?v=1234
                How to get your first 1000 subscribers; 100,000; 30; 1000; https://www.youtube.com/watch?v=1234
            """)
        )

    def title_creator_task(self,video_topic,video_details,agent):
        return Task(
            description=dedent(f"""
                Create 10 potential titles for a given YouTube video topic and description.
                It is very important to use researched videos to help you generate the titles.
                The title should be less than 70 characters and should have a high click-through-rate.
                               
                The video topic is: {video_topic}
                The video detail is {video_details}
            """),
            agent=agent,
            expected_output=dedent(f"""
                - CrewAI Tutorial for Beginners: Learn How to Use Latest CrewAI Features
                - CrewAI Tutorial: Complete Crash Course for Beginners
                - How to Connect Local LLMs to CrewAI [Ollama, Llama2, Mistral]
                ...
                """)
        )
    
    def description_creator_task(self,video_topic,video_details,agent):
        return Task(
            description=dedent(f"""
                Create a description for a given YouTube topic and description.
                The video topic is: {video_topic}
                The video detail is {video_details}
            """),
            agent=agent,
            expected_output=dedent(f"""
            Download the CrewAI Source Code Here:
            https://github.com/joaomdmoura/crewAI-examples/tree/main/CrewAI-LangGraph
            
            Donot forget to like and subscribe if you are fan of free source code.
            
            Stay updated with 
            """)
        )

    def email_creator_task(self,video_topic,video_details,agent):
        return Task(
            description=dedent(f"""
                Create an email to send to an email list to promote the new YouTube video.
                               
                The video topic is: {video_topic}
                The video detail is {video_details}
                Here are a few previous announcements that you can use as inspiration.

                Important Note:
                - Make sure to copy my style, tone, and voice when writing the email.
                - Create a draft email.  Once you have created a draft email, you MUST have a human review, you MUST have human
                review your tentative final email.

                Email 1:
                Subject: New CrewAI Tutorial: Learn How To Use the Latest CrewAI Features

                Hey [FIRST NAME GOES HERE]!

                Exciting update: CrewAI's new version is here, making it quicker and more dependable!

                You loved our first CrewAI tutorial, so I just published a new one for you.

                In this tutorial, you'll get up to speed with CrewAI's new features. We'll then apply these updates by building an AI Newsletter, demonstrating how to use what you've learned in a real project.

                [VIDEO PREVIEW HERE]

                Here's what's in store:

                Learn to manage a team with CrewAI's new Hierarchical workflow.
                Discover how asynchronous tasks can boost your efficiency.
                Find out how the Expected Output feature ensures accuracy and reliability.
                Plus, lots more insights!
                Dive into the tutorial to explore CrewAI's enhanced functions:

                [VIDEO PREVIEW HERE]

                Questions or want to share how you're doing? Email me or comment on YouTube.

                Happy coding!

                Cheers, 
                GenAI

                Email 2:
                Subject: New CrewAI Tutorial: Learn How To Use the Latest CrewAI Features

                Hey [FIRST NAME GOES HERE]!

                Exciting update: CrewAI's new version is here, making it quicker and more dependable!

                You loved our first CrewAI tutorial, so I just published a new one for you.

                In this tutorial, you'll get up to speed with CrewAI's new features. We'll then apply these updates by building an AI Newsletter, demonstrating how to use what you've learned in a real project.

                [VIDEO PREVIEW HERE]

                Here's what's in store:

                Learn to manage a team with CrewAI's new Hierarchical workflow.
                Discover how asynchronous tasks can boost your efficiency.
                Find out how the Expected Output feature ensures accuracy and reliability.
                Plus, lots more insights!
                Dive into the tutorial to explore CrewAI's enhanced functions:

                [VIDEO PREVIEW HERE]

                Questions or want to share how you're doing? Email me or comment on YouTube.

                Happy coding!

                Cheers, 
                GenAI

            """),
            agent=agent,
            expected_output=dedent(f"""
            An email that contains a subject and body that is formatted exactly like the example email provided to you earlier.
            """)
        )