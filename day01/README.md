### Exercise 00 : Data types

Exercise 00

Data types

Turn-in directory : ex00/

Files to turn in : data_types.py

Allowed functions : any import is restricted
* Like any other language, Python has several built-in data types. In this exercise,
you will become familiar with the most popular and useful ones.
* Create a script called data_types.py in which you need to define a data_types()
function. In this function, you need to declare 8 variables with different types and
print their types on the standard output.
* You must reproduce the following output exactly:
    
      > python3 data_types.py
      [int, str, float, bool, list, dict, tuple, set]

* It is forbidden to explicitly write the data types in your print. Remember to call
your function at the end of your script as explained in the instructions for the day:

    
        if __name__ == '__main__':
            data_types()
    
* Put your file in the ex00 folder in the root directory of your repository.

### Exercise 01 : Working with files

Exercise 01

Working with files

Turn-in directory : ex01/

Files to turn in : read_and_write.py

Allowed functions : any import is restricted

* For this exercise, you are free to define as many functions as you need and to name
them whatever you want. In the attached file ds.csv (you will recognize it from the
previous day), you will have several columns separated by a comma with different
data about vacancies.
* Design a Python script called read_and_write.py whose role is to open the file
[ds.csv](https://drive.google.com/file/d/1tDEDTytYaUrfJsXD5z5QvJSb5VNlL-eZ/view), read the data it contains, replace all the comma delimiters with ’\t’ and
save it to another file ds.tsv. Be careful, your data may contain commas. If you
replace them, you will corrupt the data.
* Put your script in the ex01 folder in the root directory of your repository.

### Exercise 02 : Search by key

Exercise 02

Search by key

Turn-in directory : ex02/

Files to turn in : stock_prices.py

Allowed functions : import sys

* You have the following dictionaries to copy to one of your functions:

        COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
        }

        STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
        }

* Write a program that takes a name of a company (ex: Apple) as an argument
and displays the stock price (ex: 287.73) on the standard output. If you give
the program a company that is not from the dictionary as an argument, your
script should display Unknown company. If there are no arguments, or too many
arguments, your program should do nothing and quit.

        $> python3 stock_prices.py tesla
        724.88
        $> python3 stock_prices.py Facebook
        Unknown company
        $> python3 stock_prices.py Tesla Apple

### Exercise 03 : Search by value and by key

Exercise 03

Search by value and by key

Turn-in directory : ex03/

Files to turn in : ticker_symbols.py

Allowed functions : import sys

* You have the same two dictionaries from the previous exercise. You should copy
them again in one of the functions of your script.
* Create a program this time that takes a ticker symbol (ex: AAPL) and displays
  the company name and the stock price with space as the delimiter. The rest of the
  behavior must be identical to that of the previous exercise.

      $> python3 ticker_symbols.py tsla
      Tesla 724.88
      $> python3 ticker_symbols.py FB
      Unknown ticker
      $> python3 ticker_symbols.py TSLA AAPL

### Exercise 04 : Dictionaries

Exercise 04

Dictionaries

Turn-in directory : ex04/

Files to turn in : to_dictionary.py

Allowed functions : any import is restricted

* Create a script named to_dictionary.py into one of the functions of which you need
to copy the following list of the tuples as is:

        list_of_tuples = [
        ('Russia', '25'),
        ('France', '132'),
        ('Germany', '132'),
        ('Spain', '178'),
        ('Italy', '162'),
        ('Portugal', '17'),
        ('Finland', '3'),
        ('Hungary', '2'),
        ('The Netherlands', '28'),
        ('The USA', '610'),
        ('The United Kingdom', '95'),
        ('China', '83'),
        ('Iran', '76'),
        ('Turkey', '65'),
        ('Belgium', '34'),
        ('Canada', '28'),
        ('Switzerland', '26'),
        ('Brazil', '25'),
        ('Austria', '14'),
        ('Israel', '12')
        ]

* Your script should transform this variable into a dictionary where the number is
the key and a country is the value. The same key may have several values as you
see. The script must display the content of the dictionary on standard output
accordingly to this precise formatting:

        '132' : 'France'
        '132' : 'Germany'
        '178' : 'Spain'
        ...

* Think about why the order is not necessarily identical to that of the example.

### Exercise 05 : Search by value or by key

Exercise 05

Search by value or by key

Turn-in directory : ex05/

Files to turn in : all_stocks.py

Allowed functions : import sys

* You still have those two dictionaries from ex02. And you should still copy them
into one of your functions in the script.
* Write a program that has the following behavior:
    * the program must take as an argument a string containing many expressions
(to find whatever you want) separated by a comma 
    * for each expression of the string, the program must detect whether it is a
company name or a ticker symbol, or neither 
    * the program should not be case-sensitive but be able to work with white spaces 
    * if there are no arguments or too many arguments, the program displays nothing 
    * when there are two commas in a row in the string, the program does not
display anything 
    * the program must display the results separated by a line break and use the
following formatting:

          $ python3 all_stocks.py 'TSLA , aPPle, Facebook'
          TSLA is a ticker symbol for Tesla
          Apple stock price is 287.73
          Facebook is an unknown company or an unknown ticker symbol
          $ python3 all_stocks.py 'TSLA,, apple'
          $ python3 all_stocks.py 'TSLA, , apple'
          $ python3 all_stocks.py TSLA AAPL

### Exercise 06 : Sorting a dictionary

Exercise 06

Sorting a dictionary

Turn-in directory : ex06/

Files to turn in : dict_sorter.py

Allowed functions : any import is restricted

* In this exercise, you need to take the list of tuples from ex04 with the countries
and numbers and make a dictionary out of it where the countries are keys and the
numbers are values . You should copy it into one of your functions in the script.
* Write a program that displays the country names in descending order by number,
then in alphabetical order by name if the numbers are equal. You need to display
one per line, without the numbers:

       The USA
       Spain
       Italy
       France
       Germany
       ...

### Exercise 07 : Sets

Exercise 07

Sets

Turn-in directory : ex07/

Files to turn in : marketing.py

Allowed functions : import sys

In this exercise, imagine that you work in a marketing department. You will operate
with different lists of email accounts. The first list is your clients’ email accounts. The
second list contains the email accounts of the participants in your most recent event
(some of them were your clients). The third list contains the accounts of your clients who
viewed your most recent promotional email.

In business terms, you need to:
* Create a list of those who have not seen your promotional email yet. The list will
be sent to the call center to reach those people.
* Create a list of the participants who are not your clients. You will send them an
introductory email about your products.
* Create a list of the clients who did not participate in the event. You will send them
a link to the video and slides of the event.

Technical details:
* Create different functions that convert your lists to sets and use the set operators
that you need to use to perform the aforementioned business tasks and return the
required lists of email accounts.
* Arrange your code in a script. The script takes the name of the task to perform as
an argument: call_center, potential_clients, loyalty_program. If the wrong name
is given, raise an exception.
* For this exercise you need to use the following three lists:

      clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
      'john@snow.is', 'bill\_gates@live.com', 'mark@facebook.com',
      'elon@paypal.com', 'jessica@gmail.com']
      participants = ['walter@heisenberg.com', 'vasily@mail.ru',
      'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
      'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
      recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']

### Exercise 08 : Working with strings as lists

Exercise 08

Working with strings as lists

Turn-in directory : ex08/

Files to turn in : names_extractor.py, letter_starter.py

Allowed functions : import sys

* Imagine that you work in a corporation where the email accounts always have the
same template: name.surname@corp.com.
* Create a script that takes the path to a file with such email accounts as an argument.
All the emails are delimited by ’\n’ in the file. The script should return a table
with the fields: Name, Surname, E-mail delimited by ’\t’. Name and surname
values should start from a capital letter. The table should be stored in the file
employees.tsv.

* Create another script that takes an email, searches the corresponding name from
the file created by the first script and returns the first paragraph of a letter:
* Dear Ivan, welcome to our team. We are sure that it will be a pleasure to work with
you. That’s a precondition for the professionals that our company hires.
* It is prohibited to use the structure ’la-la {0}’.format(text). Please, use f-strings.
They are faster and more readable.

### Exercise 09 : Caesar cipher

Exercise 09

Caesar cipher

Turn-in directory : ex09/

Files to turn in : caesar.py

Allowed functions : import sys

* There is something called [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher) that helps encode some text using a shift
in the alphabetical order. For example, the encoded version of hello might be tqxxa
if we use a shift equal to 12
* Write a program that will encode any string using a given shift or will decode any
string using a given shift accordingly to the argument given:

       $ python3 caesar.py encode 'ssh -i private.key user@school21.ru' 12
       eet -u bduhmfq.wqk geqd@eotaax21.dg
       $ python3 caesar.py decode 'eet -u bduhmfq.wqk geqd@eotaax21.dg' 12
       ssh -i private.key user@school21.ru

* If the scripts are given a string with, for example, Cyrillic symbols, the scripts
should raise the exception The script does not support your language yet. If an
incorrect number of arguments is given, raise an exception
