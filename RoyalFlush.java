public class RoyalFlush extends HandCategory {
    Suit suit;

    public RoyalFlush(Suit suit) {
        this.suit = suit;
    }

    @Override
    public String toString() {
        return "RoyalFlush [suit=" + suit + "]";
    }

    @Override
    int compareRank(Object right0) {
        RoyalFlush right = (RoyalFlush) right0;
        return suit.compareTo(right.suit);
    }

    @Override
    int category() {
        return 1;
    }

}
