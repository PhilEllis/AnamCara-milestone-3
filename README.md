
# Anam Cara

<h1 align="center"><img src="documents/AnamcaraPreview.png"/></h1>


<a href="https://anam-cara-45d556e859ea.herokuapp.com/"><img src="documents/anamcaral.png" width="30px" /></a> Live website

<a href="https://github.com/PhilEllis/AnamCara-milestone-3/tree/main"><img src="documents/githublogo.png" width="30px" /></a> GitHub Repository

<a href="https://anam-cara-45d556e859ea.herokuapp.com/"><img src="documents/herokulogo.png" width="30px" /></a> GitHub Repository

# Welcome to Anam Cara!

The term **"Anam Cara"** originates from the Irish Gaelic language. "Anam" meaning "soul," and "Cara" meaning "friend." 


Rooted in Celtic spirituality and philosophy, particularly in Ireland. It represents a deep and spiritual friendship that transcends superficial connections. An Anam Cara is someone with whom you can share your innermost thoughts, feelings, and emotions without fear of judgment. They understand and accept you completely, providing a safe and nurturing space for your authentic self.

It has become a symbol of the profound and transformative nature of genuine friendships that nurture the soul.

The concept of Anam Cara emphasizes the importance of fostering authentic relationships and recognizing the interconnectedness of all beings. It invites us to cultivate deep connections, engage in soulful conversations, and cherish the bonds that nourish our spirits. Anam Cara serves as a reminder of the value of genuine friendship and the power it holds in our personal and spiritual journeys.

Functionally, Anam Cara is striving to provide a platform for users to authentically express their inner thoughts, desires, and memories in a mindful and heartfelt manner. The beta version of the site allows users to create an account, login, and leave their messages termed ‘Express their hearts whispers’.

Anam Cara incorporates a unique feature where users can choose to schedule their message for publication on a specific date. This feature aligns with the concept of creating a slower, more intentional experience, rather than instant gratification. Once a day, Anam Cara scans the database and releases the scheduled messages for that day, with the newest messages appearing first. This approach encourages users to anticipate and appreciate the heartfelt messages each day, fostering a sense of connection and reflection. Users are invited to ‘Discover soulful connections ‘ by reading the published messages.

The site also provides users with the ability to login and edit or delete their published messages. This empowers users to have control over their content and allows for any necessary updates or adjustments to be made.

Socially, Anam Cara strives to create a community centered around meaningful connections and mutual understanding. By fostering a space for authentic expression and intentional reading, the platform encourages users to engage with messages that resonate with them and find solace or inspiration in the shared experiences of others. Anam Cara aims to shift the focus from endless scrolling and superficial interactions of mainstream social media platforms to a deeper, more heart-filling experience that enriches the user's day.

Overall, Anam Cara seeks to provide a mindful and soulful digital sanctuary where users can express themselves, connect with others on a profound level, and create a slower-paced, more meaningful online experience.


## Table of Contents

- [User Experience (UX)](#UX)

- [Features](#features)

- [Technologies Used](#technologies)

- [Testing](#testing)

 - [Deployment](#deployment)

- [Credits](#credits)

<a name="UX"></a>
## User Experience (UX)

## User Stories - 
- #### story 1
    1. I want to connect with like-minded individuals who resonate with my messages, fostering meaningful conversations and supportive interactions.
    1. I want to be able to login and edit or delete my messages should i chnge my mind.
    1. I want to be able to revisit and reflect upon my past messages, witnessing my personal growth and evolution over time.
    1. I want this to provide me with a slower less intrusive way of expressing myself and connecting.

    
- #### Story 2.
    1. I want the platform to provide a user-friendly and intuitive interface, allowing me to easily navigate through messages and engage with the community.
    1. I want to choose when to publish my message in particular around a date that holds significance to me.
    1. I want the platform to provide a sense of serenity and tranquility, offering a calming and visually appealing environment where I can immerse myself in the heartfelt messages. 
    1. I want the option to choose if i share my contact details and if i do have the freedom to choose what contact details i share to connect with other community members.
   

- #### Story 3
    1. I am fed up of the monotony of social media and i need a reset. I want this platform to foster slow reading and occasional visits apposed to endless scrolling.  
    1. I want to be able to connect in a world were anonymous trolls are not able to attack posts with comments but instead people can request to connect. 
    1. I don't want to provide a profile image, i want to feel part of something new that fosters love and friendship before material judgement that thrives today.
    
### User Stories - Business Owner
- #### I am a business owner currently wishing to test the concept of an app that intends to work as the anti consumer driven social media that is seen today and instead build a space where a community and real connection can be fostered. I feel this would have a major impact on peoples wellbeing and mental health. 
    1. I want to create a platform that cultivates a supportive and inclusive community, attracting a diverse range of users who value authenticity and meaningful connections. 
    2. I want to implement measures to ensure the privacy and security of user data, building trust and confidence in the platform. 
    3. I strive to create a sustainable and scalable platform, allowing for future growth and expansion while maintaining the core values and essence of Anam Cara.

## Design Choices

>### Structure Considerations
- #### Schema
    - Below is the reference table for the database schema - two tables. One for retaining the information of the message left of the note form and one for user authentication. 

         <img src="documents/Databasemodel.png" />

- #### Database Flow
    - The yellow element is the user arriving at the site. The diagram details the initial thought process behind what elements would be visible to the user prior to authentication (green elements) and what elements would need authentication to view (blue elements). This was drawn up with the user story request in mind to protect the users data messages but to give them control over their own content. 

         <img src="documents/databaseflow.png" />

- #### Wireframes
    - Referring to the database flow and i roughly sketched an idea of the rough structure. Which i then went on to progress in figma, as shown below. 

        <img src="" />

>### Aesthetic Considerations

- #### Colour scheme
    -  In order to fulfil the brief of making this platform to provide a sense of serenity and tranquility and tying it in to the Irish Gaelic origin of the name i opted for a pallete of dark moody greens. accented by light greys and a pop of yellowy gold in order to add contrast and bring attention to features. It was important to me to have a lighter grey within the palette to utilise on forms and provide that clear definition and contrast for users when reading each others messages. When considering using a darker more moody theme throughout the site i was keen to ensure that it was still accessible. Coloors does help by indicating the contrast text colour but i referred to the slack channel a11y-accessibility for their thoughts and found a brilliant link to dark theme sites. From this i gleamed that a dark theme was fine but should be enhanced by using lighter areas to bring text forward and enhance reading. https://uxplanet.org/8-tips-for-dark-theme-design-8dfc2f8f7ab6


        <img src="documents/colourpallet.png" height="70px" />


- #### Typography
    - The main brand identifiable font used is Spectral - a unique google font that i felt captured the traditional nature of story telling with a slightly softer side to it. Achieving this whilst still being accessible and very readable. The secondary font for headings was intended to be Inter however there were not any sub header occasions. Open Sans as the main text font as it is very user friendly and accessible. Sans-serif has been chosen as a fall-back font.
   

    - Spectral - for headings
       
        <img src="documents/spectral.png" height="30px" />

    
    - Inter - for Sub headings although hardly used
       
        <img src="documents/inter.png" height="30px" />


    - Open Sans - for the body


        <img src="documents/opensans.png" height="30px" />



- #### Imagery
    - I selected two images one of a man with his hand on his chest and one of a woman with her hands clasped in thought. I felt like both images conveyed the sentiment of the site and also worked well when overlaid with the dark green colour. Both images were sourced from Istock.
>### Structure & Aesthetics Considered

- #### Mockups
    - After selecting the brand colours and potential imagery and bearing in mind the advice read and received regarding darker themes i created a simple mock up of the project. The purpose of this was to guide me on my colour selection and placements. 


        <img src="documents/figmamockup.png" />

<a name="features"></a>
## Features

### Existing Features

>#### Common Features Across All Pages
- **Favicon** - 
    - Expand
- **Header** - 
    - Expand
- **Accessibility**
    - Expand
- **Buttons**
    - Expand
- **Responsiveness**
    - Expand
- **Footer**
    - Expand
    


>### Specific to Pages
-  **Index**
    - Welcome 



## Anam Cara Future Iterations

- 
- 


<a name="technologies"></a>

## Technologies Used

>### Languages Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [JavaScript](https://www.javascript.com/)

>### Frameworks, Libraries, Programs, Online Resources Used

- [Git](https://git-scm.com/) 
- [GitPod](https://www.gitpod.io/) 
- [Github](https://github.com/) 
- [Bootstrap v5](https://getbootstrap.com/) - Responsive Elements Hero, navigation, buttons & cards.
- [jquery](https://jquery.com/) - Used for the toggle function in the navigation
- [Google Fonts](https://fonts.google.com/) - Play and Source Sans Pro fonts
- [Font Awesome](https://fontawesome.com/) - Button icons.
- [Photoshop](https://www.adobe.com/ie/products/photoshop.html - images have been resized and edited within photoshop.
- [Coloors](https://coolors.co/) - Used to create the colour palettes and identify complimentary and contrasting colours. This was also used to check the accessibilty of the text colour with each background colour during the planning stage. 
- [RGBA Color Picker](https://rgbacolorpicker.com/hex-to-rgba) - to match hex colours to an RGBA so that i could change the apacity accurately.
- [Istock](https://www.istockphoto.com/)- Istock used for all imagery within the site. image credit as follows
     - [Galaxy Background](https://www.istockphoto.com/vector/space-background-with-realistic-nebula-and-shining-stars-colorful-cosmos-with-gm1173451503-325938376) image by Egor Suvorov from Istock
     - [Planet Vectors](https://www.istockphoto.com/vector/glossy-planets-vector-set-gm453780213-30624312) Vector image by andegro4ka from Istock
     - [Rocket Animation](https://www.istockphoto.com/video/ship-rocket-launch-startup-new-business-project-new-business-project-concept-vehicle-gm1249549420-364189430) created by Zozulinskyi from Istock
- [youtube](https://www.youtube.com/watch?v=mQrlgH97v94) The Planet Song - 8 Planets of the Solar System Song for Kids | KidsLearningTube on Youtube 
- [Fiver](https://www.fiverr.com/gemmawilson?source=inbox) Logo png files and favicon created by Gemma Wilson
- [Figma](https://www.figma.com/file/ladBUkKqWA50bv0xDRaMUH/SPLANETS?node-id=0%3A1&t=rRbFBuY40vnsdoR4-1) used to create mock up designs
- [Balsamiq](https://balsamiq.com/wireframes/desktop/) Used to create the initial wireframes
- [amiresponsive](https://ui.dev/amiresponsive) Used to create the live image capture of site

<a name="#testing"></a>
## Testing

>Please refer to TESTING.md document


<a name="deployment"></a>
## Deployment

>### Publishing
This website was published using [GitHub Pages] & Heroku (https://pages.github.com/). The procedure is outlined below.
1. 
2. 
3. 
4. 
5.  
6. 
7. 
8. 

>### Forking
If you wish to contribute to this website you can Fork it without affecting the main branch by following the procedure outlined below.
1. 
2. 
3. 
4. 
5. 

>### Cloning 
If you wish to clone or download this repository to your local device you can follow the procedure outlined below.
1. 
2. 
3. 
4. 
5. 
6. 
7. To create your local clone press `Enter`

<a name="credits"></a>
## Credits

>### Code 

- The majority of the code originated from the Bootstrap library and was styled with custom css.
- All of the rest of the code was written by the author - Philippa Ellis



>### ReadMe Resources
- [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#code)
- Code Institute [SampleREADME](https://github.com/Code-Institute-Solutions/SampleREADME)
- Slacks numerous Markdown questions and answers
