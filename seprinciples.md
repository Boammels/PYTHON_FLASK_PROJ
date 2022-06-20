During iteration 2, our main priority was to create functions which worked on the
backend and would therotically work on the front end. Due to time constraints 
and other factors, the quality of the code produced, in terms of software
engineering principles, the code was not up to standard. Alot of code was 
repeated instead of using functions to save short term time (not long term), 
alot of sections of logic were over complicated as a result of still developing 
understanding of the spec and efficient ways to navigate through our data 
structure. Throughout iteration 3, we have utilised software engineering principles
in order to refactor our code making it easier to understand for individuals
outside our team which will be highly beneficial in terms of long term maintanence
as well as ability to reuse code written in the future. This will document will 
break down the specific methods we went through for each main function we wrote:


AUTH FILE

- For the auth register and login  function in iteration2, we had previously checked whether 
the email had been used before by looping through all the emails in current database.
This was used frequently across functions. Therefore I create a simple function to 
find emails instead of repeating the same block of code in multiple functions.

- In admin_userpermission_change function, to change the permission_id we need to 
find the user dictionary with current u_id several times which is repeatly.
Now one function has been added in order to access current user dictionary in one line. 

- From iteration 2, there were a a few imports which were not required as they 
were being imported in other files than auth imported. This is an example of unneccessary
coupling between components. To reolve this, import jwt and from json import dumps.

- For alot of the helper functions, comments were not present explaining what each one did,
hence to fix the opacitiy of these functions, comments were added.

- As functions exit when an exception is raised, the function will exit. After a lot 
of exceptions, the functions were returning None, or something similar. This is 
unnecssary complexity and to resolve this, these lines were deleted.

- The logout function has two main points of exit, either the logout was successful,
or it wasn't. Therefore, it makes sense for this function to have only 2 return locations.
However, it has 3. This is an example of visocity, as it doesn;t make sense for this
to be occuring, making it difficult to change if a change was required. To resolve this 
issue, the unneccessary point of exit was removed and the function was restructured.
This also made the code much more opaque as it makes more logical sense.

- Some variables were misnamed, so the name was changed so it is more opaque what 
the variable is doing.

- The admin userpermission change function was broken as during initial implementation
the requirements were misunderstood, meaning the function did not function as per the spec.
This led to alot of the work being immobile. Hence this function was rewritten in 
accordance to the new spec. It was then tested with the pytests and the frontend 
to ensure it worked.

CHANNEL FILE

- Previously in iteration 2, to access a particular channel in the database 
given a channel_id we would loop through every channel, until the channel_id 
matched with the channel_id of the current channel being checked. Then when 
this occured we would store this channel in a variable so we could access it 
and break from the loop. This is an example of needless complexity as we store
the channels in order, meaning the channel with channel_id 2 will be in the 2nd
position in the array. Therefore we could access a particular channel based of the
channel_id with a simple 1 liner. This strategy for accessing a channel was also 
needlessly repeated so we could cut out a lot of lines of code. There was no need
to place this line into a function as now it is only 1 line. When Simon coded this,
he made sure to alert everyone in the team, as this would greatly simplify the code
and would be highly beneficial to everyone.

- In the get channel id function, global is used when it is not necessary. It is needlessly complex
and the data, that has already been globalled, can just be passed into the function.

- As a result of the change admin persmission function being fixed up, some changes 
to the channel invite and join functions were required. This is an example of fragility and coupling
as mulitple components are dependant on each other. However, this was more of a feature
that needed to be added rather than something that would cause an error. 

- Almost every function checks if the channel is valid and if the user is valid, 
there is currently a function which checks if the channel is valid, but to reduce
needless repition and make the function more compact, we could check if the user 
is valid within the check the channel is valid function. This could be seen as
adding compelxity but the function will be renamed to describe its additional 
functionality so it will not be confusing.

- We add a new function called show_new_list to generate a new list of channels which associate with the certain user or all of the existed channels.
There will be a arg which named as index( when index is 1 means that the fucniton should return a list of channels which associate with the given user. when index is 0 means that the function will return a list of all existed channels.)
Previously in iteration 2, there were too many nested loop. So the main aim in iteration 3 is to simplif the nested loop and decorate them as functions.

MESSAGE FILE
- For implementation 2, a get channel function was created, to go into the database
and access channel in accordance to the channel_id. However, as mentioned before,
the channels always remain stored in order and channels cannot be deleted, thus
to access a specific channel, this can be done in one line, making the function
redundant. This is an example of needless complexity. One side effect of this is,
the function checked to ensure the channel was valid but the one line approach does not.
However, to solve this a simple adaption was implemented using a try and except 
statement to perform the same get channel functionality with O(1) instead of O(n)
time complexity.

- Nearly every function requires a check that the token being passed is valid.
They also require checks that the channel is valid, the user is valid ect.
This code is frequently repeated, an example of needless repitition and could be 
made into a function of it's own to prevent this.

- Many of the message functions also use a getMessage function, which returns 
a message based on its message_id, however, it would make more sense to check 
if the message is valid within the function. This is an example of easing needless repition
as the checks were repeated across many functions. This is now resolved.

- Unlike the channels, which cannot be removed, messages can be, meaning that 
you cannot access message data in one line like you can to access a channel.
This showed a lack of opacity with no comment indicating this was the case, so one was added
above the get message function to indicate it was necessary.

- During the rush of iteration 2, I did not have time to comment what each function
does, which is good practise. Not doing so is lack of opacity and has been now 
done for every function. This will allow other team members to instantly understand 
what a function does and possibly use in in their functions.

- Message send and send later are very similar functions which are repeated. This 
could be simplified by making it one function which changes slightly based on a 
flag passed in, handles in slightly differently in terms of send now and send later.
The only problem with this is it could compramise fragility as it will make the 
two functions that are individual on the frontend combined at the backend. However,
I think the benefits outweigh the possible complexity issues as they are both message sending 
functions.

- An issue found when testing the frontend was that react was not working as expected.
When a user reacting this was not being displayed on the frontend. This is turned out
to be because the arguments, which where numbers, where being passed into the function
as strings. This caused the react to not be handled correctly by the frontend. 
To resolve this I simply ensured the frontend was recioeving an integer value 
and this cleaned everything up.

- Initially, it was difficult to test whether show channel message was working correctly
as in the spec, the pagination must occur at 50 messages, and it is time consuming to send 50 messages
everytime a test is required. This is an example of rigidity as this pagination value was repeated 
frequently over the program, meaning if a change was made for testing sake, it would require the 
hardcoded 50 value to be changed everywhere in the code. This was refactored by 
adding a pagination constant at the top of the file which could be easily changed
and everywhere that the 50 value was, was replaced with the PAGINATION constant.
I made sure to stick to convention and name the variable in capitals so it is clear to my team this
variable is a constant




USER FILE
- In iteration 2, the user_profile_set* functions were reapeating and some are useless. In this iteration, according to the priciple, I have done quite a few adjustments. These functions are similar in steps:
- 1.checking if the user is valid
- 2.checking if the new information is valid(like email, name or handle)
- 3.changing the feature in the user's dictionary to the new information
- Thus, I ahve merged the first step into one function and so does the third step cause they actually work the same. Also I have written functions called validLength and haveDuplicate to implement the second step, after that I could call these functions in the main functions so that these functions can help me to deal with the processes.
- -For the user_profile and users_all functions, they are requiring the same information about the users, so I could also simplify them according to the engineering principle

#===========================================#

KEEP THIS FILE UP TO DATE AS YOU ARE WORKING

Bens ideas
When writing these up:
    - Explain what you did
    - Explain what software engineering principle you used to clean it up
        - Rigidity: Tendency to be too difficult to change
        - Fragility: Tendency for software to break when
        single change is made
        - Immobility: Previous work is hard to reuse or move
        - Viscosity: Changes feel very slow to implement
        - Opacity: Difficult to understand
        - Needless complexity:  Things done more complex
        than they should be
        - Needless repetition: Lack of unified structures
        - Coupling: Interdependence between components
    - Provide detials into the code you wrote to clean
    - Explain how you communicated this with us (your team)

#===========================================#
