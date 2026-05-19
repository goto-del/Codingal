def evaluate_grade(score):
    """
    Evaluates a numerical score and returns the corresponding letter grade
    using conditional statements.
    """
    # First conditional statement to check for valid input bounds
    if score < 0 or score > 100:
        return f"Invalid score ({score})! Please provide a value between 0 and 100."
    
    # Using if-elif-else conditional statements to determine the grade
    if score >= 90:
        grade = 'A'
        feedback = "Excellent work!"
    elif score >= 80:
        grade = 'B'
        feedback = "Good job!"
    elif score >= 70:
        grade = 'C'
        feedback = "Average performance."
    elif score >= 60:
        grade = 'D'
        feedback = "Below average, needs improvement."
    else:
        grade = 'F'
        feedback = "Failing grade. Please seek extra help."
        
    return f"Score: {score} -> Grade: {grade} | {feedback}"

if __name__ == "__main__":
    print("--- Grade Evaluation Program ---")
    print("Demonstrating conditional statements (if, elif, else)\n")
    
    # A list of example test scores
    test_scores = [95, 82, 74, 65, 45, 105, -10]
    
    # Evaluate each score
    for score in test_scores:
        result = evaluate_grade(score)
        print(result)
