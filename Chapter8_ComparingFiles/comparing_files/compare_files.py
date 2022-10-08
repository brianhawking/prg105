"""
For this assignment, you will compare the contents of two files and display customer
information only for those customers whose accounts are overdue.

Download both files:
 accounts.txtDownload accounts.txt     # customer accounts
 over90.txtDownload over90.txt      # overdue account numbers

Read the files into two separate lists. Print the complete customer information on
the screen if the customer number is found in the overdue accounts list. Do error
checking for file names to make sure the files exist (try and except statements.)
"""


def main():
    # Initialize
    accounts = []
    overdue_accounts = []

    # Open both files
    try:
        accounts_file = open('accounts.txt', 'r')
        overdue_file = open('over90.txt', 'r')

        # Populate accounts and overdue_accounts arrays
        for account in accounts_file:
            accounts.append(account.rstrip('\n'))

        for overdue in overdue_file:
            overdue_accounts.append(overdue.rstrip('\n'))

        print("The list of overdue accounts are: ")
        # Loop through all overdue accounts and find if that account exists
        # in one of the elements in the accounts array
        for overdue_account in overdue_accounts:
            for account in accounts:
                if overdue_account in account:
                    print(account)

    except Exception:
        print("Error opening one of the files.")


# ======= START PROGRAM ==================
main()
