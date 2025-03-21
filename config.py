import os

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

SKILL_SET = [
    # Web Development
    "HTML", "CSS", "JavaScript", "React", "PHP", "Node.js", "Express.js", "RESTful APIs",

    # Databases
    "MySQL", "PostgreSQL", "MongoDB",

    # DevOps & Software Tools
    "Git", "GitHub", "Docker", "Spring Boot", "Kubernetes", "AWS", "CI/CD Pipelines",

    # Programming & Software Development
    "Python", "Java", "C++", "C", "JavaScript", "TypeScript",

    # AI, Machine Learning & Data Science
    "Machine Learning", "Deep Learning", "AI", "OpenCV", "Computer Vision",
    "TensorFlow", "PyTorch", "Data Analysis", "NumPy", "Pandas", "Scikit-learn",

    # Cybersecurity
    "Ethical Hacking", "Penetration Testing", "Network Security",

    # Electrical & Electronics Engineering
    "Embedded Systems", "Arduino", "Raspberry Pi", "ESP32", "ARM Cortex",
    "Microcontrollers", "VHDL", "Verilog", "FPGA", "Circuit Design", "Proteus", "LTspice",

    # IoT & Automation
    "IoT", "PLC Programming", "SCADA Systems", "Modbus", "Industrial Robotics",

    # Mechanical & Civil Engineering
    "AutoCAD", "SolidWorks", "CATIA", "ANSYS", "MATLAB", "Finite Element Analysis (FEA)",
    "CFD Analysis", "SAP2000", "STAAD.Pro",

    # Aerospace & Automotive Engineering
    "CFD", "OpenFOAM", "XFOIL", "Battery Management Systems", "MATLAB for EV Simulation",
    "KUKA Robotics", "ABB Robotics",

    # Industrial & Manufacturing Engineering
    "Lean Manufacturing", "Six Sigma", "SAP ERP", "Supply Chain Management"
]

