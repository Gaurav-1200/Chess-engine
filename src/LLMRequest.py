import google.generativeai as genai
from apikey import api_key
import re


def makeLLMRequest(FEN_Notation, last_move, board):
    genai.configure(api_key=api_key)     #expired Key
    model = genai.GenerativeModel("gemini-1.0-pro")
    finalRow = last_move.final.row
    finalCol = last_move.final.col
    piece = board.squares[finalRow][finalCol].piece.name
    prompt = f"""
    You are an expert Chess player. You are playing as"black". Analyze the current board position provided in FEN notation:
    {FEN_Notation}

    The board is represented as a 0-indexed grid. 
    - Black pieces occupy rows 0 and 1 at the start of the game.
    - White pieces occupy rows 6 and 7 at the start of the game.
    - Kings are initially placed in column 4.

    Your task is to determine the best next move for "black" based on the FEN notation. You should not explain your move, only give the best move.
    The last move of white was ({piece},{last_move.initial.row},{last_move.initial.col},{last_move.final.row},{last_move.final.col})

    **Output format**:("InitialRow", "InitialCol", "FinalRow", "FinalCol").  
    Ensure the move is valid according to the rules of chess. Invalid moves will not be accepted.
    """
    print(prompt)
    response = model.generate_content(prompt)
    print(response.text)
    response = response.text
    response = response.strip().strip('()')
    
    # Use regex to extract move details
    match = re.match(r'\s*(\d+),\s*(\d+),\s*(\d+),\s*(\d+)', response)
    if not match:
        raise ValueError("Invalid response format")
    
    initial_row, initial_col, final_row, final_col = match.groups()

    return [initial_row, initial_col, final_row, final_col]


# import chess

# Replace with your OpenAI API key
# OpenAI.api_key = ""

# def get_llm_move(fen: str, prompt_context: str = None) -> str:
#     """
#     Uses an LLM to decide the best move from a given FEN string.
#     Args:
#         fen (str): FEN string representing the chess board state.
#         prompt_context (str): Optional additional context for the LLM.
#     Returns:
#         str: Suggested move in UCI format (e.g., e2e4).
#     """
#     # Construct the LLM prompt
#     prompt = (
#         f"The chess board is in the following position:\n{fen}\n"
#         "Suggest the best next move in UCI format (e.g., e2e4).\n"
#         " Only suggest the best move and do not explain"
#     )
#     if prompt_context:
#         prompt += f"Context: {prompt_context}\n"

#     print(prompt)

#     response = openai.ChatCompletion.create(
#         model="gpt-4",  # Specify a capable LLM
#         messages=[
#             {"role": "system", "content": "You are a chess expert."},
#             {"role": "user", "content": prompt}
#         ]
#     )

#     # Extract and return the LLM's response
#     print(response['choices'][0]['message'])
#     print("-------------------------------------------->")
#     move = response['choices'][0]['message']['content'].strip()
#     print(move)
#     return move
    

# # from openai import OpenAI
# from openai import OpenAI


# def get_llm_move(fen):
#     client = OpenAI(api_key = "")

#     prompt = (
#             f"The chess board is in the following position:\n{fen}\n"
#             "Suggest the best next move in UCI format (e.g., e2e4).\n"
#             " Only suggest the best move and do not explain"
#         )
#     print(prompt)
#     print("------------------------------------------------")
#     completion = client.chat.completions.create(
#         model="gpt-4o-mini",
#     messages=[
#                 {"role": "system", "content": "You are a chess expert."},
#                 {"role": "user", "content": prompt}
#             ]
#     )
#     print(completion)
#     print("######################################3")
#     print(completion.choices[0].message)


