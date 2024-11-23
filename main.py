import tkinter as tk
from tkinter import ttk, messagebox

class CourseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Course Tracker")
        self.setup_name_input()
    
    def setup_name_input(self):
        # Frame for name input
        self.name_frame = ttk.Frame(self.root, padding=10)
        self.name_frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(self.name_frame, text="Enter your name:").pack(pady=5)
        self.name_entry = ttk.Entry(self.name_frame)
        self.name_entry.pack(pady=5)
        
        ttk.Button(
            self.name_frame,
            text="Next",
            command=self.show_course_input
        ).pack(pady=10)
    
    def show_course_input(self):
        self.username = self.name_entry.get().strip()
        if not self.username:
            messagebox.showwarning("Input Error", "Please enter your name.")
            return
        
        # Hide name input frame and show course input frame
        self.name_frame.pack_forget()
        
        self.course_frame = ttk.Frame(self.root, padding=10)
        self.course_frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(self.course_frame, text=f"Hello {self.username}!\nEnter your courses below:").pack(pady=5)
        
        self.course_list = []
        
        # Input fields
        ttk.Label(self.course_frame, text="Course Name:").pack(pady=5)
        self.course_name_entry = ttk.Entry(self.course_frame)
        self.course_name_entry.pack(pady=5)
        
        ttk.Label(self.course_frame, text="Unit You Are On:").pack(pady=5)
        self.unit_on_entry = ttk.Entry(self.course_frame)
        self.unit_on_entry.pack(pady=5)
        
        ttk.Label(self.course_frame, text="Unit You Should Be On:").pack(pady=5)
        self.unit_should_entry = ttk.Entry(self.course_frame)
        self.unit_should_entry.pack(pady=5)
        
        ttk.Label(self.course_frame, text="Next Assignment Weight (%):").pack(pady=5)
        self.assignment_weight_entry = ttk.Entry(self.course_frame)
        self.assignment_weight_entry.pack(pady=5)
        
        # Buttons
        ttk.Button(self.course_frame, text="Add Course", command=self.add_course).pack(pady=10)
        ttk.Button(self.course_frame, text="Finish", command=self.show_summary).pack(pady=10)
    
    def add_course(self):
        course_name = self.course_name_entry.get().strip()
        unit_on = self.unit_on_entry.get().strip()
        unit_should = self.unit_should_entry.get().strip()
        assignment_weight = self.assignment_weight_entry.get().strip()
        
        if not course_name or not unit_on.isdigit() or not unit_should.isdigit() or not assignment_weight.isdigit():
            messagebox.showwarning("Input Error", "Please fill out all fields correctly.")
            return
        
        self.course_list.append({
            "name": course_name,
            "unit_on": int(unit_on),
            "unit_should": int(unit_should),
            "assignment_weight": int(assignment_weight),
        })
        
        # Clear input fields
        self.course_name_entry.delete(0, tk.END)
        self.unit_on_entry.delete(0, tk.END)
        self.unit_should_entry.delete(0, tk.END)
        self.assignment_weight_entry.delete(0, tk.END)
        messagebox.showinfo("Course Added", f"{course_name} has been added!")
    
    def show_summary(self):
        if not self.course_list:
            messagebox.showwarning("No Courses", "You haven't added any courses.")
            return
        
        # Hide course input frame
        self.course_frame.pack_forget()
        
        summary_frame = ttk.Frame(self.root, padding=10)
        summary_frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(summary_frame, text=f"Summary for {self.username}").pack(pady=5)
        
        for course in self.course_list:
            priority = (course['unit_should'] - course['unit_on']) * course['assignment_weight']
            summary = (
                f"Course: {course['name']} | Unit On: {course['unit_on']} | "
                f"Unit Should Be: {course['unit_should']} | Next Assignment Weight: {course['assignment_weight']}% | "
                f"Priority: {priority}"
            )
            ttk.Label(summary_frame, text=summary).pack(pady=2)
        
        ttk.Button(summary_frame, text="Finish", command=self.root.quit).pack(pady=10)

# Create the application window
root = tk.Tk()
app = CourseTrackerApp(root)
root.mainloop()
