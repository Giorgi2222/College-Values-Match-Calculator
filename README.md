# College-Values-Match-Calculator

<img width="1439" alt="finance" src="https://user-images.githubusercontent.com/108226998/202897161-ec83186f-2fdb-42f7-9c47-2a08c3dbfe21.png">
A bot to scrap texts from websites and draw insights from them.

## Purpose

College's declared values can be confusing and very similar to one another. This app helps to measure what is relatively more important for college. If a word appears frequently on hundreds of pages on the website, that is a good measure of its importance.    

## Technical details

The app consists of two files. First is a web scrapper, which derives text from a page of the college website, finds inside links on that page, and puts them into a queue to be explored next. The second file uses the first one to actually analyze texts from websites.
