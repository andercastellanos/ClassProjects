public class LoseException extends Throwable {
    String name; // A string representing the name associated with the exception
    Player player; // A reference to a Player object associated with the exception

    // Constructor to create a LoseException with a name and a Player
    public LoseException(String name, Player player) {
        this.name = name; // Assign the provided name to the name field
        this.player = player; // Assign the provided Player object to the player field
    }
}
