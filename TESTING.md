# Anam Cara - Testing

![App Preview](documents/AnamcaraPreview.png)


## Table of Contents

- [Test Record](#testrecord)
- [Functionality](#functionality)
- [CSS3 Validator](#css)
- [HTML5 Validator](#html)
- [JavaScript Validator](#js)
- [Python Validator](#python)
- [Accessibility](#access)
- [Compatibility](#compatibility)
- [Performance](#performance)
- [User Story](#user)
- [Known Bugs](#bugs)



<a name="#testrecord"></a>
## Test Record :
**TEST** | **ACTION** | **EXPECTATION** | **RESULT** 
----------|----------|----------|----------
 Home page | Size to 320px using Chrome Dev Tools	| Elements look good @ 320px | Works as expected
Home page | Size to 1920px using Chrome Dev Tools | Elements look good 1920px | Works as expected
Home page | Size to 990px using Chrome Dev Tools | Navbar to toggle | Works as expected
Home page | Scroll action | NavBar Scrolls with user | Works as expected
Home page | Header Nav links clicked |  User taken to respective correct pages | Works as expected
Home page | Size to 990px & Toggle Nav links clicked |  User taken to respective correct pages | Works as expected
Home Page | Footer Nav links clicked | User taken to respective correct pages | Works as expected
Home page |Header Logo Text clicked | User taken to Home page | Works as expected
Home page | Downward chevron icon clicked | Take user to the Discover section | Worked as expected
Home page | link clicked on Express link in discover section | Take user to login prompt or if logged in to the express form | Worked as expected
Home page | link clicked on Connect link in discover section | Take user to Connect page | Worked as expected
Home page | link clicked on About link in discover section | Take user to About page | Worked as expected
About page | Size to 320px using Chrome Dev Tools	| Elements look good @ 320px | Works as expected
About page | Size to 1920px using Chrome Dev Tools | Elements look good 1920px | Works as expected
About page | Downward chevron icon clicked | Take user to the Who We Are section | Worked as expected
About page | Size to 990px using Chrome Dev Tools and toggle links clicked | NavBar to toggle and links take user to respective correct pages | Works as expected
About page | Scroll action | NavBar Scrolls with user | Works as expected
About page | Header Nav links & Logo Text clicked |  User taken to respective correct pages | Works as expected
Connect page|Size to 320px using Chrome Dev Tools	| Elements look good @ 320px | Works as expected
Connect page|Size to 1920px using Chrome Dev Tools | Elements look good 1920px | Works as expected
Connect page|Size to 990px using Chrome Dev Tools and toggle links clicked | NavBar to toggle and links take user to respective correct pages | Works as expected
Connect page | Header Nav links & Logo Text clicked |  User taken to respective correct pages | Works as expected
Connect page| Clicks Express You Heart Button | Takes User to Login or if already logged in to Express page | Works as expected
Connect page| User not logged in - Scroll to view & read messages left by users | Messages appear - No Update or Delete buttons seen | Works as expected
Connect page| User logged in - Scroll to view messages left by users | Messages appear and Users own messages now have Update & Delete buttons displayed | Works as expected
Connect page| User Logged in - click Update button on users own message | Update form appears pre populated |Works as expected
Connect page| User Logged in updating form- Clicks Submit Update button |  User redirected to Connect page and updated message appears |Works as expected
Connect page| User Logged in - click Delete Trash Can button on users own message | Delete Modal appears to confirm deletion |Works as expected
Connect page|User Logged in - clicks Cancel button on the Delete modal | Delete Cancelled redirected back to message |Works as expected
Connect page|User Logged in - clicks Delete button on the Delete modal | Message deleted user redirected back to Connect page |Works as expected
Express page|Size to 320px using Chrome Dev Tools	| Elements look good @ 320px | Works as expected
Express page|Size to 1920px using Chrome Dev Tools | Elements look good 1920px | Works as expected
Express page|Size to 990px using Chrome Dev Tools and toggle links clicked | NavBar to toggle and links take user to respective correct pages | Works as expected
Express page | Header Nav links & Logo Text clicked |  User taken to respective correct pages | Works as expected
Express page | User not logged in - Navigate to Express page | Login form shown with invitation to login to view page | Works as expected
Express page | User logged in - Navigate to Express page | Express form shown | Works as expected
Express page | User inputs Text into Name field | Data Enters min 3 - max 60 and required elements flagged when not met or exceeded | Works as expected
Express page | User selects continent | Data Entered - required elements flagged when not met | Works as expected
Express page | User selects Today's Date | Date Entered - required elements flagged when not met | Works as expected
Express page | User inputs text into Title field | Data Enters min 5 - max 60 and required elements flagged when not met or exceeded | Works as expected
Express page | User inputs text into Title field | Data Enters min 100 - max 1000 and required elements flagged when not met or exceeded | Works as expected
Express page | User inputs text into Title field | Data Enters min 3 - max 70 and required elements flagged when not met or exceeded | Works as expected
Express page | User selects Publish Date | Date Entered - required elements flagged when not met | Works as expected
Login page| Size to 320px using Chrome Dev Tools	| Elements look good @ 320px | Works as expected
Login page| Size to 1920px using Chrome Dev Tools | Elements look good 1920px | Works as expected
Login page| Size to 990px using Chrome Dev Tools and toggle links clicked | NavBar to toggle and links user to the respective correct pages | Works as expected
Login page| Header Nav links & Logo Text clicked |  User taken to respective correct pages | Works as expected
Login page| User inputs valid username and password | User taken to Connect page successful login message displayed and button to Express Your Heart now takes user to Express Form | Works as expected
Login page| User inputs valid username and password | Navigation bar Login/Register button changes to a Logout option | Works as expected
Login page| User inputs in-valid username and password | Flash message appears to highlight they have entered an invalid username or password  | Works as expected
Sign Up page| Size to 320px using Chrome Dev Tools	| Elements look good @ 320px | Works as expected
Sign Up page| Size to 1920px using Chrome Dev Tools | Elements look good 1920px | Works as expected
Sign Up page| Size to 990px using Chrome Dev Tools and toggle links clicked | NavBar to toggle and links Sign Up to respective correct pages | Works as expected
Sign Up page| Header Nav links & Logo Text clicked |  User taken to respective correct pages | Works as expected
Sign Up page| User inputs username and password | user redirected to login page saying success and inviting them to use their new credentials to login | Works as expected - Database checked password is successfully hashed
Logout NavBar Button| Logged in user clicks to logout | User logged out and redirected to the home page successful logout message displayed | Works as expected


<a name="#functionality"></a>
 ## Functionality Testing
 
- 
- 
- 

<a name="#css"></a>
## CSS3 validator - Pass
<img src="assets/img/readmeimg/cssvalid.png" />
http://jigsaw.w3.org/css-validator/validator$link

<a name="#html"></a>
## HTML5 validator
- 
- 
<a name="#js"></a>
## Javascript validator
- 
- 

<a name="#python"></a>
## Python validator
- 
- 
  
<a name="#access"></a>
## Accessibility

### Lighthouse testing
- <img src="assets/img/readmeimg/indexlighthousetest.png"/>
- 
- <img src="assets/img/readmeimg/gamelighthousetest.png" />


<a name="#compatibility"></a>
## Compatibility Testing
- Browser Compatibility tested via [Browser Stack](https://live.browserstack.com/) 
- tested on the latest versions of the following
    | Safari    | Firefox   | Chrome  | Opera  | Edge  |
    | --------- |:---------:| -------:| ------:| -----:|
    | Pass      | Pass      | Pass    | Pass   | Pass  | 
    
- Chrome developer tools has been used to check the responsiveness of the site across different screen sizes and devices. 
- The site has mostly been built and tested on a Macbook Air operating on MacOs Catalina.

<a name="#performance"></a>
## Performance Testing
-  The performance of the site was tested on the following site with satisfactory results. [Web Page Test](https://www.webpagetest.org)

<a name="#user"></a>
## Testing User Stories 
>### External testing
- 
- 
>### User Stories - Customer
- 
- 


>### User Stories - Business Owner
- 
- 


<a name="bugs"></a>
## Known Bugs



## Bugs & challenges experienced during the build
