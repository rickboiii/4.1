[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=14438743&assignment_repo_type=AssignmentRepo)
# GitHub Lab 4: Unit Testing

## Student Information

* Ricky Suarez
* Spring/2024
* 37902

## Description

It is said, that the code that is read the most often is the test case code. That is because this code tells the programmer how the code should work in order to be successful. To do this, you as a programmer must know what is considered a right and wrong answer as part of a test.

## Instructions

In this lab, you will be given a working program that requires a test script to be written for a basic calculator that does addition, subtraction, multiplication, and division. The code allows for you to accept values and do math actions. 

1. Update the file `test_main.py` to increase the number of pytest unit tests in order to ensure the class is valid.
2. Modify the `TESTS.md` file with the manual testing inputs with expected outputs *if* you were to use the class for basic input/output testing.
3. Answer the questions below on the `README.md` file.

### Tips

* Consider how you will enter values into attributes will they be directly entered or use a method.
* Consider how groups of methods work together.
* Notice how in this version, the instructor has choosen to not use Input/Output testing, just unit tests.

---

## Lab Questions

Do not provide code for any of the questions. You need to provide answers to each of the questions in normal written language answering each of the questions.

### Question 1

**How do automated unit tests affect a programmers ability to conduct testing and should a programmer only use these test? Why or why not?**

Automated tests are fast and efficient but they provide only a limited range of inputs and may provide a false sense of security.

### Question 2

**In the example test case, describe how to ensure a program is well tested?**

You can ensure a program is well tested by having test cases that cover many parts of thr program

### Question 3

**A series of test functions were left in a subbed state. How did you choose to utilize or not utilize these?**

I did not utilize them.

### Question 4

**What additional tests did you decide on adding? Provide information on why you choose these additional tests.**

I decided on adding tests for dividing by zero. I chose to add this as it is an essential part of a trustworthy calculator.

---

## Assistance at Rio Hondo

Need help? Contact the [Math, Science, & Engineering Center](https://www.riohondo.edu/mathematics-and-sciences/math-science-center/) for tutoring assistance. Any form of sharing or uploading of this assignment on external websites is strictly prohibited.

## Rubric / Grading Criteria

See [Canvas](https://riohondo.instructure.com) for specific points breakdown in the assignment rubric.

Grading is done via a combination of automatic grading in GitHub and manual testing by the instructor. Points may be deducted based on the following criteria:

* Must contain working Python code
  * Code follows all instructions listed above
  * Code is well structured, formatted, and commented
  * Code is able to be manually run without errors
  * Code uses concepts as covered in the current topic for the lab
  * Provided unit tests pass test with partial credit available for 1 or more passed tests
* More than 1 commit made by the student per GitHub Repo
* Tools such as the Measure of Software Similarity (MOSS) may be used to detect plagiarism

Points may still be deducted based on the grading criteria above even if the assignment passes the Auto Grading unit tests. **Creating code that is well structured, formatted, and commented cannot be tested automatically. So you can pass all your auto grading tests, but still lose points.**

## Testing & Auto Grading

Always try running your code in your local environment before submitting for grading and use the provided criteria for testing. Troubleshooting and debugging code is a process that you must learn to be an effective programmer as you will not be given test cases in real world programming, you will have to write them yourself. Find more information on testing on the code read the [TESTS.md](TESTS.md) file.

Auto Grading may use a combination of automated Input/Output testing, Unit Tests using pytest, or both via GitHub Classroom depending on the assignment. Scores in GitHub are not communicated to your Canvas lab assignment. The instructor must still manually grade each one then enter a grade.
