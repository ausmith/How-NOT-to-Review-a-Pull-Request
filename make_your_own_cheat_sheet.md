# Make Your Own Code Review Cheat Sheet

Because it is impossible to provide a code review cheat sheet that will apply
to everyone, this guide is intended as a framework for creating the cheat
sheet that best fits you and your team(s). The difficulty with creating a
cheat sheet that would apply for everyone is each team will develop their
own opinions on what should be required in all code reviews. Example: a
mobile development team may have very different testing concerns from a
team focused on operational tasks.

Below, you will find lists of code review advice that is broken down by
how applicable they are. When making your own code review cheat sheet, pick
as many or as few of the points as best fit and then stick to those as a group.
It is highly recommended to gather all team(s) who will be following the
chosen code review guidelines to choose what best fits you together. If you
do not have buy-in at the outset, it will be increasingly difficult to have
all members follow your code review cheat sheet. And lastly, do not be afraid
to fit the cheat sheet to your team(s) needs and create your own cheat sheet
do's and don'ts, the below lists are not exhaustive!

## Almost Always Applicable

* Listen to all feedback, even if you disagree with it.
* Pause and consider your response to feedback when you feel negatively
towards a commenter's opinion (active pausing).
* Trust but verify the submitter.
* Remember, we are all human and make mistakes sometimes, so assume good
intentions from the submitter. Treat the submitter as you wish to be treated.
* Don't be a jerk.
* Clearly state the goal of the code change(s).
* Verify the stated goal of the code change(s) match the ticket being worked.

## Sometimes Applicable

* Tests must pass.
* Ensure there is code coverage in the tests.
* Keep the code change(s) as small as possible. The longer the code change(s),
the greater the strain on reviewer attention spans.
* Run the code locally to ensure it does what the submitter says.
* Check the code with a code linter/validate the automated code lint run did
not find any issues.

## Niche Considerations

* Verify the code runs on all operating systems.
* Check the code changes in multiple web browsers.
* Validate the color changes follow your team/company's style guides.
