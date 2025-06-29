import requests
import csv
import time

# Local FastAPI backend URL
BACKEND_URL = "http://127.0.0.1:8000/chat"

# 100 sample questions (mix of coding and math)
sample_questions = [
    "What is a for loop in Python?",
    "How do you solve a quadratic equation?",
    "Explain recursion with an example in Java.",
    "What's the difference between a list and a tuple in Python?",
    "How do you integrate x^2?",
    "What is Big-O notation?",
    "Write a function to reverse a string in JavaScript.",
    "What does the term 'inheritance' mean in OOP?",
    "How do you find the derivative of sin(x)?",
    "What is a dictionary in Python?",
    "How do you implement a binary search algorithm?",
    "What is the purpose of a constructor in a class?",
    "Explain the concept of polymorphism in programming.",
    "How do you handle exceptions in Java?",
    "What is the difference between synchronous and asynchronous programming?",
    "How do you create a RESTful API in Flask?",
    "What is the time complexity of quicksort?",
    "How do you connect to a database in Node.js?",
    "What is a lambda function in Python?",
    "How do you perform linear regression in R?",
    "What is the purpose of a stack in data structures?",
    "How do you implement a queue using two stacks?",
    "What is the difference between HTTP and HTTPS?",
    "How do you use regular expressions in JavaScript?",
    "What is the purpose of a hash table?",
    "How do you implement a linked list in C++?",
    "What is the difference between a class and an object?",
    "How do you perform a depth-first search in a graph?",
    "What is the purpose of a mutex in multithreading?",
    "How do you serialize an object in Python?",
    "What is the difference between a primary key and a foreign key in SQL?",
    "How do you implement a bubble sort algorithm?",
    "What is the purpose of a closure in JavaScript?",
    "How do you calculate the Fibonacci sequence using recursion?",
    "What is the difference between a GET and POST request in HTTP?",
    "How do you implement a hash function?",
    "What is the purpose of a virtual machine?",
    "How do you perform a merge sort algorithm?",
    "What is the difference between a static and dynamic array?",
    "How do you implement a binary tree?",
    "What is the purpose of a semaphore in concurrent programming?",
    "How do you use the map function in Python?",
    "How do you calculate the area of a triangle?",
    "What is the purpose of a design pattern in software development?",
    "How do you implement a stack using an array?",

    # Math questions
    "What is the derivative of x^3 + 2x^2 - 5x + 1?",
    "Solve for x: 2x + 5 = 13",
    "Find the integral of 3x^2 + 4x - 7",
    "What is the slope of the line passing through points (2, 3) and (5, 9)?",
    "Calculate the area of a circle with radius 7 cm",
    "Find the roots of the quadratic equation x^2 - 5x + 6 = 0",
    "What is sin(30°) in exact form?",
    "Simplify the expression: 3(2x - 4) + 5x",
    "Find the limit of (x^2 - 1)/(x - 1) as x approaches 1",
    "What is the volume of a sphere with radius 4 units?",
    "Solve the system of equations: 2x + y = 7, x - y = 2",
    "Find the second derivative of f(x) = x^4 - 3x^3 + 2x",
    "What is the distance between points (-1, 2) and (3, -4)?",
    "Calculate 15% of 240",
    "Find the perimeter of a rectangle with length 8 cm and width 5 cm",
    "What is cos(45°) in exact form?",
    "Solve for y: 3y - 7 = 2y + 8",
    "Find the area of a triangle with base 12 cm and height 8 cm",
    "What is the sum of the first 10 natural numbers?",
    "Simplify: (x^2 + 3x - 4)/(x - 1)",
    "Find the median of the dataset: 5, 3, 8, 2, 9, 1, 7",
    "What is the factorial of 6?",
    "Calculate the compound interest on $1000 for 2 years at 5% annual rate",
    "Find the equation of a line with slope 2 passing through point (1, 3)",
    "What is tan(60°) in exact form?",
    "Solve: |2x - 3| = 7",
    "Find the area under the curve y = x^2 from x = 0 to x = 3",
    "What is the standard deviation of the numbers 2, 4, 6, 8, 10?",
    "Convert 0.75 to a fraction in lowest terms",
    "Find the inverse of the function f(x) = 2x + 3",
    "What is the sum of angles in a pentagon?",
    "Solve the inequality: 3x - 5 < 2x + 7",
    "Find the discriminant of x^2 + 4x + 4 = 0",
    "What is the probability of rolling a sum of 7 with two dice?",
    "Calculate the surface area of a cube with side length 6 cm",
    "Find the geometric mean of 4 and 16",
    "What is the derivative of ln(x)?",
    "Solve: 2^x = 32",
    "Find the range of the function f(x) = x^2 - 4x + 3",
    "What is the greatest common divisor of 48 and 72?",
    "Calculate the diagonal of a square with side length 10 cm",
    "Find the critical points of f(x) = x^3 - 6x^2 + 9x",
    "What is the sum of an arithmetic series with first term 3, last term 27, and 9 terms?",
    "Solve the exponential equation: 3^(x+1) = 27",
    "Find the vertex of the parabola y = x^2 - 4x + 7",
    "What is the area of a sector with central angle 60° in a circle of radius 10?",
    "Calculate log base 2 of 64",
    "Find the asymptotes of the function f(x) = (2x + 1)/(x - 3)",
    "What is the coefficient of x^3 in the expansion of (x + 2)^5?",
    "Solve the trigonometric equation: sin(x) = 0.5 for 0 ≤ x ≤ 2π",

    # You can add more manually or loop/generate them...
]

# Auto-expand the list to 100 by duplicating with slight variation
while len(sample_questions) < 100:
    base = sample_questions[len(sample_questions) % 10]
    sample_questions.append(base + " Can you give an example?")

# Save results to CSV
with open("ai_test_data.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["question", "response"])

    for i, question in enumerate(sample_questions):
        print(f"Sending question {i+1}/100: {question}")
        try:
            response = requests.post(
                BACKEND_URL,
                json={"user_input": question},
                timeout=10
            )
            data = response.json()
            ai_response = data.get("response", "No response received.")
        except Exception as e:
            ai_response = f"Error: {e}"

        writer.writerow([question, ai_response])
        time.sleep(1.5)  # Prevent throttling

print("✅ Done! Responses saved to ai_test_data.csv")
