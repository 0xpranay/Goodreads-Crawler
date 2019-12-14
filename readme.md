# Popular Quotes Crawler

This is a Python Scrapy based crawler that crawls the popular quotes page starting at https://www.goodreads.com/quotes?page=1 and reads consecutive 100 pages.The data scraped can be saved to .CSV or .JSON fomats.

## Installing Dependencies

```pip3 install scrapy```

Execute the script by entering the following command in cmd/shell in the directory demo_project/demo_project

```scrapy crawl goodreads```

### Detailed Walkthrough

#### Starting the Spider
![starting-img](https://github.com/PranayR/Goodreads-Crawler/blob/master/Images/Screenshot%202019-12-14%20at%203.16.34%20PM.png)

#### Spider pulling the data
![process-img](https://github.com/PranayR/Goodreads-Crawler/blob/master/Images/Screenshot%202019-12-14%20at%203.17.01%20PM.png)

#### Command to export data to .CSV format
![csv-img](https://github.com/PranayR/Goodreads-Crawler/blob/master/Images/Screenshot%202019-12-14%20at%203.22.00%20PM.png)

#### Command to export data to .JSON format
![json-img](https://github.com/PranayR/Goodreads-Crawler/blob/master/Images/Screenshot%202019-12-14%20at%203.22.23%20PM.png)

#### CSV Example preview
![csvpre-img](https://github.com/PranayR/Goodreads-Crawler/blob/master/Images/Screenshot%202019-12-14%20at%203.24.45%20PM.png)

#### JSON Example preview
![jsonpre-img](https://github.com/PranayR/Goodreads-Crawler/blob/master/Images/Screenshot%202019-12-14%20at%203.25.28%20PM.png)

The .CSV or .JSON data files will be stored in the parent directory of goodreads.py File.

#### CSV JSON file location
![loc-img](https://github.com/PranayR/Goodreads-Crawler/blob/master/Images/Screenshot%202019-12-14%20at%203.26.56%20PM.png)

Image extaction spider will also be soon uploaded.
