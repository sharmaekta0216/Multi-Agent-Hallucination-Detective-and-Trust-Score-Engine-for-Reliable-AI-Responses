# import json
# import sys
# import os

# # Add backend folder to Python path
# sys.path.append(os.path.abspath("../backend"))

# # Import your existing workflow
# from workflow import run_workflow


# # Load test questions
# with open("test_questions.json", "r", encoding="utf-8") as file:
#     questions = json.load(file)


# total_questions = len(questions)
# correct_answers = 0
# results = []


# print("\n==============================")
# print("STARTING EVALUATION")
# print("==============================\n")


# for item in questions:

#     question = item["question"]
#     correct_answer = item["correct_answer"]

#     print(f"\nQuestion {item['id']}: {question}")

#     try:
#         # Send question to your Multi-Agent System
#         result = run_workflow(question)

#         print("System Result:", result)

#         # Change this key according to your workflow response
#         final_answer = result.get("response", "")

#         # Simple answer comparison
#         if correct_answer.lower() in final_answer.lower():
#             status = "Correct"
#             correct_answers += 1
#         else:
#             status = "Incorrect"

#         results.append({
#             "id": item["id"],
#             "question": question,
#             "correct_answer": correct_answer,
#             "system_answer": final_answer,
#             "status": status
#         })

#     except Exception as error:

#         print("Error:", error)

#         results.append({
#             "id": item["id"],
#             "question": question,
#             "correct_answer": correct_answer,
#             "system_answer": "ERROR",
#             "status": "Error"
#         })


# # Calculate accuracy
# accuracy = (correct_answers / total_questions) * 100


# # Save results
# with open("evaluation_results.json", "w", encoding="utf-8") as file:
#     json.dump(results, file, indent=4, ensure_ascii=False)


# # Display final results
# print("\n==============================")
# print("EVALUATION COMPLETED")
# print("==============================")
# print(f"Total Questions: {total_questions}")
# print(f"Correct Answers: {correct_answers}")
# print(f"Accuracy: {accuracy:.2f}%")
# print("==============================")
# import json
# import sys
# import os

# # Add the backend folder to Python path
# sys.path.append(os.path.abspath("../backend"))

# # Import your existing workflow
# from agents.workflow import run_workflow


# # Test user ID
# USER_ID = 1


# # Load test questions
# with open("test_questions.json", "r", encoding="utf-8") as file:
#     questions = json.load(file)


# total_questions = len(questions)
# correct_answers = 0

# results = []


# print("\n====================================")
# print("MULTI-AGENT SYSTEM EVALUATION")
# print("====================================")


# for item in questions:

#     question_id = item["id"]
#     question = item["question"]
#     correct_answer = item["correct_answer"]

#     print(f"\nQuestion {question_id}: {question}")

#     try:

#         # Run your actual multi-agent workflow
#         result = run_workflow(
#             user_id=USER_ID,
#             query=question
#         )

#         # Get AI response
#         ai_response = result["ai_response"]

#         print("AI Response:", ai_response)

#         # Display scores
#         print("Fact Score:", result["fact_score"])
#         print("Logic Score:", result["logic_score"])
#         print("Evidence Score:", result["evidence_score"])
#         print("Hallucination Score:", result["hallucination_score"])
#         print("Trust Score:", result["trust_score"])

#         # Simple correctness check
#         if correct_answer.lower() in ai_response.lower():

#             status = "Correct"
#             correct_answers += 1

#         else:

#             status = "Incorrect"


#         # Save result
#         results.append({

#             "id": question_id,

#             "question": question,

#             "correct_answer": correct_answer,

#             "ai_response": ai_response,

#             "fact_score": result["fact_score"],

#             "logic_score": result["logic_score"],

#             "evidence_score": result["evidence_score"],

#             "hallucination_score": result["hallucination_score"],

#             "trust_score": result["trust_score"],

#             "trust_level": result["trust_level"],

#             "status": status

#         })


#     except Exception as error:

#         print("ERROR:", error)

#         results.append({

#             "id": question_id,

#             "question": question,

#             "correct_answer": correct_answer,

#             "status": "Error",

#             "error": str(error)

#         })


# # Calculate accuracy
# accuracy = (correct_answers / total_questions) * 100


# # Save evaluation results
# with open(
#     "evaluation_results.json",
#     "w",
#     encoding="utf-8"
# ) as file:

#     json.dump(
#         results,
#         file,
#         indent=4,
#         ensure_ascii=False
#     )


# # Final report
# print("\n====================================")
# print("EVALUATION COMPLETED")
# print("====================================")

# print("Total Questions:", total_questions)

# print("Correct Answers:", correct_answers)

# print(f"Accuracy: {accuracy:.2f}%")

# print("Results saved in: evaluation_results.json")

# print("====================================")
# import json
# import sys
# import os


# # =========================================================
# # 1. ADD BACKEND FOLDER TO PYTHON PATH
# # =========================================================

# backend_path = os.path.abspath(
#     os.path.join(os.path.dirname(__file__), "..")
# )

# sys.path.insert(0, backend_path)


# # =========================================================
# # 2. IMPORT YOUR WORKFLOW
# # =========================================================

# from agents.workflow import run_workflow


# # =========================================================
# # 3. LOAD TEST QUESTIONS
# # =========================================================

# questions_file = os.path.join(
#     os.path.dirname(__file__),
#     "test_questions.json"
# )


# with open(
#     questions_file,
#     "r",
#     encoding="utf-8"
# ) as file:

#     questions = json.load(file)


# # =========================================================
# # 4. EVALUATION SETTINGS
# # =========================================================

# # Use an existing user ID from your users table
# USER_ID = 1


# total_questions = len(questions)

# correct_answers = 0

# results = []


# # =========================================================
# # 5. START EVALUATION
# # =========================================================

# print("\n")
# print("==============================================")
# print("   MULTI-AGENT SYSTEM EVALUATION STARTED")
# print("==============================================")
# print(f"Total Questions: {total_questions}")
# print("==============================================")
# print("\n")


# # =========================================================
# # 6. RUN ALL QUESTIONS
# # =========================================================

# for item in questions[13:]:

#     question_id = item["id"]

#     question = item["question"]

#     correct_answer = item["correct_answer"]


#     print("\n")
#     print("----------------------------------------------")
#     print(f"Question {question_id}")
#     print("----------------------------------------------")

#     print("Question:", question)


#     try:

#         # -------------------------------------------------
#         # RUN YOUR ACTUAL MULTI-AGENT WORKFLOW
#         # -------------------------------------------------

#         result = run_workflow(

#             user_id=USER_ID,

#             query=question

#         )


#         # -------------------------------------------------
#         # GET AI RESPONSE
#         # -------------------------------------------------

#         ai_response = result["ai_response"]


#         print("\nAI Response:")
#         print(ai_response)


#         # -------------------------------------------------
#         # DISPLAY SCORES
#         # -------------------------------------------------

#         print("\nScores:")

#         print(
#             "Fact Score:",
#             result["fact_score"]
#         )

#         print(
#             "Logic Score:",
#             result["logic_score"]
#         )

#         print(
#             "Evidence Score:",
#             result["evidence_score"]
#         )

#         print(
#             "Hallucination Score:",
#             result["hallucination_score"]
#         )

#         print(
#             "Trust Score:",
#             result["trust_score"]
#         )

#         print(
#             "Trust Level:",
#             result["trust_level"]
#         )


#         # -------------------------------------------------
#         # CHECK ANSWER
#         # -------------------------------------------------

#         if correct_answer.lower() in ai_response.lower():

#             status = "Correct"

#             correct_answers += 1

#         else:

#             status = "Incorrect"


#         print("\nCorrect Answer:")
#         print(correct_answer)

#         print("Status:", status)


#         # -------------------------------------------------
#         # SAVE RESULT
#         # -------------------------------------------------

#         results.append({

#             "id": question_id,

#             "category": item.get(
#                 "category",
#                 "Unknown"
#             ),

#             "question": question,

#             "correct_answer": correct_answer,

#             "ai_response": ai_response,

#             "fact_score": result["fact_score"],

#             "logic_score": result["logic_score"],

#             "evidence_score": result["evidence_score"],

#             "hallucination_score": result[
#                 "hallucination_score"
#             ],

#             "trust_score": result["trust_score"],

#             "trust_level": result["trust_level"],

#             "status": status

#         })


#     except Exception as error:


#         print("\nERROR OCCURRED:")

#         print(error)


#         results.append({

#             "id": question_id,

#             "category": item.get(
#                 "category",
#                 "Unknown"
#             ),

#             "question": question,

#             "correct_answer": correct_answer,

#             "ai_response": None,

#             "status": "Error",

#             "error": str(error)

#         })


# # =========================================================
# # 7. CALCULATE ACCURACY
# # =========================================================

# if total_questions > 0:

#     accuracy = (
#         correct_answers
#         /
#         total_questions
#     ) * 100

# else:

#     accuracy = 0


# # =========================================================
# # 8. SAVE RESULTS FILE
# # =========================================================

# results_file = os.path.join(

#     os.path.dirname(__file__),

#     "evaluation_results.json"

# )


# with open(

#     results_file,

#     "w",

#     encoding="utf-8"

# ) as file:


#     json.dump(

#         results,

#         file,

#         indent=4,

#         ensure_ascii=False

#     )


# # =========================================================
# # 9. FINAL REPORT
# # =========================================================

# print("\n")
# print("==============================================")
# print("       EVALUATION COMPLETED")
# print("==============================================")

# print(
#     "Total Questions:",
#     total_questions
# )

# print(
#     "Correct Answers:",
#     correct_answers
# )

# print(
#     "Incorrect Answers:",
#     total_questions
#     -
#     correct_answers
# )

# print(
#     f"Accuracy: {accuracy:.2f}%"
# )

# print(
#     "Results Saved At:"
# )

# print(
#     results_file
# )

# print("==============================================")
# import json
# import sys
# import os


# # =========================================================
# # 1. ADD BACKEND TO PYTHON PATH
# # =========================================================

# backend_path = os.path.abspath(
#     os.path.join(os.path.dirname(__file__), "..")
# )

# sys.path.insert(0, backend_path)


# # =========================================================
# # 2. IMPORT WORKFLOW
# # =========================================================

# from agents.workflow import run_workflow


# # =========================================================
# # 3. FILE PATHS
# # =========================================================

# evaluation_folder = os.path.dirname(__file__)

# questions_file = os.path.join(
#     evaluation_folder,
#     "test_questions.json"
# )

# results_file = os.path.join(
#     evaluation_folder,
#     "evaluation_results.json"
# )


# # =========================================================
# # 4. LOAD QUESTIONS
# # =========================================================

# with open(
#     questions_file,
#     "r",
#     encoding="utf-8"
# ) as file:

#     questions = json.load(file)


# # =========================================================
# # 5. LOAD EXISTING RESULTS
# # =========================================================

# if os.path.exists(results_file):

#     with open(
#         results_file,
#         "r",
#         encoding="utf-8"
#     ) as file:

#         results = json.load(file)

# else:

#     results = []


# # =========================================================
# # 6. FIND ALREADY COMPLETED QUESTIONS
# # =========================================================

# completed_ids = set()

# for result in results:

#     if result.get("status") in [
#         "Correct",
#         "Incorrect"
#     ]:

#         completed_ids.add(
#             result["id"]
#         )


# print("\n====================================")
# print("MULTI-AGENT EVALUATION")
# print("====================================")

# print(
#     "Already completed:",
#     len(completed_ids)
# )

# print(
#     "Total questions:",
#     len(questions)
# )

# print("====================================")


# # =========================================================
# # 7. USER ID
# # =========================================================

# USER_ID = 1


# # =========================================================
# # 8. PROCESS QUESTIONS
# # =========================================================

# for item in questions:

#     question_id = item["id"]

#     question = item["question"]

#     correct_answer = item["correct_answer"]


#     # Skip already completed questions

#     if question_id in completed_ids:

#         print(
#             f"Skipping Question {question_id}"
#         )

#         continue


#     print("\n")
#     print("------------------------------------")

#     print(
#         f"Processing Question {question_id}"
#     )

#     print(
#         question
#     )

#     print("------------------------------------")


#     try:

#         # Run your actual workflow

#         result = run_workflow(

#             user_id=USER_ID,

#             query=question

#         )


#         # Get AI response

#         ai_response = result["ai_response"]


#         # Check correctness

#         if (
#             correct_answer.lower()
#             in
#             ai_response.lower()
#         ):

#             status = "Correct"

#         else:

#             status = "Incorrect"


#         # Create result

#         evaluation_result = {

#             "id": question_id,

#             "category": item.get(
#                 "category",
#                 "Unknown"
#             ),

#             "question": question,

#             "correct_answer": correct_answer,

#             "ai_response": ai_response,

#             "fact_score": result[
#                 "fact_score"
#             ],

#             "logic_score": result[
#                 "logic_score"
#             ],

#             "evidence_score": result[
#                 "evidence_score"
#             ],

#             "hallucination_score": result[
#                 "hallucination_score"
#             ],

#             "trust_score": result[
#                 "trust_score"
#             ],

#             "trust_level": result[
#                 "trust_level"
#             ],

#             "status": status

#         }


#         # Add result to list

#         results.append(
#             evaluation_result
#         )


#         # SAVE IMMEDIATELY

#         with open(

#             results_file,

#             "w",

#             encoding="utf-8"

#         ) as file:

#             json.dump(

#                 results,

#                 file,

#                 indent=4,

#                 ensure_ascii=False

#             )


#         print(
#             f"Question {question_id} saved successfully"
#         )

#         print(
#             "Status:",
#             status
#         )


#     except Exception as error:


#         print("\nERROR OCCURRED:")

#         print(error)


#         print(
#             "\nEvaluation stopped."
#         )

#         print(
#             "Already completed results are saved."
#         )


#         break


# # =========================================================
# # 9. FINAL SUMMARY
# # =========================================================

# completed_results = [

#     result

#     for result in results

#     if result.get("status") in [

#         "Correct",

#         "Incorrect"

#     ]

# ]


# correct_count = sum(

#     1

#     for result in completed_results

#     if result["status"] == "Correct"

# )


# incorrect_count = sum(

#     1

#     for result in completed_results

#     if result["status"] == "Incorrect"

# )


# if len(completed_results) > 0:

#     accuracy = (

#         correct_count
#         /
#         len(completed_results)

#     ) * 100

# else:

#     accuracy = 0


# print("\n")
# print("====================================")
# print("EVALUATION SUMMARY")
# print("====================================")

# print(
#     "Questions Completed:",
#     len(completed_results)
# )

# print(
#     "Correct:",
#     correct_count
# )

# print(
#     "Incorrect:",
#     incorrect_count
# )

# print(
#     f"Current Accuracy: {accuracy:.2f}%"
# )

# print(
#     "Results file:",
#     results_file
# )

# print("====================================")
# import json
# import sys
# import os


# # =========================================================
# # 1. ADD BACKEND FOLDER TO PYTHON PATH
# # =========================================================

# backend_path = os.path.abspath(
#     os.path.join(os.path.dirname(__file__), "..")
# )

# sys.path.insert(0, backend_path)


# # =========================================================
# # 2. IMPORT YOUR WORKFLOW
# # =========================================================

# from agents.workflow import run_workflow


# # =========================================================
# # 3. IMPORT GEMINI SERVICE
# # =========================================================

# from services.gemini_service import get_gemini_response


# # =========================================================
# # 4. FILE PATHS
# # =========================================================

# evaluation_folder = os.path.dirname(__file__)

# questions_file = os.path.join(
#     evaluation_folder,
#     "test_questions.json"
# )

# results_file = os.path.join(
#     evaluation_folder,
#     "evaluation_results.json"
# )


# # =========================================================
# # 5. LOAD QUESTIONS
# # =========================================================

# with open(
#     questions_file,
#     "r",
#     encoding="utf-8"
# ) as file:

#     questions = json.load(file)


# # =========================================================
# # 6. LOAD EXISTING RESULTS
# # =========================================================

# if os.path.exists(results_file):

#     with open(
#         results_file,
#         "r",
#         encoding="utf-8"
#     ) as file:

#         results = json.load(file)

# else:

#     results = []


# # =========================================================
# # 7. FIND COMPLETED QUESTIONS
# # =========================================================

# completed_ids = set()

# for result in results:

#     if result.get("status") in [

#         "Correct",

#         "Incorrect"

#     ]:

#         completed_ids.add(
#             result["id"]
#         )


# # =========================================================
# # 8. SEMANTIC ANSWER EVALUATION
# # =========================================================

# def check_answer(
#     correct_answer,
#     ai_response
# ):

#     prompt = f"""

# You are an expert answer evaluator.

# Compare the following two answers.

# CORRECT ANSWER:
# {correct_answer}

# AI ANSWER:
# {ai_response}

# Determine whether the AI answer is factually correct
# in meaning compared to the correct answer.

# The wording does not need to be exactly the same.

# If the AI answer gives the same correct meaning,
# return CORRECT.

# If the AI answer is factually wrong,
# return INCORRECT.

# Return ONLY one word:

# CORRECT

# or

# INCORRECT

# """


#     evaluation_response = get_gemini_response(
#         prompt
#     )


#     evaluation_response = (
#         evaluation_response
#         .strip()
#         .upper()
#     )


#     if "CORRECT" in evaluation_response:

#         return "Correct"

#     else:

#         return "Incorrect"


# # =========================================================
# # 9. EVALUATION SETTINGS
# # =========================================================

# # This ID must exist in your users table
# USER_ID = 1


# print("\n")
# print("==============================================")
# print("       MULTI-AGENT SYSTEM EVALUATION")
# print("==============================================")

# print(
#     "Total Questions:",
#     len(questions)
# )

# print(
#     "Already Completed:",
#     len(completed_ids)
# )

# print(
#     "Remaining:",
#     len(questions) - len(completed_ids)
# )

# print("==============================================")
# print("\n")


# # =========================================================
# # 10. PROCESS QUESTIONS
# # =========================================================

# for item in questions:


#     question_id = item["id"]

#     question = item["question"]

#     correct_answer = item["correct_answer"]


#     # -----------------------------------------------------
#     # SKIP ALREADY COMPLETED QUESTIONS
#     # -----------------------------------------------------

#     if question_id in completed_ids:

#         print(
#             f"Question {question_id} already completed. Skipping..."
#         )

#         continue


#     print("\n")
#     print("----------------------------------------------")

#     print(
#         f"PROCESSING QUESTION {question_id}"
#     )

#     print(
#         "Question:",
#         question
#     )
#     print("----------------------------------------------")


#     try:


#         # =================================================
#         # RUN YOUR MULTI-AGENT WORKFLOW
#         # =================================================

#         result = run_workflow(

#             user_id=USER_ID,

#             query=question

#         )


#         # =================================================
#         # GET AI RESPONSE
#         # =================================================

#         ai_response = result["ai_response"]


#         print("\nAI RESPONSE:")

#         print(
#             ai_response
#         )


#         # =================================================
#         # CHECK SEMANTIC CORRECTNESS
#         # =================================================

#         print(
#             "\nChecking answer correctness..."
#         )


#         status = check_answer(

#             correct_answer,

#             ai_response

#         )
# import json
# import sys
# import os


# # =========================================================
# # 1. BACKEND PATH SETUP
# # =========================================================

# backend_path = os.path.abspath(
#     os.path.join(
#         os.path.dirname(__file__),
#         ".."
#     )
# )

# sys.path.insert(
#     0,
#     backend_path
# )


# # =========================================================
# # 2. IMPORT WORKFLOW
# # =========================================================

# from agents.workflow import run_workflow


# # =========================================================
# # 3. IMPORT GEMINI SERVICE
# # =========================================================

# from services.gemini_service import get_gemini_response


# # =========================================================
# # 4. FILE PATHS
# # =========================================================

# evaluation_folder = os.path.dirname(
#     os.path.abspath(__file__)
# )


# questions_file = os.path.join(
#     evaluation_folder,
#     "test_questions.json"
# )


# results_file = os.path.join(
#     evaluation_folder,
#     "evaluation_results.json"
# )


# # =========================================================
# # 5. LOAD QUESTIONS
# # =========================================================

# with open(
#     questions_file,
#     "r",
#     encoding="utf-8"
# ) as file:

#     questions = json.load(file)


# # =========================================================
# # 6. LOAD OLD RESULTS
# # =========================================================

# if os.path.exists(results_file):

#     with open(
#         results_file,
#         "r",
#         encoding="utf-8"
#     ) as file:

#         results = json.load(file)

# else:

#     results = []


# # =========================================================
# # 7. FIND COMPLETED QUESTIONS
# # =========================================================

# completed_ids = set()


# for result in results[:25]:

#     if result.get("status") in [

#         "Correct",

#         "Incorrect"

#     ]:

#         completed_ids.add(
#             result["id"]
#         )


# # =========================================================
# # 8. SEMANTIC ANSWER CHECKER
# # =========================================================

# def check_answer(
#     correct_answer,
#     ai_response
# ):

#     prompt = f"""

# You are an expert answer evaluator.

# Compare the following answers.

# CORRECT ANSWER:
# {correct_answer}

# AI ANSWER:
# {ai_response}

# Check whether the AI answer is factually correct
# in meaning.

# The wording does not need to be exactly the same.

# If the AI answer gives the same correct meaning,
# return only:

# CORRECT

# If the AI answer is factually wrong,
# return only:

# INCORRECT

# Do not provide any explanation.

# """


#     evaluation_response = get_gemini_response(
#         prompt
#     )


#     evaluation_response = (
#         evaluation_response
#         .strip()
#         .upper()
#     )


#     if evaluation_response == "CORRECT":

#         return "Correct"


#     else:

#         return "Incorrect"


# # =========================================================
# # 9. EVALUATION SETTINGS
# # =========================================================

# USER_ID = 1


# print("\n")

# print(
#     "=============================================="
# )

# print(
#     "       MULTI-AGENT SYSTEM EVALUATION"
# )

# print(
#     "=============================================="
# )


# print(
#     "Total Questions:",
#     len(questions)
# )


# print(
#     "Already Completed:",
#     len(completed_ids)
# )


# print(
#     "Remaining Questions:",
#     len(questions)
#     -
#     len(completed_ids)
# )


# print(
#     "=============================================="
# )


# # =========================================================
# # 10. PROCESS QUESTIONS
# # =========================================================

# for item in questions:


#     question_id = item["id"]


#     question = item["question"]


#     correct_answer = item[
#         "correct_answer"
#     ]


#     # -----------------------------------------------------
import json
import sys
import os


# =========================================================
# 1. BACKEND PATH SETUP
# =========================================================

backend_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

sys.path.insert(
    0,
    backend_path
)


# =========================================================
# 2. IMPORT WORKFLOW
# =========================================================

from agents.workflow import run_workflow


# =========================================================
# 3. IMPORT GEMINI SERVICE
# =========================================================

from services.gemini_service import get_gemini_response


# =========================================================
# 4. FILE PATHS
# =========================================================

evaluation_folder = os.path.dirname(
    os.path.abspath(__file__)
)


questions_file = os.path.join(
    evaluation_folder,
    "test_questions.json"
)


results_file = os.path.join(
    evaluation_folder,
    "evaluation_results.json"
)


# =========================================================
# 5. LOAD QUESTIONS
# =========================================================

with open(
    questions_file,
    "r",
    encoding="utf-8"
) as file:

    questions = json.load(file)


# =========================================================
# 6. LOAD EXISTING RESULTS
# =========================================================

if os.path.exists(results_file):

    with open(
        results_file,
        "r",
        encoding="utf-8"
    ) as file:

        results = json.load(file)

else:

    results = []


# =========================================================
# 7. FIND COMPLETED QUESTIONS
# =========================================================

completed_ids = set()


for result in results:

    if result.get("status") in [

        "Correct",

        "Incorrect"

    ]:

        completed_ids.add(
            result["id"]
        )


# =========================================================
# 8. SEMANTIC ANSWER CHECKER
# =========================================================

def check_answer(
    correct_answer,
    ai_response
):

    prompt = f"""

You are an expert answer evaluator.

Compare the following answers.

CORRECT ANSWER:
{correct_answer}

AI ANSWER:
{ai_response}

Check whether the AI answer is factually correct
in meaning.

The wording does not need to be exactly the same.

If the AI answer gives the same correct meaning,
return only:

CORRECT

If the AI answer is factually wrong,
return only:

INCORRECT

Do not provide any explanation.

"""


    evaluation_response = get_gemini_response(
        prompt
    )


    evaluation_response = (

        evaluation_response
        .strip()
        .upper()

    )


    if evaluation_response == "CORRECT":

        return "Correct"


    else:

        return "Incorrect"


# =========================================================
# 9. EVALUATION SETTINGS
# =========================================================

USER_ID = 1


# ---------------------------------------------------------
# ONLY FIRST 25 QUESTIONS WILL BE EVALUATED
# ---------------------------------------------------------

questions_to_evaluate = questions[:25]


print("\n")


print(
    "=============================================="
)


print(
    "       MULTI-AGENT SYSTEM EVALUATION"
)


print(
    "=============================================="
)


print(
    "Total Questions:",
    len(questions_to_evaluate)
)


print(
    "Already Completed:",
    len(completed_ids)
)


print(
    "Remaining Questions:",

    len(

        [

            q

            for q in questions_to_evaluate

            if q["id"] not in completed_ids

        ]

    )

)


print(
    "=============================================="
)


# =========================================================
# 10. PROCESS QUESTIONS
# =========================================================

for item in questions_to_evaluate:


    question_id = item["id"]


    question = item["question"]


    correct_answer = item[
        "correct_answer"
    ]


    # -----------------------------------------------------
    # SKIP ALREADY COMPLETED QUESTIONS
    # -----------------------------------------------------

    if question_id in completed_ids:

        print(

            f"Question {question_id} "
            "already completed. Skipping..."

        )

        continue


    # -----------------------------------------------------
    # DISPLAY QUESTION
    # -----------------------------------------------------

    print("\n")


    print(
        "----------------------------------------------"
    )


    print(
        f"PROCESSING QUESTION {question_id}"
    )


    print(
        "Question:",
        question
    )


    print(
        "----------------------------------------------"
    )


    try:


        # =================================================
        # RUN MULTI-AGENT WORKFLOW
        # =================================================

        result = run_workflow(

            user_id=USER_ID,

            query=question

        )


        # =================================================
        # GET AI RESPONSE
        # =================================================

        ai_response = result[
            "ai_response"
        ]


        print("\n")


        print(
            "AI RESPONSE:"
        )


        print(
            ai_response
        )


        # =================================================
        # CHECK ANSWER
        # =================================================

        print("\n")


        print(
            "Checking answer correctness..."
        )


        status = check_answer(

            correct_answer,

            ai_response

        )


        print(

            "Answer Status:",

            status

        )


        # =================================================
        # CREATE RESULT
        # =================================================

        evaluation_result = {


            "id": question_id,


            "category": item.get(

                "category",

                "Unknown"

            ),


            "question": question,


            "correct_answer": correct_answer,


            "ai_response": ai_response,


            "fact_score": result[

                "fact_score"

            ],


            "logic_score": result[

                "logic_score"

            ],


            "evidence_score": result[

                "evidence_score"

            ],


            "hallucination_score": result[

                "hallucination_score"

            ],


            "trust_score": result[

                "trust_score"

            ],


            "trust_level": result[

                "trust_level"

            ],


            "status": status

        }


        # =================================================
        # ADD RESULT
        # =================================================

        results.append(

            evaluation_result

        )


        # =================================================
        # SAVE IMMEDIATELY
        # =================================================

        with open(

            results_file,

            "w",

            encoding="utf-8"

        ) as file:


            json.dump(

                results,

                file,

                indent=4,

                ensure_ascii=False

            )


        print("\n")


        print(

            f"Question {question_id} "
            "saved successfully."

        )


        print(

            "Results saved at:",

            results_file

        )


    # =====================================================
    # ERROR HANDLING
    # =====================================================

    except Exception as error:


        error_message = str(
            error
        ).lower()


        print("\n")


        print(
            "=============================================="
        )


        print(
            "ERROR OCCURRED"
        )


        print(
            "=============================================="
        )


        print(
            error
        )


        # =================================================
        # API LIMIT / QUOTA ERROR
        # =================================================

        if (

            "quota"
            in
            error_message

            or

            "rate limit"
            in
            error_message

            or

            "resource exhausted"
            in
            error_message

            or

            "429"
            in
            error_message

            or

            "too many requests"
            in
            error_message

            or

            "limit"
            in
            error_message

        ):


            print("\n")


            print(
                "=============================================="
            )


            print(
                "       API LIMIT REACHED"
            )


            print(
                "=============================================="
            )


            print(
                "Evaluation automatically stopped."
            )


            print(
                "Already completed results are saved."
            )


            print(
                "Run the script again after the limit resets."
            )


            print(
                "=============================================="
            )


            break


        # =================================================
        # OTHER ERROR
        # =================================================

        else:


            print("\n")


            print(
                "Unexpected error occurred."
            )


            print(
                "Already completed results are saved."
            )


            print(
                "Evaluation stopped."
            )


            break


# =========================================================
# 11. FINAL SUMMARY
# =========================================================

completed_results = []


for result in results:


    if result.get("status") in [

        "Correct",

        "Incorrect"

    ]:


        completed_results.append(
            result
        )


# =========================================================
# 12. COUNT RESULTS
# =========================================================

correct_count = 0


incorrect_count = 0


for result in completed_results:


    if result["status"] == "Correct":

        correct_count += 1


    elif result["status"] == "Incorrect":

        incorrect_count += 1


# =========================================================
# 13. CALCULATE ACCURACY
# =========================================================

if len(completed_results) > 0:


    accuracy = (

        correct_count

        /

        len(completed_results)

    ) * 100


else:


    accuracy = 0


# =========================================================
# 14. FINAL REPORT
# =========================================================

print("\n")


print(
    "=============================================="
)


print(
    "           EVALUATION SUMMARY"
)


print(
    "=============================================="
)


print(
    "Total Questions Completed:",

    len(completed_results)

)


print(
    "Correct Answers:",

    correct_count

)


print(
    "Incorrect Answers:",

    incorrect_count

)


print(
    f"Accuracy: {accuracy:.2f}%"

)


print(
    "Results File:",

    results_file

)


print(
    "=============================================="
)