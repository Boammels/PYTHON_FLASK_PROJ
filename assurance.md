 - Verification: meets the specs requirements
 - Validation: meets real users needs

Validation: Strategies to make sure our product meets the clients requests:
To ensure our product meets front end requirements, our main resource is the 
provided frontend. This will allow us to see if the data we are storing and 
providing works and will actually create a product that is usable to a client.

Once we have finished implementing the backend and it appears to work well with
frontend, we can go back the our employers and demonstrate to them what the product
does and see if they are happy with it. If they are not, we will ask them to specify 
what extra features they would like to see implemented are what features that we 
have implemented we have done wrong. If new features are required, we will add them 
in and if new feautres require updates to meet client needs, we will do that as well. 

This cycle will continue until the clients say they are happy with the final product
and are ready to release it. Initially, we will only relase the product to a select 
small group of users, so they are able to use it and report their satisfaction with the
product. 

If all goes well, then implementation can be implemented more broadly.
If not, then we will discuss with our employers what more they want from the 
product to make it better. Once these proposed changes are implemented, we will 
again go to our employers and repeat the process of checking if they are happy with 
the new product, if they are, then it will be rereleased to another small sample of users.
Once they give good reviews, it will proceed to be rolled out to the whole university.

This process is the agile approach to developing software and focuses largely on 
communication with clients and frequent working versions of the software that are
refined over time as a result of feedback. The agile approach is highly effective 
for ensuring validation is achieved as the product being built is constantly 
validated by the clients how are going to be using it, allowing for a customisable
solution that can be moulded as a result of feedback.


Verification: Strategies followed to ensure our code worked and met the spec:
 - For each user story, accpetance criteria have been written (see task board). These are small 
 testable chunks which will indicate whether a specific aspect of the specification 
 has been met. All the acceptance criteria tests will be done to ensure the code 
 written meets the specs requirements.
 - Ensure the functions being written pass the tests we wrote for our functions 
 in iteration 1. These unit test the functions and ensure they all work as planned
 in accordance to the spec.
 -Testing with postman, an API client allowed us to make sure our flask server 
was correctly implemented over the top of the functions we were writing. This 
allowed us to conduct broader testing and gain insight into whether all the 
components that have been set up in different files all work together in order to 
produce the final working product. This also allowed us to see exactly how are data 
was being stored globally across the files which was valuable as it gave insight
into exactly what we were storing and examine if their were more efficient methods
to storing the data. This process allowed us to make a change to how we were
storing messages. Had we not made this change, it would have been almost impossible
for us to meet the specs requirements.
 - Throughout the process we are making sure that the code on the master branch 
 always contains correct and functional code, and only pushing to master once we 
 have done proficient testing of the function being pushed.
 - Each team member will have their own branch to work from allowing multiple
 people to work on the same files if necessary. This will make sure that if one 
 of us makes a major mistake which ruins everything, they can simply merge from 
 master and have working code again, not ruining it for everyone else on the team.
 We also made sure to communicate when we were about to push to the master branch. 
 We would make sure we made it clear on the group chat that they have uploaded 
 their changes to their individual branch so everyone else could look over that 
 person's changes to the code. Everyone was able to make sure they were happy 
with it, understood what was being done in case any aspects of new code affected 
other peoples code and it contained to errors so they could be fixed.
 - We also used python3-coverage in order to check whether our tests 
 comprehensively tested the functions we have written. We attempted to get the
 best coverage possible so we know are tests hit all edge cases.
 - We also used pylint to catch errors in style so that our code was easier to
 read for other members of the project and maintain once the project implementation
 is complete
