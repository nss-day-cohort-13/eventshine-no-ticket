##### No ticket?
# **TIxIT!**
---
## What is TIxIT?
#### The Description
TIxIT is a simple app allowing users to create, find, and buy tickets for events. TIxIT is unlimited: Users can create any kind of event, happening on any scale from an arena rock concert to a small house-party built around board-gaming.
#### The Reality
TIxIT is an in-class group project from a small team of students at Nashville Software School. It was written over a week in late August, 2016 using AngularJS, Python 3.4.0,  and Django 1.10. Django handles user creation/registration and authentication. AngularBootstrap handles site styling.
#### The Team
**Team Lead**: The Incomparable **Whitney Mitchell**
* distributed source code control
* UI lead

The Deadly **Mike Mead**
* database functionality
* made Angular play with Django

The Sartorial **Damon Romano**
* UX/solution design
* documentation
* support dev

---
#### The Assignment
Following are the directives we received from our instructors at NSS, including  requirements for what the project must do and properties it must have...

##### Event Ticketing System
Your mission is to design, model, and build a Django application that allows users to purchase a ticket to an event, and allows a user to create an event.

## Event

The event will need the following properties. You may add more as you see fit.

1. Name
1. Description
1. City
1. Begin date/time
1. End date/time
1. Attendee limit
1. Venue

## Venue

It's possible that there can be many events going on at a single venue at any point in time, so keep that in consideration.

## User

Any user can register for any number of events, but if the user mistakenly overbooks their time, provide a notification when they log in to that effect. Use built-in Django [user authentication model](https://docs.djangoproject.com/en/1.10/topics/auth/default/#creating-users) to allow users to create a new account in your application.

> **Note:** Make sure you enable the [SessionMiddleware](https://docs.djangoproject.com/en/1.10/topics/http/sessions/) for your application.

# Stretch Goals

## Presenters

Allow a user to register as a present at an event. The user must provide the name of their talk and the time at which they would like to present. Ensure that any given time slot is not double-booked.

## Sponsors

When creating an event, let the user indicate that it is possible for other users to sponsor the event.

Allow users to indiciate that they wish to sponsor the event. The user will provide their company information, the amount of money they wish to donate for sponsorship, and their company logo.

---
License
---
Copyright (c) 2016 Whitney Mitchell, Mike Mead, & Damon Romano.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
