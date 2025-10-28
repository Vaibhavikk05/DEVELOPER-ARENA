def calculate_grade(marks):
    if marks >= 90:
        grade = "A+"
        message = "Outstanding! You're a star performer! Keep up the excellent work!"
    elif marks >= 80:
        grade = "A"
        message = "Excellent work! You've shown great dedication and understanding!"
    elif marks >= 70:
        grade = "B"
        message = "Great job! You're doing really well. Keep pushing forward!"
    elif marks >= 60:
        grade = "C"
        message = "Good effort! With a bit more practice, you'll reach even greater heights!"
    elif marks >= 50:
        grade = "D"
        message = "You're making progress! Don't give up - every expert was once a beginner!"
    else:
        grade = "F"
        message = "Don't be discouraged! This is just a stepping stone. Learn from it and come back stronger!"
    
    return grade, message

def main():
    print("=" * 50)
    print("     STUDENT GRADE CALCULATOR")
    print("=" * 50)
    
    try:
        marks = float(input("\nEnter your marks (0-100): "))
        
        if marks < 0 or marks > 100:
            print("\nError: Please enter marks between 0 and 100!")
            return
        
        grade, message = calculate_grade(marks)
        
        print("\n" + "=" * 50)
        print(f"Your Marks: {marks}")
        print(f"Your Grade: {grade}")
        print("=" * 50)
        print(f"\n{message}")
        print("\n" + "=" * 50)
        
    except ValueError:
        print("\nError: Please enter a valid number!")

if __name__ == "__main__":
    main()
