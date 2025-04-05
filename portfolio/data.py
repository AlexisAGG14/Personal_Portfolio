"""
Include data to add, using the models provided here.
We'll include data such as the work experience, the education and others.
"""
from portfolio.models import (
    WorkExperienceModel, ProjectModel,
    EducationalModel, EducationalType,
    OpenSourceModel, WorkVisaModel
)

# ========================================== #
#            WORK EXPERIENCE JOBS            #
# ========================================== #
WORK_EXPERIENCE: list[WorkExperienceModel] = [
    WorkExperienceModel(
        worked_date="May 2024 - Current",
        position_job="Data Analyst",
        company_and_city="Chubb, México",
        description_job="""
            As part of the Global Dashboard Team, I work with multiple regions including North America, LATAM, 
            APAC, and EMEA. My responsibilities include documenting KPIs and establishing technical definitions 
            aligned with business requirements, maintaining metric repositories for both technical and business 
            teams, analyzing data across processing stages to ensure accurate reporting and interpretation, and 
            providing technical support to non-technical users to ensure good project development and data accuracy.
        """,
        software_skills=(
            "Data Analysis", "KPI Management", "Technical Documentation", "Business Intelligence"
        ),
    ),
    WorkExperienceModel(
        worked_date="December 2021 - April 2024",
        position_job="Data Scientist",
        company_and_city="Valiot, México",
        description_job="""
            Led data analytics initiatives including cleaning, filtering, and analyzing data for product implementation 
            reporting. Designed and implemented optimization and machine learning projects for clients such as Samtec, 
            John Deere, and Heineken. Notable projects included time series modeling for gold usage optimization in 
            semiconductor production and production program optimization. Developed and delivered project progress 
            updates, presenting results and visualizations to stakeholders.
        """,
        software_skills=(
            "Python", "Machine Learning", "Data Science", "Time Series Analysis",
            "Optimization", "Data Visualization"
        ),
    ),
    WorkExperienceModel(
        worked_date="August 2020 - December 2021",
        position_job="Research Assistant",
        company_and_city="Universidad Autónoma de Nuevo León, México",
        description_job="""
            Focused on developing behavioral constraints for computational simulations and conducting 
            statistical analysis of behavior. This work involved implementing complex mathematical models 
            and analyzing their results to understand and predict system behaviors.
        """,
        software_skills=(
            "Statistical Analysis", "Computational Modeling", "Python",
            "Research Methods", "Data Analysis"
        ),
    )
]

# ========================================== #
#                 EDUCATION                  #
# ========================================== #
EDUCATION: list[EducationalModel] = [
    EducationalModel(
        education_type=EducationalType.UNIVERSITY,
        educational_entity="Universidad Autónoma de Nuevo León",
        study_subject="BSc Physics",
        range_years="2018-2021",
        description="""
            Specialization in Computational Physics, focusing on 
            Materials Science and Molecular Dynamics, developing 
            data analysis tools, fracture prediction in materials, 
            and optimization tools for the contours of different 
            atomic structures. During my bachelor's, I studied and learned
            not only how to apply mathematics to solve real problems,
            such as the entire physics world, but also to use it as a tool
            to model basically everything. Among this, I understand the
            benefits of using highly scalable tools (such as HPC) to model
            and simulate different kinds of problems or scenarios. I worked as a
            research assistant in the Materials Science department, using
            mathematical modeling to understand the materials' behavior in different
            situations.
        """
    )
]

# ========================================== #
#                 CERTIFICATES               #
# ========================================== #
CERTIFICATES: list[EducationalModel] = [
    EducationalModel(
        education_type=EducationalType.UNIVERSITY,
        educational_entity="Google",
        study_subject="Google Data Analytics Certificate",
        range_years="2024",
        url="https://www.credly.com/badges/24553d0c-3d4f-4bb5-b4cf-7584ba4bb966/public_url",
        description="""
            This professional certification validates completion of eight Google-developed courses 
            with interactive and practical assessments, designed to prepare for entry-level data 
            analytics positions. Demonstrates proficiency in various tools and platforms including 
            spreadsheets, SQL, Excel, and R. Acquired skills in data preparation, processing, 
            analysis, and sharing to drive thoughtful action.
        """
    ),
    EducationalModel(
        education_type=EducationalType.UNIVERSITY,
        educational_entity="IBM",
        study_subject="Python for Data Science, AI & Development",
        range_years="2021",
        url="https://coursera.org/share/24f5672f7ca0d815efb8965806110b0a",
        description="""
            This certification focuses on Python programming fundamentals for data science and 
            software development. The program covers essential concepts including variables, 
            data structures, branching, loops, functions, and object-oriented programming. 
            Demonstrates proficiency in key data science libraries (Pandas, NumPy) and tools 
            (Jupyter Notebooks), as well as data acquisition techniques through APIs and web 
            scraping using libraries like Beautiful Soup.
        """
    )
]

# ========================================== #
#                 PROJECTS                   #
# ========================================== #
PROJECTS: list[ProjectModel] = [
    ProjectModel(
        project_title="Global Dashboard Analytics",
        project_image="/projects/dashboard.jpeg",
        url_github=None,
        url_project=None,
        description="""
            As part of Chubb's Global Dashboard Team, I led comprehensive metric analysis across 
            multiple regions (North America, LATAM, APAC, and EMEA). The project focused on 
            establishing and maintaining accurate data management systems, ensuring consistent 
            reporting and efficient collaboration between regional teams.
        """,
        software_skills=(
            "Data Analysis", "Business Intelligence", "KPI Management",
            "Global Data Management", "Data Visualization"
        )
    ),
    ProjectModel(
        project_title="Semiconductor Production Optimization",
        project_image="/projects/factory.jpeg",
        url_github=None,
        url_project=None,
        description="""
            Led the deployment of Valiot FactoryOS at Samtec, implementing time series modeling 
            to optimize gold usage in semiconductor production. The project successfully reduced 
            material waste while maintaining quality standards through predictive analytics and 
            process optimization techniques.
        """,
        software_skills=(
            "Time Series Analysis", "Predictive Modeling", "Process Optimization",
            "Data Science", "Manufacturing Analytics"
        )
    ),
    ProjectModel(
        project_title="Production Program Optimization",
        project_image="/projects/valuechain.jpeg",
        url_github=None,
        url_project=None,
        description="""
            Implemented Valiot ValueChainOS for John Deere and Heineken, focusing on production 
            program optimization. Utilized data analysis to identify improvement opportunities in 
            production processes. Managed data storytelling to effectively communicate solutions 
            and algorithm features to stakeholders, leading to improved operational efficiency.
        """,
        software_skills=(
            "Data Analysis", "Process Optimization", "Data Storytelling",
            "Production Analytics", "Algorithm Development"
        )
    )
]

# ========================================== #
#              OPEN SOURCE CODE              #
# ========================================== #
OPEN_SOURCE: list[OpenSourceModel] = [
    OpenSourceModel(
        project_title="Open Source Projects",
        project_image="/projects/wip.png",
        url_github=None,
        url_project=None,
        description="""[Work in Progress] Open source contributions and projects
        are currently under development. Check back soon for updates on various
        tools and libraries focused on data science and software development.
        """,
        software_skills=(
            "Python", "Data Science", "Software Development"
        )
    )
]

# ========================================== #
#              WORK VISA MODELS              #
# ========================================== #
WORK_VISA: list[WorkVisaModel] = [
    # * Mexico Work Visas
    WorkVisaModel(
        visa_name="Citizenship",
        country="Mexico",
        description=(
            "As a citizen, I do not need any kind of visa to work in Mexico."
        ),
        eligibility_conditions=(
            "Requires to be a Mexican citizen."
        ),
        duration="N/A",
        application_fee=9999,
        processing_time="2-3 months",
        required_documents=[
            "Valid passport or ID",
        ],
        application_link=""
    ),
    # * USA Work Visas
    # WorkVisaModel(
    #     visa_name="H-1B Visa",
    #     country="United States",
    #     description="A visa for specialized professionals in fields" +
    #     " like IT, finance, and engineering.",
    #     eligibility_conditions="Requires a bachelor's degree or equivalent" +
    #     " and a job offer from a U.S. employer. Also, the employer must" +
    #     " sponsor the visa.",
    #     duration="3 years (extendable up to 6 years)",
    #     application_fee=460.00,
    #     processing_time="3-6 months",
    #     required_documents=[
    #         "Passport",
    #         "Degree certificates",
    #         "USA Job offer letter",
    #         "A sponsor employer",
    #         # "Proof of work experience"
    #     ],
    #     application_link="https://www.uscis.gov/h-1b"
    # ),
    WorkVisaModel(
        visa_name="TN Visa (Trade NAFTA)",
        country="United States",
        description=(
            "A non-immigrant visa for citizens of Mexico and Canada, "
            "allowing temporary employment in the United States in qualified professional roles." +
            " This, different from the H-1B visa, does not require a sponsor employer."
        ),
        eligibility_conditions=(
            "Applicants must be citizens of Mexico or Canada" +
            " and have a job offer in a NAFTA-listed "
            "occupation (e.g., accountants, engineers, scientists)." +
            " Proof of qualifications required."
        ),
        duration="3 years (renewable indefinitely under certain conditions)",
        application_fee=160.00,  # General consular processing fee
        processing_time="Varies by consulate or port of entry; typically 1-3 weeks",
        required_documents=[
            "Passport",
            "Degree certificates",
            "USA Job offer letter",
            "DS-160 application form"
        ],
        application_link="https://travel.state.gov/content/travel/en/us-visas/employment/tn.html"
    ),
    # * Canada Work Visas
    WorkVisaModel(
        visa_name="Working Holiday Visa (IEC)",
        country="Canada",
        description=(
            "A visa that allows Mexican citizens to travel and work temporarily in Canada "
            "without the need for a job offer or sponsor."
        ),
        eligibility_conditions=(
            "Applicants must be Mexican citizens aged 18-35, have a valid"
            " passport, and sufficient funds "
            "to support themselves upon arrival (minimum CAD 2,500)."
            " No job offer is required."
        ),
        duration="Up to 1 year",
        application_fee=156.00,  # Approximate fee in CAD
        processing_time="6-8 weeks",
        required_documents=[
            "Valid Mexican passport",
            "Proof of funds",
            "Police clearance certificate",
            "Application IRCC"
        ],
        application_link=(
            "https://www.canada.ca/en/immigration-refugees-citizenship/"
            "services/work-canada/iec.html"
        )
    )
]
