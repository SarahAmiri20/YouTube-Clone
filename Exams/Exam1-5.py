def generate_quiz():
    quiz = {
       
    1: {"question": "What part of the Box Model is responsible for adjusting the size of an element to prevent text overflow?",
        "options": ["A. margin", "B. padding", "C. width"],
        "answer": "B"},
    2: {"question": "What is the role of the CSS property in a style rule?",
        "options": ["A. It specifies the value of the style.", "B. It tells the computer what element to target on the page.", "C. It defines the structure of the page."],
        "answer": "A"},
    3: {"question": "Which HTML tag is used to include CSS code within a web page?",
        "options": ["A. <script>", "B. <link>", "C. <style>"],
        "answer": "C"},
    4: {"question": "What is a CSS value in the context of style rules?",
        "options": ["A. It is the name of the CSS property being used.", "B. It specifies the element on which the styles should be applied.", "C. It defines what the CSS property should be set to."],
        "answer": "C"},
    5: {"question": "Which of the following is NOT true about the <style> element?",
        "options": ["A. It is used to write CSS code within an HTML document.", "B. It is placed within the <head> section of the HTML document.", "C. It creates new elements on the web page."],
        "answer": "C"},
    6: {"question": "In CSS syntax, what is the purpose of the curly brackets {}?",
        "options": ["A. To group multiple selectors together.", "B. To enclose the HTML content of a web page.", "C. To define a block of styles for a specific selector."],
        "answer": "C"},
    7: {"question": "Which CSS selector targets all button elements on the page?",
        "options": ["A. button{}", "B. #button{}", "C. .button{}"],
        "answer": "A"},
    8: {"question": "How do you comment in CSS?",
        "options": ["A. // This is a comment", "B. <!-- This is a comment -->", "C. /* This is a comment */"],
        "answer": "C"},
    9: {"question": "What does HTML stand for?",
        "options": ["A. Hyper Text Markup Language", "B. Hyperlink and Text Markup Language", "C. Home Tool Markup Language"],
        "answer": "A"},
    10: {"question": "What is the primary purpose of using CSS?",
         "options": ["A. To create new elements on the page.", "B. To define the structure of a web page.", "C. To change the appearance of elements on the page."],
         "answer": "C"},
    11: {"question": "How does the computer differentiate between an opening tag and a closing tag in HTML?",
         "options": ["A. The closing tag has a slash (/) behind its name.", "B. The opening tag is always in lowercase, and the closing tag is in uppercase.", "C. The closing tag is always in lowercase, and the opening tag is in uppercase."],
         "answer": "A"},
    12: {"question": "What does a CSS selector do?",
         "options": ["A. It defines the structure of a web page.", "B. It tells the browser which HTML elements to apply the styles to.", "C. It creates new elements on the page."],
         "answer": "B"},
    13: {"question": "What is the function of an attribute in HTML?",
         "options": ["A. It defines the structure of a webpage.", "B. It modifies how an element behaves.", "C. It creates new elements on the page."],
         "answer": "B"},
    14: {"question": "What is the purpose of an HTML tag?",
         "options": ["A. It modifies how an element behaves.", "B. It creates a link to another website.", "C. It tells the computer what we are trying to create."],
         "answer": "C"},
    15: {"question": "What is the purpose of the \":hover\" pseudo-class in CSS?",
         "options": ["A. It defines styles that are applied when clicking on a button.", "B. It adds extra styles when hovering over an element.", "C. It sets the opacity of an element."],
         "answer": "B"},
    16: {"question": "What does an anchor element (<a>) represent in HTML?",
         "options": ["A. A paragraph of text.", "B. An image on the webpage.", "C. A link to another website."],
         "answer": "C"},
    17: {"question": "What is the correct syntax for adding an attribute to an HTML element?",
         "options": ["A. attribute name=\"attribute value\"", "B. attribute name: attribute value", "C. attribute name = attribute value"],
         "answer": "A"},
    18: {"question": "What is the purpose of the CSS rule provided below?\n\n```css\nbutton {\n  background-color: blue;\n  color: white;\n}\n```",
         "options": ["A. It sets the text color of all buttons to white.", "B. It sets the background color of all buttons to blue.", "C. It removes the background color from all buttons."],
         "answer": "B"},
    19: {"question": "Which HTML tag is used to create a button element?",
         "options": ["A. <button>text</button>", "B. <input type=\"button\" value=\"text\">", "C. <btn>text</btn>"],
         "answer": "A"},
    20: {"question": "What does the \"font-size: ..px\" property do in CSS?",
         "options": ["A. It changes the font family of the text.", "B. It controls the space between lines in a text.", "C. It changes the size of the text."],
         "answer": "C"},
    21: {"question": "What is the purpose of the \"target\" attribute in an anchor element (<a>)?",
         "options": ["A. It sets the destination of the link.", "B. It modifies the appearance of the link.", "C. It specifies whether the link should open in a new tab or not."],
         "answer": "C"},
    22: {"question": "What is the role of HTML syntax rules?",
         "options": ["A. They define the structure of a webpage.", "B. They tell the computer how to read and understand HTML code.", "C. They modify the appearance of elements on the page."],
         "answer": "B"},
    23: {"question": "Which property is used to align an element, such as a button, to the top of its container?",
         "options": ["A. vertical-align", "B. text-align", "C. margin"],
         "answer": "A"},
    24: {"question": "What does the \"line-height: ..px\" property control in CSS?",
         "options": ["A. The space between the lines in a text.", "B. The size of the text.", "C. The font family of the text."],
         "answer": "A"},
    25: {"question": "What CSS property is used to add space outside of an element?",
         "options": ["A. padding", "B. vertical-align", "C. margin"],
         "answer": "C"},
    26: {"question": "How do you add space on the left side of an element to separate it from the adjacent element?",
         "options": ["A. margin-top", "B. padding-left", "C. margin-left"],
         "answer": "C"},
    27: {"question": "What is the value range for the \"opacity\" property in CSS?",
         "options": ["A. Between 0 and 1", "B. Between 1 and 100", "C. Between -1 and 1"],
         "answer": "A"},
    28: {"question": "What happens when there are extra spaces in HTML code?",
         "options": ["A. The code will not work properly.", "B. Extra spaces are ignored by the computer.", "C. The computer will display an error message."],
         "answer": "B"},
    29: {"question": "What does the \"box-shadow\" property in CSS take as input?",
         "options": ["A. A single value to set the color of the shadow.", "B. Two values to set the horizontal and vertical positions of the shadow.", "C. Four values to set the horizontal and vertical positions, blur, and color of the shadow."],
         "answer": "C"},
    30: {"question": "What does the \"transition\" property in CSS do?",
         "options": ["A. It adds a shadow underneath the element.", "B. It changes the opacity of an element smoothly.", "C. It changes the background color of an element when hovering over it."],
         "answer": "B"},
    31: {"question": "How do you define a CSS class for a button with the name \"subscribe-button\"?",
         "options": ["A. .button subscribe-button { }", "B. #subscribe-button { }", "C. .subscribe-button { }"],
         "answer": "C"},
    32: {"question": "What is the purpose of the \":active\" pseudo-class in CSS?",
         "options": ["A. It defines styles that are applied when clicking on a button.", "B. It adds extra styles when hovering over an element.", "C. It changes the opacity of an element smoothly."],
         "answer": "A"},
    33: {"question": "What happens when the \"opacity\" value is set to 0 in CSS?",
         "options": ["A. The element will fade out and disappear.", "B. The element will still look normal when hovered over.", "C. The element will become fully opaque and solid."],
         "answer": "A"},
    34: {"question": "What is the value of the \"transition\" property in the provided example CSS?",
         "options": ["A. 0.5s", "B. 1s", "C. 2s"],
         "answer": "A"},
    35: {"question": "Which CSS property is used to make an element look lighter when hovering over it?",
         "options": ["A. box-shadow", "B. opacity", "C. transition"],
         "answer": "B"},
    36: {"question": "Which CSS property is used to change the font of a text?",
         "options": ["A. font-style: italic", "B. font-size: ..px", "C. font-family"],
         "answer": "C"},
    37: {"question": "What does the CSS Box Model allow you to do?",
         "options": ["A. Add space between HTML elements on a webpage.", "B. Change the font and font size of HTML elements.", "C. Add space inside and outside HTML elements."],
         "answer": "C"},
    38: {"question": "What is the purpose of using HTML entities?",
         "options": ["A. They create special characters like checkmark and middle dot.", "B. They define the structure of an HTML page.", "C. They target all elements on the page."],
         "answer": "A"},
    39: {"question": "What is the purpose of the \"rgba\" color format in CSS?",
         "options": ["A. It sets the color of the element's shadow.", "B. It defines a color with an additional opacity value.", "C. It creates a gradient effect for the background of an element."],
         "answer": "B"},
    40: {"question": "What does the Computed tab in Chrome DevTools help you do when copying a design from a webpage?",
         "options": ["A. Copy the HTML elements used in the design.", "B. Copy the background color of the design.", "C. Copy the CSS styles applied to an element, including margins and padding."],
         "answer": "C"},
    41: {"question": "How do you align text in the center using CSS?",
         "options": ["A. text-align: center", "B. text-decoration: underline", "C. font-weight: bold"],
         "answer": "A"},
    42: {"question": "Which CSS property is used to force part of the text to the next line if it overflows its container?",
         "options": ["A. font-weight: bold", "B. width: ..px", "C. text-align: center"],
         "answer": "B"},
    43: {"question": "What does the \"text-decoration: underline\" property do in CSS?",
         "options": ["A. It changes the font style to italic.", "B. It aligns the text in the center.", "C. It makes the text underlined."],
         "answer": "C"},
    44: {"question": "How can we clean CSS code by targeting all elements on the page?",
         "options": ["A. Using \"text-align: center\" property.", "B. Setting default values for margin-top and margin-bottom.", "C. Adding a \"font-family\" property to all elements."],
         "answer": "B"},
    45: {"question": "What is the purpose of using hex values to represent colors in CSS?",
         "options": ["A. Hex values are easier to remember than RGB values.", "B. Hex values allow us to measure the opacity of the color.", "C. Hex values are another way to represent RGB colors."],
         "answer": "C"},
    46: {"question": "What is the purpose of the span element in HTML?",
         "options": ["A. It creates an underlined text.", "B. It adds new styles to the element.", "C. It doesn't add any new style to the element, but styles can be added using a class."],
         "answer": "C"},
    47: {"question": "Which type of element creates a bold text in HTML?",
         "options": ["A. u element", "B. strong element", "C. span element"],
         "answer": "B"},
    48: {"question": "How can you access Chrome DevTools on a webpage?",
         "options": ["A. By right-clicking on an HTML element and selecting \"Inspect.\"", "B. By clicking on the arrow at the top left corner of the webpage.", "C. By pressing the \"F12\" key on the keyboard."],
         "answer": "A"},
    49: {"question": "What are Chrome DevTools used for?",
         "options": ["A. To create and modify HTML elements on a webpage.", "B. To measure the background color of an element in hex format.", "C. To inspect HTML elements and view their CSS styles on a webpage."],
         "answer": "C"},
    50: {"question": "What does the Computed tab show in Chrome DevTools?",
         "options": ["A. The final styles applied to an element, including margins and padding.", "B. All the HTML elements used on the webpage.", "C. The hex values of the background colors used on the webpage."],
         "answer": "A"}
}

        # Add the rest of the questions and options here...
        # Make sure to adjust the question number and answer accordingly.
    
    return quiz
    
def take_quiz(quiz):
    score = 0
    total_questions = len(quiz)

    for question_number, question_data in quiz.items():
        print(f"\nQuestion {question_number}: {question_data['question']}")
        for option in question_data['options']:
            print(option)

        user_answer = input("Enter your option (A/B/C): ").strip().upper()
        if user_answer == question_data['answer']:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")

    return score

def calculate_grade(score, total_questions):
    grade = (score / total_questions) * 100
    return grade

def main():
    quiz = generate_quiz()
    score = take_quiz(quiz)
    total_questions = len(quiz)
    grade = calculate_grade(score, total_questions)

    print(f"\nYour Grade: {grade:.2f}/100")

if __name__ == "__main__":
    main()
