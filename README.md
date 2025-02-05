# Roboarena-Team-2
## Sprints
### Sprint 1 (04.04. - 24.04.2023)
- Created the Roboarena-Team-2 repository
- Set up the [GitHup.io page](https://robo-arena-team-2-uni-tuebingen.github.io/Roboarena-Team-2/)
- Added a workflow with a Flake8 test which checks the syntax of uploaded Python code
- Created and tested the first programms and pushed them to the repository. All passed the Flake8 test

### Sprint 2 (26.04. - 09.05.2023)

#### Repository update
- changed repository to organization repo to give equal admin rights
- setting up Kanban for future sprints

#### Wireframe
![wireframe](https://user-images.githubusercontent.com/83218599/236781331-fe7f95dc-c2bc-4c22-b083-839dffdfba7d.png)

#### Arena class (by Niklas Wolf)
![arena-class](https://user-images.githubusercontent.com/83218599/236781672-8ad60e9a-917e-40a3-bf30-762b0ba8af87.png)
- the size of the arena are set at the beginning of the class
  - `TileHeight` and `TileWidth` define the size of the single tiles in pixels
  - `ArenaHeight` and `ArenaWidth` define the number of tiles
- the layout of the arena get saved in a matrix which is randomly filled at the beginning
  - the integers 0-5 represent the different tile types
  
 ![draw-tiles](https://user-images.githubusercontent.com/83218599/236783524-cb39afd0-7526-4da4-9bc3-08d22aa5d660.png)
- `paintEvent` iterates through the entrys of the matrix and calls `drawTile` which paints the single tiles
- color of the tiles is defined by the array `colorTable` (integer in the matrix ArenaLayout is index in colorTable)

![widget-with-arena](https://user-images.githubusercontent.com/83218599/236785209-5d0fb1ae-c55a-47c8-bbd9-6c9795df245e.png)
- the main window creates an arena as a widget

![random-arena](https://user-images.githubusercontent.com/83218599/236785494-0a48e9a5-9df2-439c-81fb-60163cee000c.png)
- result of a random arena layout

#### Arena Refactor (by Julian Häberle)

- implemented ability to manipulate single tiles
- implemented ability to assign more attributes to tiles
- reason for this was mostly to lay a foundation for longterm considerations

![grafik](https://user-images.githubusercontent.com/67464857/236786951-a1109422-72d1-4d12-86dc-e6f7375b466d.png)
- refactored `initArena`

![grafik](https://user-images.githubusercontent.com/67464857/236787104-4b581091-6326-45cd-9f74-acc15093371f.png)
- refactored `paintEvent` + `drawTile`

![grafik](https://user-images.githubusercontent.com/67464857/236787439-1d5b2065-1105-4737-862a-ed426ed09a99.png)
- new tiles class, which consists of a tile superclass and six tile subclasses

#### Robot (by Julian Häberle)

![grafik](https://user-images.githubusercontent.com/67464857/236787607-9fd22dec-1424-468d-88fe-359871806ce0.png)
- newly added `robot` class
- implemented all the required attributes (x, y, radius, alpha)
- minor problems with the alpha attribute, currently it doesn’t correctly respond to a input in degrees and requires an input as a fraction of pi instead, fix for that will come with the next sprint
- implemented a getAlpha method that is supposed to calculate the angle (relative to the x-axis) to any given point in preparation for a possible mouse-control scheme, currently untested though

![grafik](https://user-images.githubusercontent.com/67464857/236787884-939f4066-282c-4cdc-90a1-aa2ec010bda1.png)
- newly added method `drawRobot`, which is called from `paintEvent`
- calculates the point indicated by the angle and radius and then draws a line between it and the center of the robot
- minor problems with the flipped y-axis of the drawing, took a while to figure out, the solution was to flip the y-component of the calculation
- color orange to differentiate a bit from the tiles

![grafik](https://user-images.githubusercontent.com/67464857/236786215-f5586590-0c8e-4e42-89b9-f123d0026a9f.png)
- result of `drawRobot`

#### Movement (by Tom Kuehnle)
 - Creating timer using `QBasicTimer`
 - Setting time interval for movement ticks
<img width="627" alt="Bildschirmfoto 2023-05-08 um 10 41 35" src="https://user-images.githubusercontent.com/104011823/236791094-2d23c1c6-08fa-4b71-b69b-3700b3a2495b.png">

 - Creating `timerEvent`
 - Center of the robot moves on tiles
 - random selection of the directions up/down/left/right
 - using `TileLength` `TileWidth` and size of the arena to determine new robot position

<img width="634" alt="Bildschirmfoto 2023-05-08 um 10 41 44" src="https://user-images.githubusercontent.com/104011823/236923711-c9a7d32f-cebc-419e-a2c5-432f09112f77.png">


![Bildschirmaufnahme-2023-05-08-um-22 06 00](https://user-images.githubusercontent.com/104011823/236923814-b33b7c6a-0396-4932-879c-1d11fb63b037.gif)

### Sprint 3 (09.05.2023 - 23.05.2023)

#### Map Generator (by Julian Häberle)
- basic implementation of a randomly generated map
- uses a basic 2D simplex noise function from https://github.com/caseman/noise
- can't get it to work within the required parameters of the new tileset atm, which is why it's considered non-functional and hasn't been merged into the main yet

![grafik](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/2f416593-0e6d-4fb3-a6d8-508493e1babe)

- this particular noise function always creates the same noisemap
- random factors to shift and scale the area of interest on the noisemap

Example of a generated map (with old tileset):

![grafik](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/125645e1-7724-4c3b-a60a-c620e3f6be46)

#### Load map from ASCII text file (by Niklas Wolf)
![image](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/83218599/ae30cc9c-4638-4fe7-9ee8-2f15499946fe)
- `textToMatrix` converts a text file into a matrix of the single characters
- every line of the text file is a row in the matrix

![image](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/83218599/0535e3ae-ee79-445c-9ac7-d807257f3421)
- `translateAscii` compares a given character with the diffrent cases and returns the corresponding tile type
- the dafault for undefined characters is `NormalTile`

![image](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/83218599/87cc52f6-3c91-40ca-b103-0426b9504a46)
- `textToTiles` converts a given text file to a matrix of tiles
- `translateAscii`gets vectorized to apply it to every entry of the matrix

Example Map:

![image](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/83218599/0cefb76f-a642-46b1-ab60-410745133d6c)
![image](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/83218599/83507485-580b-4913-8799-dfddbd1370de)
- a problem with this solution is that the the text file must already have the correct dimensions of the arena

#### Graphical Tilesets and changes to the existing tileset (by Julian Häberle)
- we decided on using the Open RPG Fantasy Tileset from https://finalbossblues.itch.io/openrtp-tiles
- replaces the old tileset (Fire, Sand, Normal, Water, Ice, Wall) with a new tileset (Wall, Water, Grass, Dirt, HighGrass, Sand, Snow, Slime, Field, CobbleStone)
- this was done to implement smoother transitions and make the map look cleaner
- to accomodate for the increased tile size (16x16 vs 10x10) the size of the arena has been decreased from 100x100 to 60x60 tiles

The three mainfiles of the Open RPG Fantasy Tileset:

![dungeon](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/7950e1b6-d208-4c10-868a-346f213bfa9f)
![exterior](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/801c9fe1-9851-40a4-96ec-72393077386b)
![interior](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/af8540c2-cd2e-4538-b879-97095a522487)

Initializing and new helper functions:

![grafik](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/b0c5c7ec-e92d-48ca-8b62-19a0d9a6b139)
- Images are loaded into dungeon, exterior and interior
- `getTileRect` cuts a single tile out of the bigger images
- `getBigTileRect` cuts a 3x3 tile area out of the bigger images
- tiles that do not implement a transition atm (Wall, Water, Grass (Grass is the default tile that every other tile transitions to)) only cut out a single tile
- tiles that do implement a transition cut out a big tile

Changes to the tile super class:

![grafik](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/5ea6af45-0287-4bcf-a97e-f625d3a817e3)
- added an attribute `str` that contains the ascii character for the specific tile
- this was done to avoid typechecking in various situations
- the compare method uses this string to compare its own tile with another given tile

![grafik](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/00b3e48f-2140-401b-bb8c-a19a96e75f9c)
- the chooseTexture method requires a list of four tiles as a parameter, the tiles above, below, left and right of the own tile
- this is a bit of a codesmell, but was done in case the function is later expanded to include all 8 context tiles
- the function then compares which of the tiles in the context is a tile of the same type
- based on that information, the appropriate tile is cut out from the big tile (which is the current texture) and assigned as the new texture of the tile
- if the tile does not match to a transition in the big tile, the standard tile is chosen
- this poses a bit of a limitation in a map design aspect as it currently requires all patches (save for patches without transitions) to be at least 2x2 (with some more limitations)

Example:

![grafik](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/f45eaec9-866b-4057-84bf-f424e8f7d9e1)
- the blue marked area is the big cutout for the DirtTile
- the red cutout would be the chosen tile if the tile to the left and above would be of a different type

Tiles without implemented transition:

![grafik](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/a7752a5e-8631-4c4c-bd00-906e72c80676)
- tiles without transition override the `chooseTexture` function to just return their current texture

![grafik](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/30a30f80-35e8-4854-be89-b6168b694662)
- the `chooseTexture` function is executed once on every tile object in `ArenaLayout` after the layout has been generated
- corner cases are just assigned the `Tile` superclass for missing tiles to avoid null errors
- some minor changes to `robo-arena` as well as some minor changes to `ascii_layout`, but nothing noteworthy

Test map:

![grafik](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/b9c821db-5828-4fac-b0c6-3a4656015b2a)

#### Extend the robot class (by Niklas Wolf)
![image](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/83218599/6ce8da41-99bf-4831-a527-cc9984d99008)
- added variables that store information about the current velocity and acceleration
- at the beginning velocity and acceleration are 0 at the beginning and change with the actions of the player
- the maximum accelerations are arbitrary so far and we have to test which values make sense
  
![image](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/83218599/477cac12-b822-4afe-8c04-eb0ab34d017e)
- extended the `update` function to also change the speed parameters
- new accelerations get added to the old values 
- if they exceed the maximum acceleration, the maximum is taken as the acceleration value
- the new velocitys are calculated from the current velocitys and the new accelerations in relation to the time
- problem: we are not sure yet how some values should processed
  - negative velocity = robot moves backwards?
  - maximum velocity?  

![image](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/83218599/334d0797-8fa7-48d9-b86b-3e2c30a274a7)
- stored four robots in an array so it's easier to change the number of used robots between 1 and 4
- added the parameter color to the constructor so every robot has its indivdual color
  
![image](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/83218599/20294529-31dc-48a3-a23d-00511f3cd5f3)
- placed four robots on the playing field

#### Create (Q)Threads to move Robots 

- initializig threads in the arena class
- open a thread for each robot given and start them
- update(redraw) the widget with new robot positions
<img width="992" alt="Bildschirmfoto 2023-05-23 um 07 00 48" src="https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/104011823/732957fa-cfbe-4455-a9dc-c1a6ca217a45">
 
 -> We still redraw the whole widget, but for optimization we want to try to only redraw the robots
    or a smaller part of the widget where the robot(s) is located.

Creating new class RobotThread
 - track the current position of the assigned robot
 - initialize all the robot values needed for calculations
 - constant loop to move the robot updating every 50 ms (still to be modified)
 - (random) movement function put in the thread so each robot movement can be
   calculated independent

<img width="668" alt="Bildschirmfoto 2023-05-22 um 15 58 31" src="https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/104011823/ab3eb9e1-223f-481d-b84a-1e83b7374b7f">
 
Reworked the movement function and smoothend the movement
 - using speed of the robot
 - calculate a line between current and target tile
 - move on the line until  arrival at new target position (update every 10ms)  
      -> movement looks smoother // robot doesnt jump from tile to tile
 - check if target position is reached and create new target position if needed

<img width="633" alt="Bildschirmfoto 2023-05-22 um 15 58 49" src="https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/104011823/f6d279d8-2612-4e46-a70f-f81dfbf75f26">

- New target position is calculeted using only the tiles around current position (also diagonal neighbours)
- Checking for Arena borders

<img width="698" alt="Bildschirmfoto 2023-05-22 um 15 58 41" src="https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/104011823/d6515b88-a108-4188-9e8b-734656b90c71">

Experimented with different movement styles and tried to implement different tile logics,
for example that water or wall tiles can't be generated as new tiles:

<img width="794" alt="Bildschirmfoto 2023-05-23 um 07 30 35" src="https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/104011823/caea88ff-a4e1-4fe5-b7b9-c01b6be304b8">

But nothing is implemented yet since there were some unsolved issues,
as well as acceleration logic either for normal or rotational movement.

-> Until appropriate acceleration and tile logic is implemented we initilized
   a deafault movement speed of 2 so the random movement function can move the robot
   
<img width="282" alt="Bildschirmfoto 2023-05-23 um 06 55 15" src="https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/104011823/28ffb43f-10c8-481b-9c5c-c57606cf1d72">
   
### Sprint 4 (23.05.2023 - 06.06.2023)

#### Necessary tasks to reach our minimum viable product: (by Niklas Wolf, Tom Kuehnle, Julian Häberle)
- implement a control scheme (currently planned to be WASD & Mouse controls for a single robot)
- implement a basic game loop and game logic (setting up the game, resetting the game, victory and lose conditions, what happens when an enemy or the player dies, what happens when an enemy or the player spawns, etc.)
- main menu, for choosing a map and a difficulty (amount of enemies)
- pause menu, for pausing or quitting the game (to desktop or to main menu) (ESC-Key)
- several maps (+ a map editor tool, maybe)
- multiple kinds of enemies and their corresponding behaviour
- a damage model that applies to enemies and player
- tile logic (what effect has a tile, does the effect apply to enemies and/or player, etc)
- movement logic (where can enemies and the player move, how fast can they move there)
- implementation of several weapons
- implementation of a better robot model (for enemies as well)
- general optimization of drawing and calculating as we see fit (parts with the potential for optimization will crystalize out during development)

Some of these tasks depend on each other (for example the main menu and pause menu need to be implemented before you can implement a basic game loop)

![RoboPlan](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/104011823/1a38c19b-90e7-41b9-a716-fd7902163954)

### Sprint 5 (06.06.2023 - 20.06.2023)

#### Movementlogic (by Tom Kuehnle)

- Created simple WASD movement logic for player controlled robot
- Created keypress event to pass to the robot thread(s)

![keypressEVENT](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/104011823/440bd4ad-ae79-419f-86a6-0c70bc32aa46)

 -> didnt work initially since the keypress event was located in the wrong class,
    but Julian resolved the issue

- Creating `is_player` flag for robots which will additionaly be passed for thread creation,
  for assigning the right movement method to the robot threads

![robott_isplayer](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/104011823/a27db33e-d1f1-427c-8c59-b29187949314)

adding `is_player` to robot class

![playerflag](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/104011823/99a844a9-a107-4b2c-b9fe-23b2072f6e0b)

using `is_player` in thread creation

- updating threads to check for the new flag and deciede on the right movement method

![completethread](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/104011823/e81acb22-bd47-4a42-a6e7-0db41c34912a)

-> Attempted to base the WASD movement on the movement in my moverobotsmoothly fuinction, so that the robot calculates a target positions based on my 
keypresses which was meant to enable diagonal movement if there are two simultanious keypresses, but this turned out to be very complicated and did not work properly, e
ven in non diagonal attempts - no screenshots unfortunately -> will document more precisely next time

- Started to work on some concepts for bullet shooting (e.g. a bullet class and collision detecting)
- Started to work on some concepts for lifebars / health game logic
    -> both are still very undefined concepts but I will document my progress to present next week


#### Refinement of Movementlogic (by Julian Häberle)
- Two main reasons for refinement are to allow simultaneous input and to enable smoother movement by changing the existing logic to a vector based logic
- Simultaneous input is handled by a dictionary that tracks which keys are pressed and released through the KeyPress and KeyRelease events
- also added the keys Q and E to the existing WASD Keybind to control Decceleration and Acceleration

![grafik](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/3a88321c-36f4-493c-a05b-8bd97b027f89)
- The initial dictionary

![grafik](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/93f34587-903b-48de-8677-32b25daa25e6)
- logic in the `robo-arena` class which handles the inputs and passes them to the thread in question
- currently the playerthread is always on position 0 in the array, this is intentional but has to be kept in mind should that change later

![grafik](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/20fa24e9-d106-467f-8684-b853495d0adb)
- in the `thread` class the target is then changed according to the input in the dictionary, the resulting target is passed to the robot, to provide necessary information that the paintEvent needs to draw the target indicator

![grafik](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/b522e55a-9aea-4bac-8f02-f4d73bc3124d)
- the new `moveRobotSmoothly` function, then calculates a vector to the target and moves the robot according to its current speed along it
- I have experimented with automatic acceleration and deceleration based on a comparison between old and new target vector but couldn't get it to work and opted for a manual control of acceleration and decceleration

![grafik](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/3ed2f9f7-2cfe-467f-a3d5-8ffde9fb9005)
- the `accelerate` and `decelerate` functions merely add/subtract the acceleration from the current speed and then enter a one second long cooldown

#### Implementation of Mousehandling (by Julian Häberle)
- The Mouse is supposed to control the weapons through the buttons and direction of view through the general position of the robot later
- To allow for simultaneous input the Mouse also uses a dictionary to track Click and Release events
- Due to setting the `setMouseTracking` property of the QWidget to true, a mouseevent triggers on every movement of the mouse, as opposed to every click

![grafik](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/fed07785-7e4f-4b5e-86d6-8cb871185f9b)
- Due to the possibility of simultaneously pressed buttons in a single event, the logic looks a bit different than it does for the keyEvents
- the `event.buttons()` function returns an 8-bit sequence that is then compared to the bit sequence of the key of the dictionary with a bitwise And, the result of this comparison indicates whether the button in question was clicked or not

![grafik](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/febab1d3-e938-40a1-a078-50f7a5513406)
- the coordinates of the mouseevent and the dictionary are then passed on to the relevant thread
- currently only the coordinates are used to calculate the direction of view of the robot
- the coordinates are then saved in a property of the thread and passed to the robot in the `run` function of the thread
- this is to make sure that the robot is always directed at the mouse, even if the mouse is not moving

![grafik](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/c2cbf704-cad5-4b19-a348-88c2598e526b)
- in the `run` function the coordinates get passed into the `getAlpha` function of the robot class
![grafik](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/398c32e3-6e88-404d-84c7-ade99b2de411)
- the `getAlpha` function then calculates the respective angle to the x-Axis
- this needs to be inverted since the y-axis of the coordinates is inverted

#### Tile and Effect Logic (by Julian Häberle)
- the tile logic handles whether a tile is impassable or has an effect
- this requires further modifications to the movement that I didn't get around to yet
- effect logic handles how an effect applies, how it is removed and how it influences the entity it is applied to
- currently there are five effects: Slow, Freeze, Corrosion, Collateral and Speedup
- Slow reduces acceleration and maximum Speed
- Freeze reduces accuracy and enemies inflict more damage
- Corrosion makes enemies inflict significantly more damage
- Collateral is WIP, currently undecided what it does
- SpeedUp raises maximum Speed and provides a slight acceleration buff
- each effect has an intensity, the more stacks of an effect an enemy or player gets the more it'll be influenced by it
- some times have the same effect but apply them with a different intensity
- it's possible to have multiple effects of different intensities on one entity
- effects decay naturally over time
- after an effect is applied there's an immunity period for a certain amount of time until the next effect can be applied
- not yet decided whether the effect comes from the tile the center of the robot is on or whether the effect stems from all tiles the robot touches
- There's already some code for it but it's still WIP and not merged, since it misses crucial functionality, which will be added during the next sprint

![grafik](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/a006315b-a23a-46e7-b77b-4352ed56e5ec)
- effects are tracked in a dictionary, the apply/remove cooldowns are tracked in their own booleans to make use of a singleshot timer

![grafik](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/f82f3a93-0bff-41e7-81f7-bcce06728cf1)
- implementation of `applyEffect` and `removeEffect`
- effects come as a tuple of str, int#
- originally I intended to give them their own objects with an internal cooldown and so on, but this turned out to be easier

![grafik](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/310a6cf1-c7f4-4dfd-b4d2-a28e587be873)
- examples for the added attributes to the tile class

#### Pausing the Game (by Niklas Wolf)
For stopping the robots:

![image](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/83218599/797eefdf-71fd-426f-9eaf-d139d2e0a27a)
- key events have now to be handed over to every thread to give them the signal to pause
- added an `is_paused` flag to the threads to overview the status

![image](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/83218599/110dde88-62c6-4a14-9bd4-d1ffb4cfb837)
- if the `is_paused` flag is `True` the positions of the robots don't get changed unless it's `False` again
- first tried to break the `while`-loop and call `run()` later to reactivate the robots but that didn't work

![image](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/83218599/06162cca-8d91-46de-a7d4-3f8de46bb108)
- the robot of the player only accepts key events if the game isn't paused so you can't move your target during the pause

![image](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/83218599/69cd3b0f-cfde-48e2-a646-2d0a4319dde8)
- every robot processes the input of `Esc` which just swaps the value of the `is_paused` flag for now

Show the pause menu:

![image](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/83218599/534191bd-18b4-4687-88df-8b68406a8f6f)
- implemented the `PauseMenu` class which contains the widget pause menu
- the pause widget has:
  - a `Resume` button that resumes the game and hides the menu again
  - a `Quit` button that closes the game for now. When we implemented a main menu it brings you back to it
  - a slider that will adjust the volume if we add in-game sounds

![image](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/83218599/ae483e5c-65dc-43df-a8a2-1f49d4c87f13)
- the `Resume` button emulates pressing the `Esc` key to resume the game
- so you can resume the game with the `Esc` key also

![image](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/83218599/1803f939-e392-4940-8471-44ae097b5350)
- added the pause-menu-widget to the main window
- for now, the pause get shown just beside the arena, we'll discuss the overall layout of the game later

![image](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/83218599/aa026c7c-441a-4e53-94c8-70149f7763d0)

- a problem is that it takes a little time to show the pause menu when you pause the game the first time

### Sprint 6 (20.06.2023 - 04.07.2023)

#### New Maps
- implemented a new map

![grafik](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/c5da42d7-623f-4a11-b1d9-68f16b5dba17)
- left and upper side indicate a bug in the map creation/drawing process, didn't get around to looking for that yet
- noted it down as an issue (https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/issues/40)

#### Finished Implementation of Status Effects (by Julian Häberle)
- completely revamped the cooldown system, the old approach with the singleshot timers didn't work

![grafik](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/1ee2c0ea-ce9d-4916-b47b-bb21db8b9c55)
- new cooldown system uses `time.time()` and adds the cooldown on top. The next call of the method checks whether `time.time()` returns a larger value.
- simpler than singleshot timers, more reliable, and doesn't need extra threading (since the singleshot timers themselves create an extra thread)

- fixed flaws in the method that calculates the position of the tile in the ArenaLayout Array

![grafik](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/0acf0e24-82a9-4961-b46e-abeb2019fe40)
- main problem here were the edge cases which sometimes returned invalid indices, which in return caused the program to crash

- added implementation for Slow and Speedup Statuseffects and tested them

![grafik](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/403332b9-ccc8-4610-b5f3-cb7fba513508)
- slow and speedup cancel each other respectively
- both get added two 200 because they're supposed to give a 50% malus/bonus at 100 stacks

#### Collision System for movement (by Julian Häberle)
- biggest problem so far
- in theory simple, in practice not so much
- the original idea was to check the edges of the robot for a collision, then block movement in that particular direction by modifying the movement vector

![grafik](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/b881f92f-9b45-4a0e-a22c-dd6c63602235)

- first iteration of this idea, function basically checks up to 90° to the left and right from the view direction for collisions
- expanding this to a full circle check would completely block the robot everytime it hit a wall
- this had a whole host of unintended consequences, from being able to move backwards into walls, over the currently non-player robots breaking completely, up to the robot getting permablocked in corners or on obstacles
- tried additional iterations of this, but they got very complex very fast and demanded a lot of performance
- abandoned this approach and began exploring in the opposite direction, with the simplest variant of collision detection
- the new approach is basically just "Can I go where I go?", merely checks if the new position is impassable or not and blocks the movement if it is
- implementation of this was trivial with the remainders of the original approach, but the result is much more reliable

![grafik](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/1c03f6a9-495d-4af2-995d-21bc707d359e)
- theoretically there exists an edge case where a robot at full speed could "jump" over an impassable tile, although I haven't managed to achieve this yet

#### Basic Health System (by Julian Häberle)
- very basic health system with health, maxHealth attributes and methods to manipulate those

![grafik](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/cdbc236e-1912-4f6c-a1bb-92a367865e16)
![grafik](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/9217e857-a8ac-4f40-9d18-f8694cd98bcc)
- basic cooldowns on healing and damage, work after the cooldown principle established by the status effects
- `applyDamage` implements the status effect Corrosion, which increases damage by 50% at full stacks
- might be expanded later on, if necessary

#### Adding Life-Bars (by Tom Kühnle)
- drawing Life-Bars for every robot centered over them
- life bars cannot have less than zero health, otherwise the lifebars start growing negatively
- the color green shows the remaining life, grey parts show the missing life
- adding a black outline to the Life-Bars

<img width="740" alt="Bildschirmfoto 2023-07-03 um 18 40 15" src="https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/104011823/633be935-0baf-4fe7-9e68-fce1472b3530">

- adding Life-Bars to the `paintEvent`
 
<img width="586" alt="Bildschirmfoto 2023-07-03 um 18 00 35" src="https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/104011823/a5415b69-d332-40b2-9821-3e60ea50e80a">

example for full life:

<img width="171" alt="Bildschirmfoto 2023-07-03 um 15 20 13" src="https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/104011823/951d668c-5bb2-4ce7-b4c2-05cf3eb8fcf0">

example at 70% health:

<img width="227" alt="Bildschirmfoto 2023-07-03 um 15 20 45" src="https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/104011823/591f1b18-ec0a-4a4d-bbb0-ede865ee30aa">

#### Bullet Shooting and Bullet Collision (by Tom Kühnle)
- creating bullet class with movement logic

<img width="425" alt="Bildschirmfoto 2023-07-03 um 20 24 37" src="https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/104011823/402f4e8f-9b03-4be5-9d02-be6b8fb0f5f0">

- creating a bullet list to store existing bullets
- setting timer intervall to 30ms for bullet drawing

<img width="556" alt="Bildschirmfoto 2023-07-03 um 20 26 08" src="https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/104011823/b6775421-a9a5-46b4-80f6-3a3c021079ac">

<img width="683" alt="Bildschirmfoto 2023-07-03 um 18 00 56" src="https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/104011823/9dd4fc31-6a28-48b7-8b7a-3ef436c30f30">

- setting the key to shoot bullets to spacebar
   -> left mousbutton did not work with touchpad, maybe implement diffrent
      options for shooting bullets later
  
<img width="341" alt="Bildschirmfoto 2023-07-03 um 21 26 46" src="https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/104011823/bd0db08c-2c2e-41fd-808c-4d0acd49f001">

- implementing logic for shooting the bullet and draw it at the right position
   -> did the math wrong for drawing the bullet at the right spot since
      the axes are inverted and I had to use -alpha , Thank you Julian :)
  
<img width="677" alt="Bildschirmfoto 2023-07-03 um 20 18 08" src="https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/104011823/7efaeb74-c9f7-4f8c-8c11-8744508b99e6">

- adding `timerEvent` to move the bullets and check for collision
- keep updating a list which stores bulltes to remove, if they:
    - are out of the arena boarders
    - did hit an enemy robot (collision check)
- If the collision check is true, the robot which got hit loses 10HP

<img width="936" alt="Bildschirmfoto 2023-07-03 um 20 18 20" src="https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/104011823/41e63386-400f-41c5-b25e-f0d3e6437155">

Example for shooting bullets:
https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/104011823/cf970938-3564-42f2-8389-fe16559ca2c1

Still undefined:
 - bullets can hurt the robot which shooted them
 - logic for dead robots is still to be implemented
 - bullet shooting needs to be restricted by a cooldown, otherwise a new bullet can
   be drawn every 30ms (redrawing rate of the bullets)

#### Main Menu (by Niklas Wolf)
![image](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/83218599/bd7ab753-9f61-4ea9-9a4b-6fce5d4fb3f7)

- added the new class GameMenu, which contains the widget of the Main Menu
- You can choose the number of players(1-2) and the arena layout(1-5) with spin boxes
  - for now, there are only two designs, more are following
- "Play" starts a new game, "Settings" doesn't have a function yet because we don't have any settings yet and "Quit" ends the game

![image](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/83218599/9909c12c-79f8-49d6-83a4-0249a7cd6f0c)

- Then had to add the main menu to the `RoboArena`

![image](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/83218599/9da75b72-c892-4822-b95d-479bf19bb48a)

- made a stacked widget, so the widgets change at the same position
- connected the "Play" button with the function `switchToGame`
  - function adds a widget of the game to the stack and saves the current values of the spin boxes
  - sets flag `game_running` to true, without the flag the program tries to pass the mouse and key events to the Arena widget, which doesn't exist at that moment
    
![image](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/83218599/f0dce541-228b-4813-b276-0108070a0ff4)

![image](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/83218599/0892b148-8cbc-4d78-9ab3-d95968e6b7ea)

![image](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/83218599/f3794061-5a43-44a4-a95e-cb0053c5f556)

- The `Arena` takes the values of the spin boxes and starts a new game
- changed the `is_player` parameter of the robots to `player_number` to check if the robot gets steered manually or randomly
  - if the player number is lower or equal to the number of players then it's a  player else it's random
- choosing is just comparing the given `arena_number` with its corresponding map
  - more maps has to be designed later

![image](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/83218599/779d783f-db5b-4f22-954f-099f61872e4d)

- returning to the main menu to the game is now connected to the "Quit"-Button of the pause menu, so you can choose a different map without restarting the whole application

![image](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/83218599/b83c1718-b654-4b08-8d0b-704c0ea53415)


### Sprint 7 (04.07.2023 - 018.07.2023)

#### Pathfinding (by Julian Häberle)
- implemented rudimentary pathfinding using the networkx library
- not fully functional as of now, still has major problems and will need to refactored/fixed at a later point
- works with a djikstra algorithm, using weighted edges
- weight of edges is determined by the tile they lead to, the weight leading to a standard tile without a status effect is 10, for tiles with benefitial status effects it's lower, for those with detrimental status effects it's lower
- intended was to deliver a mechanic that allows the AI robots to path through the map without incurring too much negativ status effects and to make their paths a bit predictable (i.E. the robot is much more likely to go over a field of cobblestone tiles then through a field of water tiles right next to it)

![grafik](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/74cfb3b4-3620-467b-89a8-996979ebe679)
- the ´initArena´ function has been expanded to first add tuples of coordinates as nodes to a graph and afterwards to initialize the edges between the nodes
- every tile in this sense is connected to the 8 tiles it surrounds
- it doesn't matter whether the tile is impassable or not, impassable tiles merely have a weight 9999, which should (in theory) exceed the weight of the longest shortest path

![grafik](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/7cf4fafc-6981-4d80-979d-d3be9679caf2)
- paths are either generated to intercept the players movement or to a random valid tile (a tile that is not impassable) of the arena
- robots will generate a random path if they collide with something, one of the major problems that I have not been able to get rid off yet

- apart from this most changes are either helper functions or minor changes to existing functions that are not overly important

#### Expanded Bulletsystem and Weapons (by Julian Häberle)
- this is based off the bulletsystem Tom implemented in the last sprint
- first I refactored the old system by extracting it from the Arena class and putting it into it's own thread
- When a bullet is fired, it's passed from the thread of the robot who fired it, into Arena and from Arena into the bulletThread

![grafik](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/a5410213-4972-4aa1-becb-78f13bd25f22)
- the bulletthread iterates over a copy of the bullet list, and discards bullets that have either hit a robot/wall or leave the arena
- on hit of a robot, the damage value of the bullet gets applied to the pawn
- the collision check against pawns is just a check against the euclidean distance from the center of the robot

![grafik](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/f87ed3a7-1963-4f69-b9b4-66363a374f43)
- the `weapon` class is the basic class of all weapons
- the `shoot` function is the function that fundamentally controls the weapons behaviour
- it checks whether the weapon is currently being cycled (basically the firerate) or reloaded, then it checks whether the weapon has rounds in the magazine
- based on the time since the last shot it is decided whether this shot is being treated as a consecutive shot
- based on the number of consecutive shots and the current speed of the robot in addition to the usual recoil, a accuracy penalty is applied
- this is done by adding a random factor drawn from a uniform distribution influenced by the accuracy penalty
- once all this is done, the bullet object is constructed and passed back to the caller of the function

![RoboArena-2023-07-17-12-49-39](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/a4d4e1e8-0ae2-48ff-a6cf-550c1e8ef614)

![grafik](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/b2cd371b-77b4-463d-aed6-1f1aeb93f755)
- the two other variations of weapons currently implemented
- the underlying principle is the same, only the initial parameters have been changed

![RoboArena-2023-07-17-12-50-14](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/c196035d-6375-409d-b25c-b5fbfb77fc60)
- Revolver

![RoboArena-2023-07-17-12-51-19](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/eff56af2-bbce-43f8-ac30-cbfc83bf8c48)
- Machinegun

#### Spawn and Death Mechanics (by Julian Häberle)
- Comparatively minor changes that enable us to handle spawning and killing robots
- killing and spawning is associated with a couple of intermediate steps like setting up and starting threads as well as adding the robot objects to the relevant lists

![grafik](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/6b09de41-510d-4368-9685-712aee81ea41)
- main part of the changes, basically just a couple of functions that handle the start of the threads and the removal/addition to lists

![grafik](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/e8805728-eb57-4d11-a142-11529cc2ad67)
- applyDamage now sets a death flag as soon as the robots hp fall to zero or below

![grafik](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/908ef8c4-6896-469a-b237-f86f1a26ebd9)
- the Death flag is queried by the thread of the robot, the thread will exit its loop as soon as the flag is set and proceed to remove the robot as well as spawn another one

#### Basic Game Loop (by Julian Häberle)
- contains basic victory conditions and checks for them (victory by points, time, kills as well as survival, which is essentially no victory condition)
- contains functionality to abort threads and return to the main menu upon win/loss
- implemented basic behaviour for robots (look in the players direction and shoot)
- implemented function to spawn enemy robots at valid positions throughout the arena
- UI implementation is to follow in the future

![grafik](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/82759282-2a93-4678-a7c0-5873bac8b496)
- basic checks of the three victory conditions

![grafik](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/56a02531-abef-4452-8624-88bab03c9f58)
- basic functionality for respawning the player, winning, losing and ending all relevant threads in a controlled manner
- the player can't be treated as other robots due to some codesmells that I'm going to get rid off in a future refactor

![grafik](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/839aa840-1e45-4b21-845c-36f08947d36e)
- changes to the run method in threads
- upon a kill, two new robots will be spawned at random positions in the arena
- robots will automatically turn towards the player and shoot at every opportunity, now matter whether it's possible to hit or not 

#### Add music (by Niklas Wolf)
![image](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/83218599/075a8f9e-eddd-48bc-b4bd-c7142dfdf45f)
- added the class `MusicPlayer` which gets a song and plays it in a loop
- also possible to change the volume of the song

![image](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/83218599/1816467c-6288-46e0-ba12-126194ef49ca)
- current volume values get saved in a config file
- don't have to change it every time you start the game and shares the value easily between the widgets

![image](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/83218599/c778192d-bc59-4855-adbf-fb56ae81ec4e)
![image](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/83218599/9f395bf9-ce47-4044-aa46-8b88be6c5a48)
- adding the `MusicPlayer` to the main window
- connecting the slider of the `PauseMenu` to the music player and setting the slider to the current value of the volume
- background music is at the moment Discord Amongst Operatives by TeknoAXE http://teknoaxe.com/Link_Code_3.php?q=1163


![image](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/83218599/e8354583-c0b3-49df-8790-10e0ed768dd9)
- added a volume icon to the `PauseMenu`

#### adding a menu for the settings (by Niklas Wolf)
![image](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/83218599/4759d005-b0b5-43ed-94b2-78f274728f37)
- added a widget to show the settings menu
- For now, the only settings are turning the music on and off and changing its volume like with the pause menu
- the settings are also saved in the config file

![image](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/83218599/4bbb12e4-9f89-474c-bd56-0e54e264198e)
- the method `toggleMusic` changes the value if the music is playing in the config file
- also changes the appearance of the button

![image](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/83218599/2e2aec25-8705-45f0-aa3c-e2efea64ece7)
- green "ON" if the music is playing
  
![image](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/83218599/95979231-e998-4564-9868-90796e31a4c8)
- red "OFF" if music is paused

#### Level System (by Tom Kühnle)
- adding new parameters necessary for leveling in the robot class

<img width="197" alt="Bildschirmfoto 2023-07-17 um 18 58 59" src="https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/104011823/58ed851a-57d6-4835-be78-cfe2cee62a72">

- experimental functions for experience handling
- if the player kills a robot, he will get experience (still needs refinement)
- if the experience needed for a level-up is reached, the level of the
  robot goes up by one
- after level-up the experience needed is extended by 10%
- functionality will be connected to the kill counter of Julian in the future

<img width="531" alt="Bildschirmfoto 2023-07-17 um 21 20 27" src="https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/104011823/8297483c-77c0-4d87-9b74-f68efd7d3bd3">

- added experience bar with display of the actual level of a player
- experience bar shows the amount of experience in relation to the experience
  needed for a level-up
- still needs to be connected to the actual state of the experience

<img width="966" alt="Bildschirmfoto 2023-07-17 um 21 21 32" src="https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/104011823/d387317a-f7d3-46ca-b865-9e3c4ea3f033">

<img width="1019" alt="Bildschirmfoto 2023-07-17 um 21 23 32" src="https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/104011823/faae0e21-22d9-47a8-b56e-ff2e97f5e348">

Example of the experience bar in the pause menu:

<img width="828" alt="Bildschirmfoto 2023-07-17 um 21 23 46" src="https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/104011823/0991637f-c617-48dc-a196-5fb1f1a72b5c">

-> everything still needs to be refined for the case that there is more than one 
   actual player



### Sprint 8 (18.07.2023 - 01.08.2023)

#### Better Models (by Julian Häberle)
- added models for enemies and the player
- taken from https://opengameart.org/content/top-down-sci-fi-shooter-characters-20
![Top-Down_Shooter_v2_1](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/5fd354c6-ca68-40f6-ba3d-497b5d08e2d1)

![tech](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/8c229874-977b-49f9-9ee5-264d1f35acfb)
-model for the player

![tech](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/7587ab67-98da-43ed-a35c-fe7ddf29171e)


![assault](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/8905d3a3-14fb-483c-b200-551eb8a0139b)

- unit of normal health/normal speed
- carries a machinegun (may be changed later to avoid overlap with the heavy gunner)
- no special behaviour yet, no particular plans yet
- standard enemy class

![assault](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/df0e787a-2107-4918-81c9-640b38b00394)


![cannoneer](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/06a271ce-82d4-427d-9048-b0c070cddb9c)
- unit of high health/slow speed
- carries a revolver (may be changed to a cannon to fit better)
- no specialized behaviour yet, but is supposed to become a CC enemy, that forces the player into cover with suppressing fire
- area denial enemy (maybe)

![cannoneer](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/bb9aa530-3cd8-47aa-8184-a836964f50be)


![heavy_gunner](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/ad835f0a-811a-496a-96bd-0f918288c459)
- unit of high health/slow speed
- carries a machinegun
- no specialized behaviour yet, may become an enemy that patrols a certain area of the map and tries to prevent the player from passing through
- hunting/suppressing enemy

![heavy_gunner](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/cae09ec6-4ccb-43cc-bb01-aa3123eb8cff)


![sniper](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/aaefcda3-7a45-487b-b7a7-4a70ba11e31e)
- unit of low health/low speed
- carries a sniper rifle (newly added weapon)
- no specialized behaviour yet, but is supposed to ambush the player and to do high damage accurately (still needs some work)
- hunting enemy

![sniper](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/b4661a5b-a3e2-48c4-9e52-757a57171c62)


![scout](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/13fe1d87-6a17-4260-b06f-52f14a980f6e)
- unit of low health/high speed
- carries a dual pistol (newly added weapon)
- no specialized behaviour yet, apart from the alternate fire of the dual pistols, is supposed to chase the player from cover
- hunting enemy

![scout](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/ad928f68-ace8-409b-904d-f06e1f434d59)

- the images for the different robots are loaded as pngs and scaled down
- the images are drawn and transformed in the `drawRobot` function

![grafik](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/65c2f10c-1d77-4c8f-961f-9ac3d1d4a3f6)
- it is very important that the translation to the center of the robot happens before the rotation, otherwise the robot will be rotated around the origin instead of its center
- the `resetTransform` function then resets the transformation matrices to prevent them from influencing the other robots
- the `shoot` method of the `bullet` class was modified to accept an offset_radius and offset_angle to align the origin of the bullet with the barrel of the model

- there are some additional minor code changes, but none of them is really important
- behaviours and different stats for enemies might be realized/refined with an additional object tying into the robot class


#### Victory/Defeat Screen (by Niklas Wolf)
Designed a "Victory" ...
![victory_screen](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/83218599/6d979bee-4b47-4ad4-b37d-58c7c96f4c75)

... and a "Defeat" screen
![defeat_screen](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/83218599/cc78563f-6e41-4f87-b834-33033918cfb6)


- should be as a half-transparent layer over the arena
- not implemented yet because of problems drawing it into the existing widget with a parent

### Sprint 9 (01.08.2023 - 15.08.2023)

#### Behaviour (by Julian Häberle)
- the `Behaviour` class controls the basic decision making of the enemies
- enemies mainly make their decision based on two factors, distance to the player and whether there's an unobstructed line of sight to the player
- more complex behaviour is currently a little complicated to implement because we lack the pathfinding ability
- the behaviour object is added to the robot, originally it was intended to be able to swap behaviours in one robot in one game based on how long it has been since the robot has "seen" the player
- for example, a standard behaviour might switch to a patrolling behaviour or a scouting behaviour after a certain time of no contact
- due to lack of time this was not implemented
- five behaviours overall were implemented: Standard, Patrolling, Stationary, Sniping and Scouting
- `getAngle` and `openFire` functions work the same for every behaviour
- `getAngle` decides whether the robot looks at a random point within it's `awareness_distance` or whether it looks at the player
- this depends on the `awareness_threshold` and whether or not the robot has a line of sight
- the `openFire` Function works much the same way
- the robot opens fire if the distance to the player is lower than the `fire_threshold`, the line of sight is unobstructed and the angle points at the player (the bool for whether the angle points at the player is set in `getAngle`
- additionally there are a `accelerate`, a `decelerate` and a `reload` function
- `accelerate` and `decelerate` are only used by the `scouting` behaviour and are configured for just the scout
- `reload` decides whether the robot reloads based on an ammo threshold defined in each behaviour

![grafik](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/67464857/e398af0b-7682-4f1a-b17b-91a5387ab337)
- the `hasLineOfSightToPoint` function calculates a line equation and then iteratively traverses the line from one point to the other
- should one iteration meet an impassable tile, it returns False, otherwise it returns true

- Standard behaviour is assigned to the standard enemy
- it moves to random points within a certain `patrol_radius` until the player enters it's `distance_threshold`

- Patrolling behaviour is assigned to the heavy_gunner enemy
- the enemy moves to random points within its `patrol_radius` around it's initial position, it does not follow the player

- Stationary behaviour is assigned to the cannoneer
- the cannoneer doesn't move and instact acts like a gun turret

- Sniping behaviour is assinged to the sniper
- the sniper tries to back away from the player once the player enters the `distance_threshold`
- upon firing the sniper ceases movement until it stops firing

- Scouting behaviour is assigned to the scout
- the scout charges the player as soon as it has a line of sight and accelerates the closer it gets to the player

- apart from the behaviour and the associated code, the behaviour branch contains a clean-up of assets and maps, some minor refactors and a lot of added commentary

#### Display stats (by Niklas Wolf)
![stats-screen](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/83218599/fbd4decb-86b1-4127-8de8-7cfaaac70445)

- stats showing the played time, health, points, kills, the weapon with ammunition and if the weapon is reloading, and the values of the active effects
  
![stats-screen](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/83218599/f02feedf-3dbc-48ce-abef-0db86913af7e)
- changing the stats by emitting a signal if the values change and connecting it to the update function
- problems by taking signals of nested classes, especially if they aren't a QObject
  - the classes called the other classes had to take the values and emit them as signals

![timer-function](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/83218599/2bf48d58-b5cb-4c1d-95bb-5c56a8e4dfbc)
- implementation of the timer
- increasing the counter every 1000ms by reacting to the timer signal
  
#### Implementation of win/lose screen (by Niklas Wolf)
![image](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/83218599/e5b2fd73-7b79-4365-a253-6e7fe893d595)

- calling the end screen and passing the last picture of the game as a screenshot, so it looks like an overlay but avoids the problem of the threads
![defeat](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/83218599/5a6c5305-ff50-4c2c-8a6e-a66b2be3827b)

#### Improving the design of the pause and game menu (by Niklas Wolf)
- know now better how to handle the labels, buttons and backgrounds in the widgets, so I reworked the menus I did at the beginning

Pause menu:
![pause-menu](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/83218599/b090d2ef-0ed5-45c4-b49f-51c2327d40ef)

Game Menu:
![game-menu](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/83218599/a7f7e984-c5cf-4aa0-b62a-063c880ed0d5)

#### New Map and PP Presentation (by Tom Kuehnle)

- creating new map, which has slightly different spawn points if you choose it

New Map:
![map2](https://github.com/Robo-Arena-Team-2-Uni-Tuebingen/Roboarena-Team-2/assets/104011823/7bbaca8e-d8f1-4a19-a77f-e02c29228fae)

- Creating power point presentation


