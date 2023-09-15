public class LoseException extends Throwable {
    String name;
    Player player;

    public LoseException(String name, Player player) {
        this.name = name;
        this.player = player;
    }
}
