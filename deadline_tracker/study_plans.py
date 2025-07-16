"""
Study Plans for Graduate School Test Preparation
Contains structured study plans for TOEFL and GRE
"""

STUDY_PLANS = {
    "TOEFL": {
        "title": "TOEFL iBT Study Plan",
        "target_score": 100,
        "duration_weeks": 8,
        "study_hours_per_day": 2,
        "description": "Comprehensive 8-week TOEFL preparation plan targeting 100+ score",
        "phases": [
            {
                "phase": "Week 1-2: Foundation & Assessment",
                "duration": "2 weeks",
                "focus": "Baseline assessment and fundamentals",
                "tasks": [
                    {
                        "task": "Take diagnostic test",
                        "time_required": "3 hours",
                        "description": "Complete full-length practice test to identify strengths/weaknesses"
                    },
                    {
                        "task": "Grammar review",
                        "time_required": "1 hour/day",
                        "description": "Review essential grammar rules and structures"
                    },
                    {
                        "task": "Vocabulary building",
                        "time_required": "30 min/day",
                        "description": "Learn 20-30 new academic words daily"
                    },
                    {
                        "task": "Reading comprehension basics",
                        "time_required": "30 min/day",
                        "description": "Practice reading academic passages and answering questions"
                    }
                ]
            },
            {
                "phase": "Week 3-4: Skill Development",
                "duration": "2 weeks",
                "focus": "Develop individual section skills",
                "tasks": [
                    {
                        "task": "Reading section practice",
                        "time_required": "45 min/day",
                        "description": "Practice reading passages and question types"
                    },
                    {
                        "task": "Listening section practice",
                        "time_required": "45 min/day",
                        "description": "Practice lectures and conversations"
                    },
                    {
                        "task": "Speaking practice",
                        "time_required": "30 min/day",
                        "description": "Practice independent and integrated speaking tasks"
                    },
                    {
                        "task": "Writing practice",
                        "time_required": "30 min/day",
                        "description": "Practice integrated and independent writing tasks"
                    }
                ]
            },
            {
                "phase": "Week 5-6: Integration & Strategy",
                "duration": "2 weeks",
                "focus": "Integrate skills and develop test strategies",
                "tasks": [
                    {
                        "task": "Integrated tasks practice",
                        "time_required": "1 hour/day",
                        "description": "Practice tasks that combine multiple skills"
                    },
                    {
                        "task": "Time management practice",
                        "time_required": "30 min/day",
                        "description": "Practice pacing and time allocation strategies"
                    },
                    {
                        "task": "Note-taking skills",
                        "time_required": "30 min/day",
                        "description": "Develop effective note-taking for listening and reading"
                    },
                    {
                        "task": "Mid-term practice test",
                        "time_required": "3 hours",
                        "description": "Full-length practice test to assess progress"
                    }
                ]
            },
            {
                "phase": "Week 7-8: Final Preparation",
                "duration": "2 weeks",
                "focus": "Final review and test readiness",
                "tasks": [
                    {
                        "task": "Weak areas focus",
                        "time_required": "1 hour/day",
                        "description": "Intensive practice on identified weak areas"
                    },
                    {
                        "task": "Full practice tests",
                        "time_required": "3 hours, 2x/week",
                        "description": "Complete 4 full-length practice tests"
                    },
                    {
                        "task": "Review and analysis",
                        "time_required": "30 min/day",
                        "description": "Analyze mistakes and refine strategies"
                    },
                    {
                        "task": "Test day preparation",
                        "time_required": "1 hour",
                        "description": "Review test day procedures and relaxation techniques"
                    }
                ]
            }
        ],
        "resources": [
            "ETS Official TOEFL iBT Tests",
            "TOEFL iBT Official Guide",
            "Magoosh TOEFL Prep",
            "Barron's TOEFL iBT",
            "Academic word lists"
        ],
        "milestones": [
            {"week": 2, "milestone": "Complete diagnostic test and identify weak areas"},
            {"week": 4, "milestone": "Achieve 70+ in individual section practices"},
            {"week": 6, "milestone": "Score 85+ on mid-term practice test"},
            {"week": 8, "milestone": "Consistently score 100+ on practice tests"}
        ]
    },
    
    "GRE": {
        "title": "GRE General Test Study Plan",
        "target_score": 320,
        "duration_weeks": 12,
        "study_hours_per_day": 3,
        "description": "Comprehensive 12-week GRE preparation plan targeting 320+ score",
        "phases": [
            {
                "phase": "Week 1-3: Foundation Building",
                "duration": "3 weeks",
                "focus": "Establish fundamentals and assess baseline",
                "tasks": [
                    {
                        "task": "Diagnostic test",
                        "time_required": "3.5 hours",
                        "description": "Complete full-length GRE practice test"
                    },
                    {
                        "task": "Vocabulary building",
                        "time_required": "45 min/day",
                        "description": "Learn 25-30 GRE words daily using spaced repetition"
                    },
                    {
                        "task": "Math fundamentals review",
                        "time_required": "1 hour/day",
                        "description": "Review arithmetic, algebra, geometry, and data analysis"
                    },
                    {
                        "task": "Reading comprehension basics",
                        "time_required": "45 min/day",
                        "description": "Practice reading strategies and question types"
                    },
                    {
                        "task": "Analytical writing introduction",
                        "time_required": "30 min/day",
                        "description": "Learn essay structure and practice basic writing"
                    }
                ]
            },
            {
                "phase": "Week 4-6: Skill Development",
                "duration": "3 weeks",
                "focus": "Develop section-specific skills",
                "tasks": [
                    {
                        "task": "Verbal reasoning practice",
                        "time_required": "1 hour/day",
                        "description": "Practice text completion, sentence equivalence, and reading comprehension"
                    },
                    {
                        "task": "Quantitative reasoning practice",
                        "time_required": "1 hour/day",
                        "description": "Practice problem solving and quantitative comparison"
                    },
                    {
                        "task": "Analytical writing practice",
                        "time_required": "45 min/day",
                        "description": "Practice both issue and argument essays"
                    },
                    {
                        "task": "Vocabulary reinforcement",
                        "time_required": "30 min/day",
                        "description": "Continue vocabulary building and review"
                    }
                ]
            },
            {
                "phase": "Week 7-9: Strategy & Integration",
                "duration": "3 weeks",
                "focus": "Develop test strategies and integrate skills",
                "tasks": [
                    {
                        "task": "Advanced verbal strategies",
                        "time_required": "1 hour/day",
                        "description": "Learn advanced techniques for difficult verbal questions"
                    },
                    {
                        "task": "Advanced quantitative strategies",
                        "time_required": "1 hour/day",
                        "description": "Learn shortcuts and advanced problem-solving techniques"
                    },
                    {
                        "task": "Timed practice sessions",
                        "time_required": "1 hour/day",
                        "description": "Practice under time pressure with mixed question types"
                    },
                    {
                        "task": "Mid-term practice test",
                        "time_required": "3.5 hours",
                        "description": "Full-length practice test to assess progress"
                    }
                ]
            },
            {
                "phase": "Week 10-12: Final Preparation",
                "duration": "3 weeks",
                "focus": "Final review and test readiness",
                "tasks": [
                    {
                        "task": "Weak areas intensive review",
                        "time_required": "1.5 hours/day",
                        "description": "Focus on areas identified as weakest"
                    },
                    {
                        "task": "Full practice tests",
                        "time_required": "3.5 hours, 2x/week",
                        "description": "Complete 6 full-length practice tests"
                    },
                    {
                        "task": "Test analysis and review",
                        "time_required": "1 hour/day",
                        "description": "Analyze performance and refine strategies"
                    },
                    {
                        "task": "Final vocabulary review",
                        "time_required": "30 min/day",
                        "description": "Review all learned vocabulary and common roots"
                    }
                ]
            }
        ],
        "resources": [
            "ETS Official GRE Super Power Pack",
            "Manhattan Prep GRE Strategy Guides",
            "Magoosh GRE Prep",
            "Barron's GRE",
            "PowerScore GRE Verbal Reasoning Bible",
            "Kaplan GRE Math Workbook"
        ],
        "milestones": [
            {"week": 3, "milestone": "Complete diagnostic and establish baseline score"},
            {"week": 6, "milestone": "Achieve 150+ Verbal, 155+ Quantitative on practice tests"},
            {"week": 9, "milestone": "Score 155+ Verbal, 160+ Quantitative on mid-term test"},
            {"week": 12, "milestone": "Consistently score 320+ on practice tests"}
        ]
    }
}

def get_study_plan(test_type):
    """Get study plan for specific test type"""
    return STUDY_PLANS.get(test_type.upper(), None)

def get_all_test_types():
    """Get all available test types"""
    return list(STUDY_PLANS.keys())

def get_phase_tasks(test_type, phase_number):
    """Get tasks for a specific phase of a test"""
    plan = get_study_plan(test_type)
    if plan and 0 <= phase_number < len(plan['phases']):
        return plan['phases'][phase_number]['tasks']
    return []