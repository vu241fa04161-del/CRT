import os
import django

# Setup Django Environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'onlinequiz.settings')
django.setup()

from django.contrib.auth.models import User
from messages1.models import Quiz, Question

def seed():
    print("Starting database seeding...")

    # Clear existing quizzes & questions to avoid duplicates
    Question.objects.all().delete()
    Quiz.objects.all().delete()

    quizzes_data = [
        {
            'title': 'HTML5 Essentials',
            'description': 'Test your knowledge on modern HTML5 markup, elements, and semantics.',
            'category': 'HTML',
            'level': 'Simple',
            'time_limit': 15,
            'questions': [
                {
                    'question': 'Which HTML5 element is used to define semantic navigation links?',
                    'option1': '<nav>',
                    'option2': '<navigation>',
                    'option3': '<links>',
                    'option4': '<menu>',
                    'correct_answer': '<nav>',
                    'marks': 2
                },
                {
                    'question': 'What does HTML stand for?',
                    'option1': 'Hyper Text Markup Language',
                    'option2': 'Home Tool Markup Language',
                    'option3': 'Hyperlink and Text Markup Language',
                    'option4': 'Hyperactive Textual Markup Language',
                    'correct_answer': 'Hyper Text Markup Language',
                    'marks': 2
                },
                {
                    'question': 'Which tag is used to embed a native video in HTML5?',
                    'option1': '<embed>',
                    'option2': '<media>',
                    'option3': '<video>',
                    'option4': '<source>',
                    'correct_answer': '<video>',
                    'marks': 2
                },
                {
                    'question': 'Which HTML attribute is used to define inline styles?',
                    'option1': 'class',
                    'option2': 'styles',
                    'option3': 'font',
                    'option4': 'style',
                    'correct_answer': 'style',
                    'marks': 2
                },
                {
                    'question': 'Which element represents the main content of a document?',
                    'option1': '<section>',
                    'option2': '<main>',
                    'option3': '<body>',
                    'option4': '<article>',
                    'correct_answer': '<main>',
                    'marks': 2
                },
                {
                    'question': 'Which element represents a self-contained composition (e.g. blog post, forum post, product card)?',
                    'option1': '<section>',
                    'option2': '<article>',
                    'option3': '<aside>',
                    'option4': '<div>',
                    'correct_answer': '<article>',
                    'marks': 2
                },
                {
                    'question': 'Which attribute specifies that an input field must be filled out before submitting the form?',
                    'option1': 'placeholder',
                    'option2': 'required',
                    'option3': 'validate',
                    'option4': 'constraint',
                    'correct_answer': 'required',
                    'marks': 2
                },
                {
                    'question': 'Which element is used to group a set of form controls, typically with a caption?',
                    'option1': '<group>',
                    'option2': '<fieldset>',
                    'option3': '<legend>',
                    'option4': '<form>',
                    'correct_answer': '<fieldset>',
                    'marks': 2
                },
                {
                    'question': 'What does the <canvas> element do in HTML5?',
                    'option1': 'Renders 3D audio',
                    'option2': 'Used to draw graphics on the fly via scripting',
                    'option3': 'Stores local client-side data',
                    'option4': 'Formats long code text blocks',
                    'correct_answer': 'Used to draw graphics on the fly via scripting',
                    'marks': 2
                },
                {
                    'question': 'Which HTML5 tag is used to display a measurement within a known range or a fractional value?',
                    'option1': '<progress>',
                    'option2': '<meter>',
                    'option3': '<range>',
                    'option4': '<scale>',
                    'correct_answer': '<meter>',
                    'marks': 2
                },
                {
                    'question': 'What is the correct HTML5 doctype declaration?',
                    'option1': '<!DOCTYPE html>',
                    'option2': '<!DOCTYPE HTML5>',
                    'option3': '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 5.0//EN">',
                    'option4': '<doctype html>',
                    'correct_answer': '<!DOCTYPE html>',
                    'marks': 2
                },
                {
                    'question': 'Which HTML5 element represents content that is tangentially related to the content around it, like a sidebar?',
                    'option1': '<section>',
                    'option2': '<article>',
                    'option3': '<aside>',
                    'option4': '<nav>',
                    'correct_answer': '<aside>',
                    'marks': 2
                },
                {
                    'question': 'Which input type creates a slider control in HTML5?',
                    'option1': 'type="slider"',
                    'option2': 'type="range"',
                    'option3': 'type="number"',
                    'option4': 'type="progress"',
                    'correct_answer': 'type="range"',
                    'marks': 2
                },
                {
                    'question': 'What is the purpose of the alt attribute on an <img> tag?',
                    'option1': 'Speeds up image loading',
                    'option2': 'Defines alternative stylesheet for the image',
                    'option3': 'Provides alternative text description if the image cannot be displayed',
                    'option4': 'Sets image transparency level',
                    'correct_answer': 'Provides alternative text description if the image cannot be displayed',
                    'marks': 2
                },
                {
                    'question': 'Which HTML5 element represents a caption for a <figure> element?',
                    'option1': '<figcaption>',
                    'option2': '<caption>',
                    'option3': '<legend>',
                    'option4': '<title>',
                    'correct_answer': '<figcaption>',
                    'marks': 2
                }
            ]
        },
        {
            'title': 'CSS & Responsive Design',
            'description': 'Test your CSS layout skills, Flexbox, Grid, and Media Queries properties.',
            'category': 'CSS',
            'level': 'Medium',
            'time_limit': 20,
            'questions': [
                {
                    'question': 'What does CSS stand for?',
                    'option1': 'Creative Style Sheets',
                    'option2': 'Computer Style Sheets',
                    'option3': 'Cascading Style Sheets',
                    'option4': 'Colorful Style Sheets',
                    'correct_answer': 'Cascading Style Sheets',
                    'marks': 2
                },
                {
                    'question': 'Which CSS property controls the layout alignment along the main axis in Flexbox?',
                    'option1': 'align-items',
                    'option2': 'justify-content',
                    'option3': 'flex-direction',
                    'option4': 'align-content',
                    'correct_answer': 'justify-content',
                    'marks': 2
                },
                {
                    'question': 'How do you apply a blur background effect using modern CSS backdrop filters?',
                    'option1': 'background-blur: 10px;',
                    'option2': 'filter: blur(10px);',
                    'option3': 'backdrop-filter: blur(10px);',
                    'option4': 'glassmorphism: blur(10px);',
                    'correct_answer': 'backdrop-filter: blur(10px);',
                    'marks': 2
                },
                {
                    'question': 'Which CSS selector selects all paragraph elements inside a div element?',
                    'option1': 'div p',
                    'option2': 'div.p',
                    'option3': 'div + p',
                    'option4': 'div > p',
                    'correct_answer': 'div p',
                    'marks': 2
                },
                {
                    'question': 'What is the default value of the position property in CSS?',
                    'option1': 'relative',
                    'option2': 'absolute',
                    'option3': 'static',
                    'option4': 'fixed',
                    'correct_answer': 'static',
                    'marks': 2
                },
                {
                    'question': 'What is the difference between em and rem units in CSS?',
                    'option1': 'em is relative to root font-size; rem is relative to parent element font-size',
                    'option2': 'em is relative to parent element font-size; rem is relative to root element font-size',
                    'option3': 'em is absolute; rem is relative',
                    'option4': 'em is only for margins; rem is only for fonts',
                    'correct_answer': 'em is relative to parent element font-size; rem is relative to root element font-size',
                    'marks': 2
                },
                {
                    'question': 'Which CSS layout system is designed for two-dimensional layouts (both rows and columns)?',
                    'option1': 'Flexbox',
                    'option2': 'Grid',
                    'option3': 'Float',
                    'option4': 'Positioning',
                    'correct_answer': 'Grid',
                    'marks': 2
                },
                {
                    'question': 'What does the z-index property control?',
                    'option1': 'Zoom level of an element',
                    'option2': 'Horizontal position',
                    'option3': 'Vertical position',
                    'option4': 'Stack order of positioned elements',
                    'correct_answer': 'Stack order of positioned elements',
                    'marks': 2
                },
                {
                    'question': 'Which media query feature is commonly used to target styles for screens with a maximum width of 768px?',
                    'option1': 'screen-width: 768px',
                    'option2': 'max-width: 768px',
                    'option3': 'device-width: 768px',
                    'option4': 'limit-width: 768px',
                    'correct_answer': 'max-width: 768px',
                    'marks': 2
                },
                {
                    'question': 'What does the box-sizing: border-box; property do?',
                    'option1': "Excludes padding and border from the element's total width and height",
                    'option2': "Includes padding and border in the element's total width and height",
                    'option3': 'Sets the border color to match the box',
                    'option4': 'Removes all margins',
                    'correct_answer': "Includes padding and border in the element's total width and height",
                    'marks': 2
                },
                {
                    'question': 'Which CSS property is used to make text bold?',
                    'option1': 'font-style',
                    'option2': 'font-weight',
                    'option3': 'text-bold',
                    'option4': 'font-variant',
                    'correct_answer': 'font-weight',
                    'marks': 2
                },
                {
                    'question': 'Which selector matches an element only when it is being hovered over by the mouse pointer?',
                    'option1': ':active',
                    'option2': ':hover',
                    'option3': ':focus',
                    'option4': ':visited',
                    'correct_answer': ':hover',
                    'marks': 2
                },
                {
                    'question': 'How do you center a block-level element horizontally inside its container using margins?',
                    'option1': 'margin: auto 0;',
                    'option2': 'margin: 0 auto;',
                    'option3': 'margin-left: 50%;',
                    'option4': 'margin: center;',
                    'correct_answer': 'margin: 0 auto;',
                    'marks': 2
                },
                {
                    'question': 'Which value of the display property makes an element behave like a block element but flow inline with surrounding content?',
                    'option1': 'inline',
                    'option2': 'block',
                    'option3': 'inline-block',
                    'option4': 'flex-inline',
                    'correct_answer': 'inline-block',
                    'marks': 2
                },
                {
                    'question': 'What is the CSS property to change the background color of an element?',
                    'option1': 'color',
                    'option2': 'background-color',
                    'option3': 'bgcolor',
                    'option4': 'fill-color',
                    'correct_answer': 'background-color',
                    'marks': 2
                },
                {
                    'question': 'In Grid Layout, which property defines the size of the grid columns?',
                    'option1': 'grid-template-rows',
                    'option2': 'grid-template-columns',
                    'option3': 'grid-column-gap',
                    'option4': 'grid-columns-size',
                    'correct_answer': 'grid-template-columns',
                    'marks': 2
                },
                {
                    'question': 'Which CSS transition property specifies how long the transition effect should take to complete?',
                    'option1': 'transition-delay',
                    'option2': 'transition-duration',
                    'option3': 'transition-timing-function',
                    'option4': 'transition-property',
                    'correct_answer': 'transition-duration',
                    'marks': 2
                },
                {
                    'question': 'What is the CSS selector to select all elements with the class name "btn"?',
                    'option1': '#btn',
                    'option2': '.btn',
                    'option3': '*btn',
                    'option4': 'btn',
                    'correct_answer': '.btn',
                    'marks': 2
                },
                {
                    'question': 'Which CSS property determines whether an element is visible or hidden, while still occupying its original space in the layout?',
                    'option1': 'display',
                    'option2': 'visibility',
                    'option3': 'opacity',
                    'option4': 'transform',
                    'correct_answer': 'visibility',
                    'marks': 2
                },
                {
                    'question': 'What is the purpose of the @keyframes rule in CSS?',
                    'option1': 'To define a new font',
                    'option2': 'To specify CSS variables',
                    'option3': 'To create CSS animations by defining styles at various stages',
                    'option4': 'To import external stylesheets',
                    'correct_answer': 'To create CSS animations by defining styles at various stages',
                    'marks': 2
                }
            ]
        },
        {
            'title': 'JavaScript Core & ES6',
            'description': 'Assess your understanding of Javascript variables, arrays, scope, and async methods.',
            'category': 'JavaScript',
            'level': 'Medium',
            'time_limit': 20,
            'questions': [
                {
                    'question': 'Which keyword is used to declare block-scoped variables in modern JavaScript?',
                    'option1': 'var',
                    'option2': 'let',
                    'option3': 'const',
                    'option4': 'Both let and const',
                    'correct_answer': 'Both let and const',
                    'marks': 2
                },
                {
                    'question': 'What is the output of "typeof null" in JavaScript?',
                    'option1': '"null"',
                    'option2': '"undefined"',
                    'option3': '"object"',
                    'option4': '"number"',
                    'correct_answer': '"object"',
                    'marks': 2
                },
                {
                    'question': 'Which method is used to add one or more elements to the end of an array and returns the new length?',
                    'option1': 'push()',
                    'option2': 'pop()',
                    'option3': 'shift()',
                    'option4': 'unshift()',
                    'correct_answer': 'push()',
                    'marks': 2
                },
                {
                    'question': 'Which operator is used to compare both value and data type in JavaScript?',
                    'option1': '==',
                    'option2': '===',
                    'option3': '=',
                    'option4': '!=',
                    'correct_answer': '===',
                    'marks': 2
                },
                {
                    'question': 'How do you create a promise in JavaScript?',
                    'option1': 'new Promise((resolve, reject) => { })',
                    'option2': 'Promise.create((resolve, reject) => { })',
                    'option3': 'new Promise(resolve, reject)',
                    'option4': 'Promise.new((resolve, reject) => { })',
                    'correct_answer': 'new Promise((resolve, reject) => { })',
                    'marks': 2
                },
                {
                    'question': 'What is the output of console.log(2 + "2") in JavaScript?',
                    'option1': '"4"',
                    'option2': '4',
                    'option3': '"22"',
                    'option4': 'NaN',
                    'correct_answer': '"22"',
                    'marks': 2
                },
                {
                    'question': 'Which ES6 feature allows you to extract properties from an object and bind them to variables?',
                    'option1': 'Spreading',
                    'option2': 'Destructuring',
                    'option3': 'Serialization',
                    'option4': 'Extraction',
                    'correct_answer': 'Destructuring',
                    'marks': 2
                },
                {
                    'question': 'How does an arrow function handle the "this" keyword?',
                    'option1': 'It binds "this" to the global object',
                    'option2': 'It has its own "this" binding',
                    'option3': 'It inherits "this" from the enclosing lexical context',
                    'option4': 'It cannot use the "this" keyword',
                    'correct_answer': 'It inherits "this" from the enclosing lexical context',
                    'marks': 2
                },
                {
                    'question': 'Which method creates a new array with all elements that pass the test implemented by the provided function?',
                    'option1': 'map()',
                    'option2': 'filter()',
                    'option3': 'reduce()',
                    'option4': 'every()',
                    'correct_answer': 'filter()',
                    'marks': 2
                },
                {
                    'question': 'What is the output of console.log(NaN === NaN)?',
                    'option1': 'true',
                    'option2': 'false',
                    'option3': 'undefined',
                    'option4': 'TypeError',
                    'correct_answer': 'false',
                    'marks': 2
                },
                {
                    'question': 'Which mechanism in JavaScript moves variable and function declarations to the top of their containing scope before code execution?',
                    'option1': 'Hoisting',
                    'option2': 'Lifting',
                    'option3': 'Seeding',
                    'option4': 'Elevating',
                    'correct_answer': 'Hoisting',
                    'marks': 2
                },
                {
                    'question': 'What is the purpose of the Set object in ES6?',
                    'option1': 'To store key-value pairs',
                    'option2': 'To store unique values of any type',
                    'option3': 'To execute a callback function',
                    'option4': 'To format date and time',
                    'correct_answer': 'To store unique values of any type',
                    'marks': 2
                },
                {
                    'question': 'Which operator is used to unpack elements of an array or properties of an object in ES6?',
                    'option1': 'Rest operator',
                    'option2': 'Spread operator',
                    'option3': 'Split operator',
                    'option4': 'Unpack operator',
                    'correct_answer': 'Spread operator',
                    'marks': 2
                },
                {
                    'question': 'How do you handle asynchronous operations in synchronous-looking code using ES8 features?',
                    'option1': 'callbacks',
                    'option2': 'Promises',
                    'option3': 'async/await',
                    'option4': 'generators',
                    'correct_answer': 'async/await',
                    'marks': 2
                },
                {
                    'question': 'What is the value of x after: let x = 10; { let x = 20; }?',
                    'option1': '10',
                    'option2': '20',
                    'option3': 'undefined',
                    'option4': 'ReferenceError',
                    'correct_answer': '10',
                    'marks': 2
                },
                {
                    'question': 'Which method is used to convert a JavaScript object into a JSON string?',
                    'option1': 'JSON.parse()',
                    'option2': 'JSON.stringify()',
                    'option3': 'JSON.toString()',
                    'option4': 'JSON.serialize()',
                    'correct_answer': 'JSON.stringify()',
                    'marks': 2
                },
                {
                    'question': "What does the 'use strict' directive do at the beginning of a JavaScript file?",
                    'option1': 'Enables strict type checking',
                    'option2': 'Enforces strict syntax rules and catches common mistakes',
                    'option3': 'Prevents the use of external packages',
                    'option4': 'Runs the script in a web worker',
                    'correct_answer': 'Enforces strict syntax rules and catches common mistakes',
                    'marks': 2
                },
                {
                    'question': 'What is a closure in JavaScript?',
                    'option1': 'A function that returns another function',
                    'option2': 'A way to close a database connection',
                    'option3': 'A function combined with references to its surrounding state',
                    'option4': 'A built-in class for cryptography',
                    'correct_answer': 'A function combined with references to its surrounding state',
                    'marks': 2
                },
                {
                    'question': 'Which statement about const is true in JavaScript?',
                    'option1': 'It creates an immutable value',
                    'option2': 'It prevents the re-assignment of the variable identifier',
                    'option3': 'It automatically freezes objects',
                    'option4': 'It has function scope',
                    'correct_answer': 'It prevents the re-assignment of the variable identifier',
                    'marks': 2
                },
                {
                    'question': 'What is the result of Boolean("false") in JavaScript?',
                    'option1': 'true',
                    'option2': 'false',
                    'option3': 'null',
                    'option4': 'undefined',
                    'correct_answer': 'true',
                    'marks': 2
                }
            ]
        },
        {
            'title': 'Python Fundamentals',
            'description': 'Test your Python coding, data types, loops, lists, and function scopes.',
            'category': 'Python',
            'level': 'Simple',
            'time_limit': 15,
            'questions': [
                {
                    'question': 'What is the correct syntax to output "Hello World" in Python?',
                    'option1': 'p("Hello World")',
                    'option2': 'print("Hello World")',
                    'option3': 'echo "Hello World"',
                    'option4': 'System.out.println("Hello World")',
                    'correct_answer': 'print("Hello World")',
                    'marks': 2
                },
                {
                    'question': 'Which data type is mutable in Python?',
                    'option1': 'tuple',
                    'option2': 'string',
                    'option3': 'list',
                    'option4': 'integer',
                    'correct_answer': 'list',
                    'marks': 2
                },
                {
                    'question': 'How do you define a function in Python?',
                    'option1': 'function myFunc():',
                    'option2': 'def myFunc():',
                    'option3': 'void myFunc():',
                    'option4': 'define myFunc():',
                    'correct_answer': 'def myFunc():',
                    'marks': 2
                },
                {
                    'question': 'What is the correct file extension for Python files?',
                    'option1': '.py',
                    'option2': '.pyt',
                    'option3': '.pyw',
                    'option4': '.pt',
                    'correct_answer': '.py',
                    'marks': 2
                },
                {
                    'question': 'Which of the following is used to handle exceptions in Python?',
                    'option1': 'try...catch',
                    'option2': 'try...except',
                    'option3': 'throw...catch',
                    'option4': 'try...finally',
                    'correct_answer': 'try...except',
                    'marks': 2
                },
                {
                    'question': 'What is the output of print(type(5.0)) in Python?',
                    'option1': "<class 'int'>",
                    'option2': "<class 'float'>",
                    'option3': "<class 'double'>",
                    'option4': "<class 'number'>",
                    'correct_answer': "<class 'float'>",
                    'marks': 2
                },
                {
                    'question': 'How do you add an element to the end of a list in Python?',
                    'option1': 'add()',
                    'option2': 'append()',
                    'option3': 'push()',
                    'option4': 'insert()',
                    'correct_answer': 'append()',
                    'marks': 2
                },
                {
                    'question': 'Which of the following statements about dictionary keys in Python is correct?',
                    'option1': 'They must be mutable',
                    'option2': 'They must be immutable',
                    'option3': 'They must be lists',
                    'option4': 'They can be of any data type',
                    'correct_answer': 'They must be immutable',
                    'marks': 2
                },
                {
                    'question': 'What is the result of 2 ** 3 in Python?',
                    'option1': '6',
                    'option2': '8',
                    'option3': '9',
                    'option4': '5',
                    'correct_answer': '8',
                    'marks': 2
                },
                {
                    'question': 'How do you start a single-line comment in Python?',
                    'option1': '//',
                    'option2': '/*',
                    'option3': '#',
                    'option4': '--',
                    'correct_answer': '#',
                    'marks': 2
                },
                {
                    'question': 'Which built-in function returns the number of items in a collection?',
                    'option1': 'count()',
                    'option2': 'size()',
                    'option3': 'len()',
                    'option4': 'length()',
                    'correct_answer': 'len()',
                    'marks': 2
                },
                {
                    'question': 'What is the output of bool([]) in Python?',
                    'option1': 'True',
                    'option2': 'False',
                    'option3': 'None',
                    'option4': 'TypeError',
                    'correct_answer': 'False',
                    'marks': 2
                },
                {
                    'question': 'How can you write a list comprehension to create a list of squares of numbers from 0 to 4?',
                    'option1': '[x*x for x in range(5)]',
                    'option2': '[x*2 for x in list(5)]',
                    'option3': 'x*x for x in range(4)',
                    'option4': '{x*x for x in 5}',
                    'correct_answer': '[x*x for x in range(5)]',
                    'marks': 2
                },
                {
                    'question': 'What is the purpose of the global keyword in Python?',
                    'option1': 'To make a variable accessible in other modules',
                    'option2': 'To bind a local variable to a global scope inside a function',
                    'option3': 'To declare a class-level variable',
                    'option4': 'To initialize a variable to None',
                    'correct_answer': 'To bind a local variable to a global scope inside a function',
                    'marks': 2
                },
                {
                    'question': 'Which keyword is used to import a specific attribute or function from a module in Python?',
                    'option1': 'import',
                    'option2': 'load',
                    'option3': 'from',
                    'option4': 'include',
                    'correct_answer': 'from',
                    'marks': 2
                }
            ]
        },
        {
            'title': 'Django MVC Web Framework',
            'description': 'Challenge your understanding of Django Models, Views, Templates, and URLs.',
            'category': 'Django',
            'level': 'Hard',
            'time_limit': 25,
            'questions': [
                {
                    'question': 'Which file handles database mappings and schema definitions in Django?',
                    'option1': 'views.py',
                    'option2': 'models.py',
                    'option3': 'urls.py',
                    'option4': 'admin.py',
                    'correct_answer': 'models.py',
                    'marks': 2
                },
                {
                    'question': 'What command is used to run the Django local development server?',
                    'option1': 'python manage.py runserver',
                    'option2': 'python manage.py startserver',
                    'option3': 'django-admin devserver',
                    'option4': 'python dev.py',
                    'correct_answer': 'python manage.py runserver',
                    'marks': 2
                },
                {
                    'question': 'Which architectural pattern does Django closely follow?',
                    'option1': 'MVC (Model-View-Controller)',
                    'option2': 'MVVM (Model-View-ViewModel)',
                    'option3': 'MVT (Model-View-Template)',
                    'option4': 'MVP (Model-View-Presenter)',
                    'correct_answer': 'MVT (Model-View-Template)',
                    'marks': 2
                },
                {
                    'question': 'What is the command to create database migration scripts in Django?',
                    'option1': 'python manage.py migrate',
                    'option2': 'python manage.py makemigrations',
                    'option3': 'python manage.py syncdb',
                    'option4': 'django-admin migration',
                    'correct_answer': 'python manage.py makemigrations',
                    'marks': 2
                },
                {
                    'question': 'Which Django package is used by default to manage user sessions and login status?',
                    'option1': 'django.contrib.auth',
                    'option2': 'django.contrib.sessions',
                    'option3': 'django.contrib.admin',
                    'option4': 'Both auth and sessions',
                    'correct_answer': 'Both auth and sessions',
                    'marks': 2
                },
                {
                    'question': 'In a Django settings file, what does the INSTALLED_APPS list contain?',
                    'option1': 'Path to database files',
                    'option2': 'List of enabled Django applications',
                    'option3': 'Middleware classes',
                    'option4': 'Third-party python libraries imported',
                    'correct_answer': 'List of enabled Django applications',
                    'marks': 2
                },
                {
                    'question': 'Which template tag is used to display the value of a variable named username in Django?',
                    'option1': '{% username %}',
                    'option2': '{{ username }}',
                    'option3': '{# username #}',
                    'option4': '<%= username %>',
                    'correct_answer': '{{ username }}',
                    'marks': 2
                },
                {
                    'question': 'How do you register a model named Quiz with the Django Admin site?',
                    'option1': 'admin.site.register(Quiz)',
                    'option2': 'admin.register(Quiz)',
                    'option3': 'Quiz.register()',
                    'option4': 'admin.site.add(Quiz)',
                    'correct_answer': 'admin.site.register(Quiz)',
                    'marks': 2
                },
                {
                    'question': 'Which ORM method is used to retrieve a single object from the database that matches a given lookup?',
                    'option1': 'Quiz.objects.filter()',
                    'option2': 'Quiz.objects.get()',
                    'option3': 'Quiz.objects.find()',
                    'option4': 'Quiz.objects.first()',
                    'correct_answer': 'Quiz.objects.get()',
                    'marks': 2
                },
                {
                    'question': 'What is the primary purpose of Django middleware?',
                    'option1': 'To render HTML templates',
                    'option2': 'To run database migrations',
                    'option3': 'To process requests and responses globally before or after view execution',
                    'option4': 'To serve static media files',
                    'correct_answer': 'To process requests and responses globally before or after view execution',
                    'marks': 2
                },
                {
                    'question': 'Which template tag is required inside HTML forms in Django to prevent Cross-Site Request Forgery?',
                    'option1': '{% csrf_token %}',
                    'option2': '{{ csrf_token }}',
                    'option3': '{% csrf %}',
                    'option4': '{% csrf_protection %}',
                    'correct_answer': '{% csrf_token %}',
                    'marks': 2
                },
                {
                    'question': 'What does the command "python manage.py migrate" do?',
                    'option1': 'Creates new python script files for database schema changes',
                    'option2': 'Applies migrations to the database to sync the database state with models',
                    'option3': 'Deletes all table records',
                    'option4': 'Installs new Django dependencies',
                    'correct_answer': 'Applies migrations to the database to sync the database state with models',
                    'marks': 2
                },
                {
                    'question': 'What is the default port used by Djangos local development server?',
                    'option1': '5000',
                    'option2': '3000',
                    'option3': '8000',
                    'option4': '8080',
                    'correct_answer': '8000',
                    'marks': 2
                },
                {
                    'question': "How does a function-based view in Django receive the client's request data?",
                    'option1': 'Via a global variable g.request',
                    'option2': "As the first parameter (usually named 'request')",
                    'option3': 'From a context manager',
                    'option4': 'Through django.request import',
                    'correct_answer': "As the first parameter (usually named 'request')",
                    'marks': 2
                },
                {
                    'question': 'Which field type should be used in a Django Model to establish a one-to-many relationship?',
                    'option1': 'OneToOneField',
                    'option2': 'ForeignKey',
                    'option3': 'ManyToManyField',
                    'option4': 'RelatedField',
                    'correct_answer': 'ForeignKey',
                    'marks': 2
                },
                {
                    'question': 'Which ORM lookup is used to perform a case-insensitive search matching a substring (e.g. contains)?',
                    'option1': '__contains',
                    'option2': '__icontains',
                    'option3': '__like',
                    'option4': '__match',
                    'correct_answer': '__icontains',
                    'marks': 2
                },
                {
                    'question': 'What is the purpose of Djangos urls.py file?',
                    'option1': 'To store database credentials',
                    'option2': 'To map URL patterns to the appropriate views',
                    'option3': 'To configure static file hosting',
                    'option4': 'To handle HTTP redirect requests',
                    'correct_answer': 'To map URL patterns to the appropriate views',
                    'marks': 2
                },
                {
                    'question': 'In a Django template, how do you loop over a list of quizzes?',
                    'option1': '{% loop quiz in quizzes %}',
                    'option2': '{% for quiz in quizzes %}',
                    'option3': '{# for quiz in quizzes #}',
                    'option4': '@foreach(quizzes as quiz)',
                    'correct_answer': '{% for quiz in quizzes %}',
                    'marks': 2
                },
                {
                    'question': 'Which class is the base class for Django forms that automatically generate fields from a database model?',
                    'option1': 'forms.Form',
                    'option2': 'forms.ModelForm',
                    'option3': 'forms.DBForm',
                    'option4': 'models.ModelForm',
                    'correct_answer': 'forms.ModelForm',
                    'marks': 2
                },
                {
                    'question': 'What is the role of settings.py in a Django project?',
                    'option1': "It contains the project's view functions",
                    'option2': 'It defines the HTML template structure',
                    'option3': 'It holds configuration settings for the entire project',
                    'option4': 'It maps URLs to views',
                    'correct_answer': 'It holds configuration settings for the entire project',
                    'marks': 2
                },
                {
                    'question': 'Which method should be overridden in a Django model to customize the string representation of an object?',
                    'option1': '__repr__',
                    'option2': '__str__',
                    'option3': '__unicode__',
                    'option4': 'get_name',
                    'correct_answer': '__str__',
                    'marks': 2
                },
                {
                    'question': 'What does the Django ORM method select_related do?',
                    'option1': 'Filters objects based on related fields',
                    'option2': 'Optimizes queries by performing a SQL join and retrieving related object data in a single query',
                    'option3': 'Lazily loads related objects',
                    'option4': 'Selects related fields to delete',
                    'correct_answer': 'Optimizes queries by performing a SQL join and retrieving related object data in a single query',
                    'marks': 2
                },
                {
                    'question': 'How do you return a JSON response directly from a standard Django view?',
                    'option1': 'Return JsonResponse(data)',
                    'option2': 'Return HttpResponse(data, content_type="application/json")',
                    'option3': 'Return both JsonResponse(data) or HttpResponse with JSON content type',
                    'option4': 'Return template rendering JSON',
                    'correct_answer': 'Return both JsonResponse(data) or HttpResponse with JSON content type',
                    'marks': 2
                },
                {
                    'question': 'What is django-admin?',
                    'option1': 'The user interface for the admin panel',
                    'option2': 'A command-line tool for administrative tasks',
                    'option3': 'A package to manage Django security',
                    'option4': 'A web server for deployment',
                    'correct_answer': 'A command-line tool for administrative tasks',
                    'marks': 2
                },
                {
                    'question': 'Which dictionary key in request.POST or request.GET returns a list of values for a field name instead of a single value?',
                    'option1': 'get()',
                    'option2': 'get_list()',
                    'option3': 'getlist()',
                    'option4': 'fetch()',
                    'correct_answer': 'getlist()',
                    'marks': 2
                }
            ]
        }
    ]

    for q_data in quizzes_data:
        quiz = Quiz.objects.create(
            title=q_data['title'],
            description=q_data['description'],
            category=q_data['category'],
            level=q_data['level'],
            time_limit=q_data['time_limit']
        )
        print(f"Created Quiz: {quiz.title}")
        for quest in q_data['questions']:
            Question.objects.create(
                quiz=quiz,
                question=quest['question'],
                option1=quest['option1'],
                option2=quest['option2'],
                option3=quest['option3'],
                option4=quest['option4'],
                correct_answer=quest['correct_answer'],
                marks=quest['marks']
            )
            print(f"  Added Question: {quest['question'][:40]}...")

    # Create a default superuser admin if none exists so user can log in to admin out of the box!
    if not User.objects.filter(is_superuser=True).exists():
        User.objects.create_superuser('admin', 'admin@quizapp.com', 'admin123')
        print("Created Superuser: admin / admin123")

    print("Database seeding completed successfully!")

if __name__ == '__main__':
    seed()
