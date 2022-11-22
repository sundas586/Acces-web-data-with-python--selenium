# Acces-web-data-with-python--selenium

![client server](https://user-images.githubusercontent.com/33677647/202933264-b5eeed6e-727c-4e09-a43b-1b78bd0cba24.JPG)
![2](https://user-images.githubusercontent.com/33677647/202933279-a5aa80a5-91b8-46c2-8e66-bbd304a0ee35.JPG)
![3](https://user-images.githubusercontent.com/33677647/202933283-009414c9-b15d-496d-be8c-4b0c5c47a941.JPG)

- import request----> only brings the content of any HTML web page over internet, it only bring the content and not parse it.
- import HTML5 ----> will parse the content, so that content can be used by beautiful soup (import bs4).

- you need fetch HTML content of a website as a string.
- Request module has a function that can help fetch web content as a string.
- After fetching content as a string, you need to parse it as a proper structure (e.g tree like structure). for fast searching using bs4 and html5

![4](https://user-images.githubusercontent.com/33677647/202933507-6d115c50-2ccb-4bac-aa95-4d8c5f69cbfc.JPG)

- now after html string is fetched and then parsed like a tree, we need to manupulate that tree (Tree Traversal), using quries

here are the example of html trees :

![Example-of-a-HTML-page-A-its-HTML-code-B-and-the-corresponding-data-tree-structure](https://user-images.githubusercontent.com/33677647/203140568-85ce4a3f-9de4-4db1-9e0c-dd2c450eaa42.png)
![ss](https://user-images.githubusercontent.com/33677647/203140580-7eaeee45-95e5-4cbf-92cf-6c8c1c85c144.png)
![kjgg](https://user-images.githubusercontent.com/33677647/203140598-5cac7643-65b0-4155-933e-d580b896f541.png)
![jhfj](https://user-images.githubusercontent.com/33677647/203140602-a6c830b6-fcb8-4935-8950-4224661fd1b4.png)
![a](https://user-images.githubusercontent.com/33677647/203140605-d5238b38-84a2-4bfd-a697-b6171d8d3e2a.png)


![5](https://user-images.githubusercontent.com/33677647/202933727-4cf9853a-4164-4742-a2ef-5883820cc3c3.JPG)

![6](https://user-images.githubusercontent.com/33677647/202934575-c8bd3695-ddaf-4a40-998c-e21a5ad8f024.JPG)

As google , facebook etc, provides their own API for us to scrape data in their allowed way. iTS illegal to scrape data from their website with our own made web scrape API.

So once we create a tree like structure of our fetched and parse html string, it will be very easy to traverse the html string/ content, as we can ask that give us all the "div" present in content or any else thing.

## Commonly used objects in HTML :

1_ **Tags** < >
2_ **NavigableString** object (A NavigableString object holds the text within an HTML or an XML tag. Sometimes we may need to navigate to other tags or text within an HTML/XML document based on the current text. This is a Python Unicode string with methods for searching and navigation. 
It is better than normal string in python because it has some special functions)
3_ **Beautiful soup object**.
4_ Comment

![3](https://user-images.githubusercontent.com/33677647/203195641-b850819f-0686-4af3-8fa3-b4f0c0f424e1.JPG)
![1](https://user-images.githubusercontent.com/33677647/203195652-a2d5843a-1201-474f-9151-adcb57a3cf85.JPG)
![2](https://user-images.githubusercontent.com/33677647/203195659-17425156-5571-44cc-93c7-5215be0649ff.JPG)


