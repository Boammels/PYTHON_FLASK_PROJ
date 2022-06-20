After having completed the tests, we have been able to gather a relatively good
idea about which functions are dependant on others, which ones will be more 
complicated and which will be easier. Whilst at this stage we have not worked 
out exactly how we will allocate who does which functions, it is possible that
it will involve implementing the functions that we wrote tests for. This will 
hopefully be efficient as while writing tests, you must understand the 
requirements and most likely have formulated ideas about how the function could 
best be implemented.

Steps for implementation:
1) In order to begin working effectively, we need to implement the auth register
and auth login features. This will be the first step as users need to be able to 
build an account and login before they can use any of the other features of the
software. It is also not dependant on any other functions and alot of other 
functions have depednencies on it. These dependencies come as almost all other
functions involve using a token that is generated on login or register and is 
continued to be used as a way to identify which user is calling each function.
It is therefore vital to ensure this function works perfectly before moving on,
as if it doesn't it will be very difficult to pin down exactly where errors are
due to the dependencies. Most likely, all of us will focus together on getting
these functions perfect, as we can't begin work on other functions until this
one is done. This will ideally take about a week to finish completely.

2) Once we have implemented and tested auth register and auth login and are sure
it works, we can then split up and implement functions seperately. Certain 
functions throughout the project will be more important to the overall functionality 
of the backend than others. These functions should be implemented first. This is so we 
want to be able to produce a working verson of the software as quickly as possible,
a key feature of the agile development approach. The following functions will allow
for a basic version of the channel system to be implemented, allowing users to join 
channels and send messages for others to see in the channel.
These functions will be:
channels_create, channel_join, channel_invite, message_send, message_remove
After having implementing these functions, a basic version of the backend system 
should be working. Hopefully, this should take another week to implement.

3) After having completed these functions, the following developments will slowly
implement the features specified by the clients. Overtime more and more smaller features, 
such as the ability to react to and pin messages, the ability to customise profiles
ect. These features will be more independant and easier to test. This should take between
1 and 2 weeks to finish, as there are alot of functions to finish. We will make sure that 
these are all implemented on seperate branches and are only merged after we are sure they 
work with no issues.

4) After all the features are added, we can go over all the functions we have written and
test that they are commented well for maintanence as well as pass all the tests that were 
written in iteration 1. This should not take too long, between 2-3 days, and this time can 
be minimised by ensuring we test and comment along the way. After this stage is done,
iteration 2 of the project should be complete. 

Overall broader plans that we hope to follow are making use of github branches.
Throuhghout the first phase of implementation, we have only used the master branch. 
This is because we divided up work so nothing overlapped, making branches unnecessary.
However, once we start implementing code, we may want to write the function in multiple ways
and then push the best, most efficient and working version to the master branch. This is
much more important for the second iteration of the project which requries one main program
to be subdivided into parts that work together. This in turn, means team members progress 
affects the progress of everyone else.
Similarly, we will need to focus on more frequent communication, to let our team mates know
when we have completed a function so we can successfully merge it and use it. This will be 
necessary in order to minimise merge conflicts which can be completely avoided with good 
communication. This can also be done with regular by regular pushes to github.
We will also make use of the task board git hub offers that we used for the user stories
to indicate to our team mates what is currently being worked on and when certain tasks
have been completed. This will provide us with useful information about where we are up to 
in terms of implementation and whether deadlines are being met. It is important to stay on
top of deadlines so that implementation can go as smoothly as possible.

Diagram for the timeline attached in the planDiagram.png file