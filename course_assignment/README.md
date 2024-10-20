# Course Assignment - Conway's Game of Life

This project involves designing, architecting, and developing John Conway's Game of Life while applying the design patterns covered in the course.

## Classes and Design Patterns

1. **Game** (Singleton, State, Observer)
   - Purpose: Central control of the game logic and state.
   - Patterns: Singleton ensures only one game instance, State manages game states, Observer for updates.

2. **Grid** (Observer)
   - Purpose: Represents the game board and manages cell interactions.
   - Pattern: Observer pattern to notify when the grid state changes and update the cells accordingly.

3. **Cell** (State)
   - Purpose: Represents individual cells in the game.
   - Pattern: State pattern to manage alive/dead states and transitions.

4. **GridBuilder** (Builder)
   - Purpose: Constructs complex Grid objects.
   - Pattern: Builder pattern for step-by-step creation of Grid objects.

5. **CellFactory** and **RandomCellFactory** (Factory Method)
   - Purpose: Creates Cell objects.
   - Pattern: Factory Method for creating cells with different initial states.

6. **Renderer** and its subclasses (Strategy, Template Method)
   - Purpose: Handles the rendering of the game state.
   - Patterns: Strategy for swappable rendering algorithms, Template Method for common rendering structure.

7. **GameTicker** (Observer)
   - Purpose: Manages game update intervals.
   - Pattern: Observer pattern to notify when it's time to update the game state.

8. **InputAdapter** (Adapter)
   - Purpose: Handles user input and interfaces with the game.
   - Pattern: Adapter pattern to convert user inputs into game actions.

9. **GameState** and its subclasses (State)
   - Purpose: Represents different states of the game (e.g., Running, Paused).
   - Pattern: State pattern to manage game state transitions.

10. **RendererStyle** (Enum)
    - Purpose: Defines different rendering styles available in the game.
    - While not a design pattern itself, it supports the Strategy pattern used in renderers.

This implementation demonstrates the use of multiple design patterns to create a flexible, maintainable, and extensible Game of Life simulation. Each class and pattern serves a specific purpose in managing the complexity of the game's logic, rendering, and user interaction.
