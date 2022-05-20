## web-scrapping-NDTV
## About task1
### this file can be runed only one time.

 firstly I have imported these modules
* requests
* bs4 library
* json
* pprint
As I want to scrap the story of 5 pages,that is why I need to change "url" for the different pages.
so, I used **"for loop"** , that iterate till 5,
According to that page url get changed every iteration.

After that I scrapp thiese informations
*title of the story
*image url
*author name
* date
* description
by inspecting the page.

I stored each story's detail in a dictionary and after that appended each dictionary to a **main_data**, list.
After that I created the **json** file,named as **news.json**, and dump the **main_data** file there.

___________________________________________________________________

## About **Task2**

In this file also I done the same thing as task1, and stored the data in the list named as **new_data**...
I read **(load)** the **news.json** file in task 2 , as **old_data**.

After that I loop through the new_data, and checked that if any news in this file is "" not in"" the old_data,
then **insert** that news to old_data file.

After completing I stored **new_data** file in json as **news1.json**.

