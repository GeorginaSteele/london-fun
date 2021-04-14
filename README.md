# london-fun
A repo to create a map of fun (mainly foodie) things to do in London



## MVP

The MVP UI should look similar to the below diagram. The pop up information box should appear when hovered over/ clicked. Location pins on the map can be filtered by category/ time of day. 

![MVP UI](https://user-images.githubusercontent.com/65658835/113923032-f3e05a80-97df-11eb-92b3-9b503bf98a38.png)

Places in London will be kept in a json file to begin with (could expand this to use a DB in the future) and stored with the following information:
* Name (string)
* Category (enum of strings)
* Time of Day (enum of strings)
* Website (string)


## Technology to Investigate

Technologies that might be helpful for this project:
* Django - high level python web framework
* Flask
* Fastapi
* Starlette

## Expansion Ideas

* Add a category for type of food (for the food places) and be able to filter on this too
* Have a similar project for cycling cafes
* Expand json file of places to database
* Colour-code the location pins according to category
