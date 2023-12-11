import openai
import json
from copy import deepcopy

openai.api_key_path = 'creds'

def concatenate_strings(string_list):
    """
    Takes a list of strings as input and produces a single string, concatenated by spaces.

    :param string_list: List of strings to be concatenated.
    :return: A single string, concatenated by spaces.
    """
    return ' '.join(string_list)

class LLMSummarizer():
    def __init__(self):
        self.prompt = "Your role is to summarize the text as described below.\n\n"


    def summarize(self, input_text, mode='data_extractor'):
        prompt = deepcopy(self.prompt)
        print(f"prompt: {prompt}")
        print(f"type(prompt): {type(prompt)}")

        print(f"input_text: {input_text}")
        input_text = concatenate_strings(input_text)
        print(f"input_text: {input_text}")

        prompt += input_text
        
        # Send the prompt to the model
        response = openai.Completion.create(    
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=500
        )
        # Extract the summary from the response
        summary = response.choices[0].text.strip()
        return summary
    
if __name__ == "__main__":
    from termcolor import colored
    llm_summarizer = LLMSummarizer()

    original = """
AUTO LOAN AGREEMENT
THIS AGREEMENT is made this 1st day of March, 2023.

BETWEEN:
ABC Auto Loans 157, a financial institution duly organized and existing under the laws of the state, having its principal place of business at 2793 Elm St, Springfield, USA (hereinafter referred to as the "Lender").

John Doe 951, an individual residing at 512 Main St, Springfield, USA (hereinafter referred to as the "Borrower").

RECITALS:
WHEREAS, the Borrower has requested the Lender to extend a loan to the Borrower for the purpose of financing the acquisition of a vehicle described in detail in ARTICLE 1;

WHEREAS, the Lender has agreed to extend such a loan to the Borrower on the terms and conditions set forth herein;

NOW, THEREFORE, in consideration of the mutual covenants contained herein and other good and valuable consideration, the receipt and sufficiency of which are hereby acknowledged, the parties hereto agree as follows:

ARTICLE 1 – LOAN DETAILS
1.1 Loan Amount
The Lender agrees to lend to the Borrower, and the Borrower agrees to borrow from the Lender, the principal amount of FIFTY-TWO THOUSAND FIVE HUNDRED FIFTY-TWO UNITED STATES DOLLARS (US$52,552) (the "Loan").

1.2 Interest Rate
The Loan shall bear interest at a rate of nine point sixty-seven percent (9.67%) per annum, calculated on the basis of a 360-day year for the actual number of days elapsed.

1.3 Loan Term
The term of the Loan shall be forty-four (44) months, commencing on the date hereof and ending on the last day of the forty-fourth month thereafter, unless sooner terminated in accordance with the terms hereof.

1.4 Down Payment
The Borrower has made a down payment of THREE THOUSAND EIGHT HUNDRED SEVENTY-FOUR DOLLARS AND SEVENTY-SEVEN CENTS (US$3,874.77) towards the purchase of the vehicle.

1.5 Repayment
The Borrower shall repay the Loan in monthly installments of principal and interest, with the first installment due on April 1, 2023, and subsequent installments due on the first day of each month thereafter.

1.6 Vehicle Details
The loan is extended for the purpose of financing the acquisition of the following vehicle:

Make: Hyundai
Model: Van
Year: 2016
VIN: WIK3ZNEGTQ4JOSX8U
ARTICLE 2 – REPRESENTATIONS AND WARRANTIES
The Borrower hereby represents and warrants to the Lender as follows:

2.1 Legal Age
The Borrower is of legal age to enter into binding contracts in the jurisdiction where the Borrower resides.

2.2 Accurate Information
All information provided by the Borrower to the Lender, including but not limited to the Borrower’s financial condition, is true, correct, and complete.

(Additional representations and warranties would include details regarding no conflicts, litigation, accuracy of information, etc.)

ARTICLE 3 – COVENANTS
The Borrower covenants and agrees with the Lender as follows:

3.1 Maintenance of the Vehicle
The Borrower shall maintain the vehicle in good working condition and shall bear all costs associated with the maintenance of the vehicle.

3.2 Insurance
The Borrower shall maintain comprehensive insurance on the vehicle at all times during the term of the loan.

(Additional affirmative and negative covenants would be detailed in this section, including financial reporting requirements, restrictions on indebtedness, etc.)

ARTICLE 4 – EVENTS OF DEFAULT
The following shall constitute events of default under this Agreement:

4.1 Non-Payment
Failure by the Borrower to pay any amount due under this Agreement within ten (10) days of the due date.

4.2 Breach of Representation
Any representation or warranty made by the Borrower herein proves to have been incorrect in any material respect when made.

(Additional events of default would be detailed in this section, including bankruptcy events, cross-defaults to other agreements, etc.)

ARTICLE 5 – MISCELLANEOUS
5.1 Notices
Any notice or other communication required or permitted to be given hereunder shall be in writing and shall be deemed to have been duly given when delivered in person, or sent by registered mail, to the respective parties at the addresses set forth above.

5.2 Governing Law
This Agreement shall be governed by and construed in accordance with the laws of the state, without regard to conflict of laws principles.

(Additional miscellaneous provisions would include details regarding amendments, waivers, severability, etc.)

IN WITNESS WHEREOF, the parties hereto have executed this Agreement as of the date first above written.
ABC Auto Loans 157
By:_________________
Name: (To be filled in)
Title: Loan Officer

John Doe 951
By:_________________
Name: John Doe 951
Title: Borrower

DISCLAIMER:
THIS DOCUMENT IS A MOCK REPRESENTATION CREATED FOR DEMONSTRATION PURPOSES ONLY. IT IS NOT INTENDED TO BE USED FOR ANY REAL LEGAL OR COMMERCIAL TRANSACTIONS.


    """

    summary = llm_summarizer.summarize(original, mode='data_extractor')

    print(colored(f"original: {original}", 'blue'))
    print(colored(f"summary: {summary}", 'yellow'))