# PRD for 26 Sept Version

|Target release|Sep 26, 2023|
|---|---|
|Epic|Type /Jira to add Jira epics and issues|
|Document status|Ongoing|
|Document owner|@Siddhartha Kala (Unlicensed)|
|Designer|@Akshay Jadhav|
|Tech lead|@Santosh Gorale|
|Technical writers|@Bhanu Pratap Singh @Varun Mathur|
|QA|@Medha Bhatnagar|

##  Objective

Provide context on the various features being released as part of the product launch targeted for 26th September 2023 release
##  Assumptions

Before releasing the requirements, detailed discussions with various stake-holders have been conducted and relevant approvals have been

granted.
##  Requirements













|Requirement|Anchor Link|User Story|Importan ce|Design Ticket|Delivery Tickets|Notes|Col8|
|---|---|---|---|---|---|---|---|
|In-app Notifications on web and mobile|Approv ed Notificati on|As a registered user, I should receive important in- app notifications through a dedicated notifications section|HIGH|TPD -40|TA-1440 TA-1465: QA|||
|Guest User Home Page|Approv ed Guest User Home Page|As a new user, I should land on the guest user home page which provides easy|HIGH|TPD- 79: Gue st User Home P age HAND-OFF D|TA-1432 TA-1461: QA ONE|||


-----

|Col1|Col2|access to sign-up, login, and parts of the content and app|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|Enhanced Signup Flow and Experience|Approv ed Enhance d Signup Flow and Experien ce|As a New User I should be able to utilize Social Sign-in options. In Addition, I need further help thus making onboarding and verification through email easier.|HIGH|TPD-85 TPD-56|TA-1437 TA-1464: QA TA-1439|||
|Location based filtering for activities|Approv ed Location based filtering for activities|As a User, I should be able to filter Activities based on Provider Communities, Mode and Location|HIGH|TPD-67|TA-1463|||

##  Notifications

**FUNCTIONAL REQUIREMENTS**

**Impacted Users:**

**Member - Users of the Platform**

**Partner**

**Requirements:**



The notifications feature is accessible through the notifications icon in the menu on both web and mobile browser.

**Activities notifications** 
As an event participating member, I should receive in-app notification 30 minutes before the event

As an event participating member, I should receive in-app and email notifications in case an event or activity is cancelled

As an event participating member, I should receive in-app notifications upon major event changes such as - location, date/time, link

or description update

As a member, if I join/RSVP an event or activity, I should be added to the event chat group automatically, and should receive chat

group joining notification in the notifications panel, as well as the chat icon.

As a Member, When I click Notifications icon I should be able to see 4 (New + Unread ) latest notifications. And If I want to see all

notification, I should click on “See All Notifications“ which should take up to listed Notifications page.

New Notifications - Any notifications which have come in since the user lasted visited the application.


-----

Unread Notifications - Any Notifications which have not been click/read by the user will be categorized under Unread.

Unread Notifications are shown with Blue Dots against them.

@Akshay Jadhav  Please confirm this once.

Notifications should be shown in reverse chronological order ( recent first).

**Partner notification -** As a partner, I should receive a notification on the notifications panel and via email if the super-admin deletes

an activity created by me. The participating member should receive the usual activity cancelled notification.

**General Notifications -**

As a user, when i open the notifications, the number on top of the notifications icon should get cleared, and the count for new

notifications should be reset

~~New~~ ~~content~~ ~~uploaded~~

~~**Notifications**~~ ~~**Controls**~~ ~~**-**~~ ~~**TBD**~~

~~The~~ ~~user~~ ~~should~~ ~~be~~ ~~able~~ ~~to~~ ~~mute~~ ~~notifications~~ ~~upto~~ ~~some~~ ~~extent~~

~~The~~ ~~user~~ ~~should~~ ~~be~~ ~~able~~ ~~to~~ ~~clear~~ ~~or~~ ~~delete~~ ~~notifications~~

**OUT OF SCOPE**

This does not include in-chat notifications, which should be shared separately

This does not include email notifications, these should be carried out same as before, and if required, more details will be shared

separately

Push notifications, browser notifications, native notifications on laptop and mobile devices are not being considered in the current scope.

Notifications specific for **Partners and Super Admin, Guest Users** of the application.

**Exception**    - Notification for activity deletion done by super-admin should be received on the notifications panel and email by the

partner
##  Guest User Home Page

**GOALS**

Provide a great landing page for new or existing (logged-out) members who are either visiting the app for the first time, or, coming back

to explore more, signup or login

Provide easy signup access to new visitors

Provide easy access to login to signup-visitors

Enable first-time or guest visitors to explore core features and functionality without having to sign up

Provide a glimpse of what the app has to offer in terms of socialising, activities, content, and more

**FUNCTIONAL REQUIREMENTS**

As a guest visitor, I would like to see what core features the TA Plus app has to offer

As a guest visitor, I should be able to discover activities, living options, articles and posts, etc right on the home page without having to

sign up

As I guest visitor, I should be able to explore activities and events, but should be required to sign-up if I try to RSVP to an event/activity

As a guest user, I should be able to navigate through the core pages of the app like living options, and activities page with limited

functionality.

As a guest user, I should be able to use the support functionality through the **Get Help** button on the menu bar

As a guest user, I should be able to easily find and sign up using the social sign up buttons on the landing page.

This would need A/B Testing.

Ideally we would have a simple Guest Page and the other option would be to show Social Signup Buttons to certain users.

As an existing member, I should be able to find and login using the primary login button.


-----

As a guest user, I should be able be able to get a glimpse of what the app looks like and offers, by simply scrolling down or by using the

**Explore More** button

As a guest user, I **should not** have access to the My Events page, or any other relevant pages that require a user to be sign-in

As a guest user, I should be redirected to login/signup pages if I try to use restricted content or activities

As a guest user, I should be able to see live and upcoming activities in the relevant section.

The live event should have highest precedence and should be placed before any of the upcoming event

If there are multiple live events, highest precedence should be given to the event that started the at the earliest. If two or more live

events started at the same time, then they should be arranged in alphabetical order.

If there are multiple upcoming events, the highest precedence should be given to the most recent upcoming event.

**OUT OF SCOPE**

This does not take into account the updated navigation or menu changes **EXCEPT**  
The updated Get Help button on the menu bar

The updated primary Login button on the top right of the menu bar

This does not take into account any impending changes to the content cards

Nothing on comments and likes has been finalised yet - This may be added soon enough but need to be confirmed.
# Enhanced Signup Flow and Experience
## Goal and Objective

Easier Signup and Sign-in Process

Utillizing prominent Social platforms ( Google, AppleId, Facebook, Amazon) for ease of Sign-Up / Verification
## Target Users

Member - Users of the Platform
## User Stories

As a New User, I should be able to Signup with any of the Social Sign-in’s.

As an Existing User, I should be able to link my existing Email sign-in’s to one of the Social Signin’s.

Some Discussion needed here with @Akshay Jadhav

Seems to be done Technically, but we have not looked at this as a UX flow. Requires discussion with @Santosh Gorale

As a New User, I should be able to Sign-up by providing an email Id and verify the same with ease.

As an Existing User, If I wish to change password the new Password help should be available to me thus choosing the password is

easier.

As a User, I should be able to crop my Profile image.

This could be during the Signup Flow.

Or

This should be available to Existing Users, or the once who skipped Profile completion, under profile Section as well

As a Super Admin, I should be able to understand which Social Sign-in is a User utilizing and their minimal identification details.


-----

As an existing user, I should be able to log-in using any of the social log-in options without having to verify my email or duplicate my

account multiple times

As a new user, I should be able to complete the profile details or skip them without much friction, after the email verification is done

As an existing user, I should not be required to login each time I revisit the TA Plus app.

As an existing user, I should be able to easily log-out if/when required

As an existing user, if I try to signup again using the same email ID or social login, relevant warning prompts should be shown
## Dependency

None Identified
## Release Criteria

The release Aims to

Enable Social Sing-up/Sign-in capabilities for the Member Users - This is expected to work without much friction

Ease Out challenge's faced during selecting Password

Ease Out challenge's faced during Email Verification process

Delay of Email’s being received on Users Inbox is not in-scope, since we don’t see any challenges w.r.t that.

There is monitoring in place for AWS Email Service (SES ), to identify any potential delays or bounces

Ease out challenges faced to provide right Image, thus users have a better identity on the platform.
## Out of scope

Profile Section changes

Both Partner and Member
## Metrics

**Google Analytics**

Signup method used i.e. Social, exactly which platform, and Email.

Time Taken to Signup and Complete Verification process.

Clicked Signup but never completed.
# Location based filtering for activities
## Goals and Objectives

To Support quick access to near by Activities available to the Logged In Members of Application shown on Activities page.
## Target Users

Logged in members with access to Activities Page


-----

## User Story

As a Logged in Member, I should see Filter chips for Activities in category selection by Name ( includes Image of Provider Community /

Organization and their Name ) and Online/Virtual, as well as a location dropdown which enables me to select the location by name, Zip,

or “detect current location“.

If I select a Community filter, it will Filter all activities defined by that Provider Account.

If I select a Community Filter with list of US Locations( or Zip Code), it should filter out any Activities provided by that Community in

that Location.

The List of Location shown should be from the list of Activities available on the app.

When the Locations are filtered based on input by User, the Activities on the page should as well get filtered.

In Case User selects a different valid Location, for which no Activity is present on the App. The Location should still show up

however Activities page should show “No results found“.

In case User selects an invalid Location, we should “No results found“ on the suggestion box itself.

@Siddhartha Kala (Unlicensed) Please review this.

Similarly, If I select a Community Filter with Online Activities filter, it will Filter All the Activities provided by that Provider which are

Virtual.

If only a Zip or area name is selected from the dropdown, the page should show all the relevant results from that location. As a

member, I should be then able to use the filter chips to filter the results by Partner name, and Online/Virtual

For example, If “Seattle“ is selected as a location, the results should show all listings for Seattle area. And when the user applies a

filter for Fred Lind Manor (FLM), the results should show all the listings for Fred Lind Manor that are from Seattle area

As a logged in member, when no filter is applied the default activities page should show all the activities listings as before

As a logged in member, i should see a “No results found“ page if no results are available after applying the filters

As a Logged in member, When I Click on Use “My current location” icon in the location dropdown, the Browser should prompt access .

Once accepted the identified Zip Code or Area should get selected.

This should impact the Filtering of listed Activities.
## Dependency

Browser Location capabilities
## Out of Scope

Activities Recommendation shown on Home Page based on Default location based on profile Zip Code or Browser/IP based location

identification.

Location based identification through Ip Address.

Defaulting or Suggesting Activities by default, based on defaulting location through Profile’s Zip Code or Browser Location Identification

automatically.


-----

