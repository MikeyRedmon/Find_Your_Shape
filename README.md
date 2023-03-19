# Find Your Shape - The Fitness Class System

## Introduction

Welcome to the fourth project; the FSD project.

I have decided to create an app that would be used by a Gym and its members to Create, Read, Update and Edit Assessments and Personal Training sessions, while also allowing
the management of the gym to Create, Read and Update classes ran by the gym on a daily basis. 

A Live website can be found here:

# Table of Contents

- [1. UX](#ux)
    - [1.1 Strategy](#strategy)
        - [Project Goals](#project-goals)
        - [User Goals](#user-goals)
        - [User Expectations](#user-expectations)
    - [1.2 Structure](#12-structure)
    - [1.3 Skeleton](#13-skeleton)
    - [1.4 Surface](#14-surface)
- [2. Features](#features)
- [3. Technology Used](#technology-used)
- [4. Testing](#testing)
- [5. Development Cycle](#development-cycle)
- [6. Deployment](#deployment)
- [7. End Project](#end-project)
- [8. Known Bugs](#bugs)
- [9. Credits](#credits)

<a name='ux'></a>

# 1 UX

[Go To Top](#table-of-contents)

As someone who goes to the gym five to six times a week, I do sometimes find myself wishing I knew when the staff might be avalible to answer a question or help out with 
a personal best. 

Sometimes I want to be able to set up an appointment with my trainer without having to drive to the gym, or call them and get nothing done. 

This project will showcase simplicity and ease of function when it comes to creating an appointment, updating an appointment, canceling an appointment and allowing Management to do the same. 

## 1.1 Strategy

[Go to Top](#table-of-contents)

### Project Goals

The main goal of this project is to allow the user to sign up, sign in/out and then Create, Read, Update and Delete their appointments. 

### User Goals:
First Time User Goals:
- As a First time User I want to be able to understand the sign up instructions
- as a First time User I want to be able to simply and easily navigate the app.

Regular User Goals: 
- As a Regular User I want to be able to edit my appointments to suit my schedule.
- As a Regular User I want to be able to cancel an appointment I've made

### User Expectations
The App should have a siomple user interface, with navigation to each section clear and concise

- The Log in menu is clear and simple with good User Feedback
- Creating, editing, deleting an item should return feedback to the user to confirm actions

## 1.2 Structure

[Go To Top](#table-of-contents)

It is important in all aspects of modern web design that you provide a responsive and sleek look to an application in order to make it as user friendly as possible.

- Responsive on all device sizes
- Easy Navigation
- Footer at the bottom with social media websites
- All elements will be consistant with font size, font family and colour scheme. 

<a name='skeleton'></a>

## 1.3 Skeleton

Database Structure: 

```python
class hiitbook(models.Model):
    name = models.CharField(max_length=10, null=False, blank=False)
    focus = models.CharField(max_length=50, null=False, blank=False)
    time = models.DateTimeField(max_length=10)

    def __str__(self):
        return self.name


class SpinClasses(models.Model):
    name = models.CharField(max_length=10, null=False, blank=False)
    genre = models.CharField(max_length=10, null=False, blank=False)
    time = models.DateTimeField(max_length=10)

    def __str__(self):
        return self.name


class hittclasses(models.Model):
    name = models.CharField(max_length=10, null=False, blank=False)
    trainer = models.CharField(max_length=10, null=False, blank=False)
    focus = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name


class PtClasses(models.Model):
    name = models.CharField(max_length=10, null=False, blank=False)
    trainer = models.CharField(max_length=10, null=False, blank=False)
    focus = models.CharField(max_length=50, null=False, blank=False)
    time = models.DateTimeField(null=False, blank=False)

    def __str__(self):
        return self.name
```

<a name='surface'></a>

## 1.4 Surface

### Colours

Please find the colours I used [here](https://coolors.co/000000-ffd700-e7e4e4-7b3f00-0000ff)

### Typography

I went with two seperate fonts; Oswald for Headings with Raleway used for everything else. 

You can find [Oswald](https://fonts.google.com/specimen/Oswald) And [Raleway](https://fonts.google.com/specimen/Raleway) at these links