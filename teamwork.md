ITERATION 2

#===============#

Physical meetup #1

#===============#

Time: 16/10/2019, 1pm - 3pm
What we achieved:
This was our first physical meetup after the demo of iteration 1 so firstly we 
briefly discussed how that went and what we could have done better. In summary,
we thought that the main aspect of team work we need to focus on for the next 
iteration is communication. This is becuase we are aware of how when implementing
software, often code overlaps and is depedant on each others. Also, we all have
different ideas about what the best way to go about the problem is, for example,
how we plan to store the data, what is the most efficient way to divide up the
work load, ect. At this point, we are planning on sticking with what we planned 
in iteration 1 and dividing the work in accrodance with the tests we wrote as we 
will be more familiar with what is expected from these functions. However, at this
early stage, we will work together as a group.

Once we had consolidated our iteration performance, we then went
on to begin working on the project itself. With any big project, the best way to
go about it's completion is break it down into steps. Luckily, as a result of the
plan written in iteration 1, we have conceptually already done this. Our first 
step we decided on would be to get the auth functions working, as this would 
users cannot do anything with the app itself until they have an account logged
in. Therefore, in this first session, we all worked together to try and get 
auth/register working. In order to do this we needed to work out a way to store 
data. For now, we are just using a local data variable to the auth function but
since we are planning to split up all the functions into files based on their type,
auth, message, channels and user, this will need to be changed later. At this point,
we have not connected the functions up to a flask server, and are making sure the functions
work simply off of the test files we wrote in iteration 1. Then once we are further 
along in the projects lifetime, we can actually create the flask overlay for the server.

By the time we were done, we were able to complete the auth register (testing with 
our original tests passed all of them) function and make good progress on the auth 
logout functions. We worked well together as a team and were able to do pair
programming in groups of two, communicating with the other 2 when we had questions
allowed us to think through a range of possible implementation ideas for both the 
implementation of the functions and how everything should be stored.

Methods to ensure meeting was successful:
As mentioned above, pair programming, brainstorming ideas and following a conceptual 
plan played a major role in making sure we stayed on track.

Plans to deal with problems:  
- Create deadlines for certain parts to be done so we can stay on track
- Ensure we communicate constantly with what we have completed and when we want 
to push to the master branch so no one messes up anyone elses work. Merge conflicts 
are also not pleasant to deal with so minimising these will make for smoother 
implementation.
- Aiming to meet up phycially at minimum once a week and have regular messaging
and calls on our group chat. During the physical meetups we should go over exactly 
what we have done so everyone else knows, however, hopefully we should know already 
from good communication on the group chat

#===============#

Physical meetup #2

#===============#

Time: 24/10/2019, 12pm - 2pm
What we achieved:
During this meetup, alot of the project has been completed. We have worked out
how we are going to implement the flask server over the backend and also how we 
are going to split the files. Up until this point, everyone was working from their 
own file but wasnt sure how exactly we would end up relating them together. The 
main reason for this confusion was it relied heavily on the implmentation of the 
flask server which was not yet completed. 

In the first meetup, we mainly did pair programming on the flask server, as at 
this point, we had worked out a good way to do it, but hadn't implemented it yet. 
Therefore, Simon and I focused on soing this, whilst Leslie and Jason focused on 
the finishing up the channels function which they had made good progress on together.
We also begun testing the function themselves with postman. Whilst this was a bit 
later than I personally would have liked to begin testing with the internet 
(we had done testing with out own tests of course), that was just the nature of 
the problem, as we hadn't yet worked out the flask server implementation. We were 
able to get valid inputs for most of the auth functions we had written which was 
good as it meant testing could commence for the auth functions. 

However, an issue did arise when when checking on the channels functions written 
by Jason and Leslie. They had been using their own data structure and not the 
global one we had implemented. This raised issue as the way the data was stored 
did not line up. This meant that Jason needed to work out a way to adapt his code 
to to fit in with how Simon and I had implemented the data. Jason and I dealt with 
this in the next physical meetup, which only involved the two of us, unlike the 
others which involved the whole team. We planned to meet in order to work out how 
to merge the two different data structures we had used into one global one such 
that it is feasable for both of us. In hindsight, greater communication between 
our pair programming groups would have erased this issue.

Methods to ensure meeting was successful:
- Testing of the functions we were writing to ensure they worked
- Pair programming as it was very successful and led to great progress being 
made last time we did it. For Simon and I, he would type whilst I would look over 
his shoulder whilst he would type. I would be bug fixing and giving him ideas as 
he typed. When we were testing, we would both type when we had ideas as to what 
was causing the bugs we encountered. Jason and Leslie used a similar practise with 
Jason typing and Leslie looking over his shoulder.

Plans to deal with problems:  
- As mentioned, we are planning to resolve the data storage conflict in our next 
meeting, we will hopefully solve this by pair programming and communicating how 
in specifics how we have implemented our respective functions such that we can 
compramise and revise the data structure so it suites everyone. Once we have done 
that, we will make sure that everyone follows this strictly so the problem doesn't 
arise again.

#===============#

Physical meetup #3

#===============#

Time: 24/10/2019, 3pm - 4pm

What we achieved:
Throughout this meetup, Jason and I focused on fixing up the data storage conflicts 
we came across in the previous meetup. In order to go about solving this, we did 
pair programming, with me typing and Jason looking over my shoulder. Luckily for 
us, the differences between our data structures did not overlap as much as we thought 
as the way users and channels are stored hnot interact with each other by nature. 
This made things much easier to work with, but there was still issues that we had 
to overcome as a result of the data structure Simon had come up with for storing 
channels conflicting with Jasons. The data structure was changed to pretty much 
overide the one Simon wrote for channels whilst still keeping the user one 
untouched. This is because it is best we want to make the transition from Jasons 
data type to ours as easy as possible. Along the way we realised that it would be 
best for the messages field to be stored within the channels field. This idea will 
definitely make implementation of the messages file, which I will be doing, much 
easier. Jason will need to make some minor revisions to his code as a result of 
the adapt to the new data structure but it shouldn't be too difficult as structurally 
there is not too much difference. All in all, with the data structure finalised 
as a result of this meetup, we can be confident in finishing up the rest of the 
project on time.

Methods to ensure meeting was successful:
- Pair programming and good communication of how we implemented our code up until
this point.

Plans to deal with problems:  
- With no more physical meetups likely, we will keep up the voice calls on the 
group chat and messgae regularly to inform the others of exactly what is being 
done and when we need to update our branch as fixes have been made.

In summary, we worked well as a team. Both in person and online, we were able to
communicate effectively with eachother in order to complete iteration 2 of the
project as quickly as possible. In order to improve for the next iteration, we
would benefit from meeting up physically even more in order to pair program, which
was very effective. Also greater communication from everyone on the taskboard 
would allow all other team members to have a greater understanding of what was 
expected from other team members.

ITERATION 3

#===============#

Physical meetup #1

#===============#

Time: 9/11/2019, 1pm - 2pm

What we achieved:
Prior to this meetup, we had been primarily using online communication. However,
we figured in order to work out exactly how we were going to go about handling the more complex 
documentation and code that would require good allocation of resources to do effectively. We had 
been working on getting our basic functions to work with the frontend. This was done mainly through 
visual testing, as even though the functions did indeed pass the required pytests, the frontend was 
not working correctly. As we worked thorugh the problem, it turns out that a majority of these 
issues came as a result of misunderstnading the format data was required to be sent in to the 
frontend. Therefore, simple fixes were applied which alot of functions which were not workinmg to 
work very quickly. These include GET channel details, channel list all and channel show messages. 
This goes to show how simple misunderstandings can be resolved quickly with good teamwork. 

In the meeting, we worked out how we were going to handle the workload for the seprincples document. This 
document is a large percentage of the mark, so it is very important we do it thoroughly. I planned 
to refactor each main document that we wrote, auth/channel/message and user. With 4 main documents, 
this leaves one person to refactor each file. We divided it up using a very similar approach to 
what we used in the past, with each person refactoring the code they were most familiar with. By 
this point, individuals would be highly familiar with their code and would be aware of how it 
worked, allowing them to make changes to increase efficiency without having the side effect of 
breaking the once working code. A potential issue that we discussed was the fact that refactoring 
without careful testing after each change could make bug testing very difficult once we merge our 
code together. Hence, I made it very clear, we needed to test frequently after every individual 
update and only push to master once everyone was satisfied with it working. At this point, we have 
done alot of working on the front end and do not want to waste time fixing bugs that were not 
present initially. 

After we had worked out how to divide up the load, we made a deadline,
we had to have the work complete by the 13/11/2019. This deadline was set to give us ample time
to fix any merge conflicts that will most likely arise and also test to esnure that all components
are still working together as they once were.


Methods to ensure the meeting was successful:
- Setting deadlines to ensure work gets done and we don't have to rush to implement 
- pair programming to reduce errors and problem solve together
- open communication, we made sure everyone understood what was expected of them so they knew exactly what to do with no excuses

Plans to deal with problems
- If the dealine is not met, we will likely resolve this by communicating with 
the team member whose duty it was to check how close they are. They will most likely 
be close but just be finishing things off as they may have been busy with other 
commitments. Hence, a group member with a slightly lighter load or more technically 
component can communicate they will finish off the job. The clear communication of 
the task being handed over is vital to reduce merge conflicts and ineffient work 
(multiple people workin on the same code).
- Any programming problems with the frontend will be solved through communication 
with other team members. ASking for their insight and persepctive is an excellent resource for problem solving. 
Other great resources are asking questions on the forum or preparing questions to ask tutors.

#===============#

Physical meetup #2

#===============#

Time: 11/11/2019 3pm-4pm

What we achieved: During the first meetup, we focused primarily on planning how we were going to 
complete the documentation and did not do much coding. Hence, we decided that this meetup would be 
much more focused on coding. For this iteration, their are a few difficult functions which we have 
not yet implemented and we would be more effective if we brainstormed the ideas for the best 
solution. These functions include the upload and crop photo function and the standup functions. We 
realised that all of these difficult functions were currently allocated to Simon to complete as he 
was the one who wrote tests for them and coded them initially on the backend. However, it was clear 
very quickly that the programming workload he would have would be disproportionate to anyone else. 
Therefore, we divided up these task, with me willing to take all the standup functions as during 
brainstorming, we realised that alot of the concepts were similar in nature to the message send 
later function I had already implemented. Simon would then take the upload and crop image, which 
turned out to be a difficult task taking multiple days to complete. Whilst this eventually worked 
out well, this problem arised intially from underestimating the difficulty of functions. The 
ability to be flexible and accomidating for other team members and a good work ethic proved to be 
key in successful team work. 

Jason and Leslie continued to focus on refactoring throughout the 
metting, helping each other out with refactoring the functions they had been allocated. Having 
instant communication avaliable in a team meeting proved to be highly beneficial as whenever any 
minor problem occured, it was able to be put to the group and then quickly resolved. This process 
would be much slower with a message to our group chat, with a response potentially taking longer. 
We did also make clear that we would try to be active on the chat as much as possible so problems 
would not be left unaddressed, which would halt progress greatly. 

Simon and I for the remainder of 
the meeting pair programmed on user profile, as we discovered a bug with user profile. It appeared 
to be outputting the correct information, but the frontend did not seem to understand it. Luckily 
this isssue was indepedant from the upload profile image function, so Simon was able to work on 
that and test it with my help here and there without being effected by the broken user profile 
function. By the end of the meeting, both Simon and I had made progress on our problems, whilst not 
having resolved them entirely. Jason and Leslie had also continued to make good progress 
refactoring their functions, making the meeting successful and productive.

Methods to ensure the meeting was successful:
- We continued to utilise pair programming an open communication as it has proven and continues to 
prove to be effective in maximising quality product, as the input of another individual can iron 
out bugs quicker and provide new and possibly more efficient solutions to problems that might not 
be obvious from your own persepctive.
- Talk about all problems and concerns in physical meetings, any misundersntaings about their own 
tasks or other peoples code were encouraged to be clarified during the meeting rather than later.

Plans to deal with problems
- Division of tasks when the workload became too heavy for one person proved to also be effective.
- Constant communication on the group chat so everyone knows the state of everyone elses progress.

#===============#

Physical meetup #3

#===============#

Time: 14/11/2019 12pm - 2pm

What we achieved: With the deadline fast approaching, in this meeting, we focused on making sure we 
were on track to completing the task on time. Between this meetup and our previous, the deadline we 
set for finishing the seprinciples document had elapsed, meaning we used the start of this meeting 
to make sure that everyone had finished and if not, check how close they were to doing so. Whilst a 
few people had finished others were having difficulties working out exactly how they were going to 
refactor their program, or had not written large amounts in the documents. This was discussed and 
foe those who hadn't yet completed, they said they were able to get it done within the next few 
days. I had initially set the deadline for completing this to be well before when the project was 
due. This is so we would have plenty of time to test the refactored changes and possibly accomodate 
for people by writing extra parts for them in the seprinciples document if they had not been able 
to complete their task. If the document has not been complete by Friday, then I will most likely 
step in and finish everything up as I have knowledge most aspects of the program at this point and 
would be able to do that.

After that, we split up, all having aspects of the project that we knew we wan't to work on. Simon 
was finishing up the upload profile and crop, which is proving to be one of the most difficult 
functions for the whole project. Everyone has been made aware of this and were giving him as many 
ideas as possible to help him out. The main issue he was having was accessing the server side port 
being used from his machine as the program can only access the backend port. However, by the end of 
the meeting, he managed to store the image on the backend, not requiring the frontend port and 
hence getting the function working with the frontend. This was very well done from SImon and showed 
great perseverance, as he had been working on this feature for multiple days only making 
incremental progress, so it is great to see everything work out, getting the frontend a major leap 
further to being completely implemented. I focused on fixing the user profile bug. I was having no 
luck until Simon managed to work out with the help of the piazza forum that it was just an issue 
with the return type, with the frontend simply wanting the user dict by itself as opposed to 
{'user': userdict}, which was confusing as almost all other functions require data to be given in 
the latter way so it is JSON serialisable, but I am happy that is working. For the remainder of the 
meeting I worked on standup and made some great progress on it. This was able to happen as the 
standup functions did turn out to be similar to the message send later function, utilising a thread 
which would stall the execution of a part of the code until the standup time had elapsed. By the 
end of the session, standup was working and the only problem was the formatting of the standup 
message being a bit strange.

Jason and Leslie continued to work together utilising pir programming to do their parts of the 
seprinciples document. By the end of the session, their parts were very close to being finished. 
With this, the project is coming along very nicely, almost all of the functions have been correctly 
implemented with the frontend with the exception of auth permission change. 
With this likely being our last physical meeting, at the end, we discussed what needed to be done 
in order to finish of the rest of the project. The main things we came up with were:
- Fix up the pytests as some of them have failed after frontend adjustments being made
- Fix up the test admin permissions function so that it works with both pytest and the frontend
To keep track of this, we made sure that we would keep the taskboard up to date, so everyone knows 
at all times what has been done, what is being worked on and what needs to be done. This way our 
work overlaps as little as possible. We also made sure that we would write every piece of work we 
were compelting onto the task board in order to keep everyone in the group up to date on everyone 
elses progress.

Methods to ensure the meeting was successful:
- We used pair programming an open communication as it has proven and continues to prove to be 
effective in maximising quality product. We have repeated to do this thorughout the porject since 
iteration 1 as we have found it to be so effective.
- Clear communication continued to be used, we made sure everyone knew what was expected and made 
compramises where neccessary

Plans to deal with problems
- Make use of the task board and keep it updated so everyone in the team is kept up to date on 
everyone elses progress.
- Compramise, take the work load for others if it is too much. Take the steps required to ensure 
the project is compelted to the highest possible standard.

In conclusion.
Iteration 3 has gone smoothly, we have been able to utilise teamwork effectively to divide tasks 
and ensure we are efficient. We have been change our initial allocations of work in accordance to 
what would work best, which is typically not easy, but we have handled it well to ensure the work 
gets done. We have been able to compramise for each other and this in turn has made our team 
efficient and able to produce a quality functional product that not only meets user requirements, 
but has been tested to ensure its functionality. Our use of the agile development process 
throuhgout implementation can be seen throughout and was a driving factor been our ability to 
excel.