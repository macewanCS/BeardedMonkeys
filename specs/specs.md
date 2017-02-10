### PROJECT DESCRIPTION:

   The Edmonton Public Library’s IT Department currently handles every electronically-submitted issue ticket with very outdated 
software, causing several difficulties:

- Tickets cannot be directly submitted, instead being created automatically when an email is sent to a certain address

o	Users cannot edit or close their own tickets 

o	Tickets often lack required information, which is difficult to acquire when working on the ticket due to varying employee 
  schedules
  
o	It’s very difficult for users to track their own tickets and know when said ticket is being worked on

   The purpose of the project is to build a webpage that can tie into EPL IT’s SQL database and provide a system to facilitate 
submission and management of issue tickets. 

   The webpage should only handle the submission and surface-level management of tickets; all IT workflow is outside of the 
project’s scope. It has to write the tickets to the existing SQL database as well as allow existing tickets to be modified, 
but cannot otherwise alter anything about the database. 



### REQUIREMENTS:

Functional: 

o	User can log-in to personal profile

o	Users can submit tickets

o	Users are guided through submission of tickets, including branching submission paths for different ticket categories

o	Submitted tickets contain all required information for their category

o	User profile tracks their previously submitted tickets and allows ticket management (including altering information or 
  closing tickets as needed)
  
o	Users can see (non-private details of) previously submitted tickets from other users

o	Managers can edit tickets from all users within their branch

### Technical:

o	System is web-based

o	Accessible with all major browsers – Internet Explorer/Edge, Firefox, Chrome, Safari

o	Supported on computer and mobile platforms

o	System can handle large numbers of tickets simultaneously (upwards of 200)

o	System can access existing tickets for users to edit

o	Tickets (submissions and modifications) are written to existing SQL database for management by IT Department 

### Usability:

o	System will be usable by all major browsers

o	System will have mobile support

o	System aids users in creating, submitting, and editing tickets

### WORKFLOW/SYSTEM DESCRIPTION:

   The web interface will closely follow the established style of the EPL. When the user logs in to the system, they are taken to 
their personal profile page, which presents a video demonstration of how to use the system. From there the user can submit 
tickets, as well as manage their submitted tickets and view the tickets that others in their branch have submitted.

   The user can submit a ticket for issues belonging to one of five categories: Password reset; hardware issues; 
system/software issues; service requests; and general/other questions. Each type of ticket has certain details that must be 
provided to allow the user to submit the ticket, as the issue will not be solvable without the attending technician knowing 
those details. 

   The user can also view all of the tickets that they’ve already submitted, as well as the tickets submitted by other users in 
their branch. This view provides several details of each ticket, including the ticket ID, the submitter’s username, the date of
submission, the ticket status (“Open”, “in progress”, or “closed”), the issue category, and a short description of the issue. 
They will be able to sort and filter the tickets by these parameters (save the ID and the description). Should the user wish to 
edit or close one of their tickets, they need simply select the relevant ticket from the list.

   If the user is the manager of a branch, they will be able to edit the tickets of any user in their branch. Regular users will
only be allowed to edit their own tickets.

   The system will not allow the viewing nor access of tickets in the database that were not submitted through the system, as 
these tickets often contain sensitive information (as in the case of HR tickets).
